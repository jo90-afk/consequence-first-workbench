"""Neutral synthetic fixtures test the harness, not the skills or a model."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_distribution import Invalid, validate
from evaluate_activation import plan, score


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


class AssuranceTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        self.plugin = self.root / "plugins/example-tools"
        self.skill = self.plugin / "skills/workflow-tool"
        self.skill.mkdir(parents=True)
        self.contract = {"schema_version": 1, "visibility": "public", "plugin_name": "example-tools",
                         "marketplace_name": "example-tools", "skills": ["workflow-tool"],
                         "forbidden_identifiers": ["private-example-guidance"]}
        write_json(self.root / "assurance/distribution.json", self.contract)
        write_json(self.root / ".agents/plugins/marketplace.json", {
            "name": "example-tools", "interface": {"displayName": "Example tools"},
            "plugins": [{"name": "example-tools", "category": "Productivity",
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "source": {"source": "local", "path": "./plugins/example-tools"}}]})
        write_json(self.plugin / ".codex-plugin/plugin.json", {"name": "example-tools", "version": "1.0.0",
            "description": "Neutral test fixture", "skills": "./skills", "interface": {
                "displayName": "Example tools", "category": "Productivity", "capabilities": []}})
        (self.root / "VERSION").write_text("1.0.0\n")
        (self.root / "README.md").write_text("Version 1.0.0\n")
        (self.skill / "SKILL.md").write_text("---\nname: workflow-tool\ndescription: A neutral test skill\n---\nRead [guide](references/guide.md).\n")
        (self.skill / "references").mkdir()
        (self.skill / "references/guide.md").write_text("Neutral public guide.\n")
        (self.skill / "assets").mkdir()
        (self.skill / "assets/icon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
        (self.skill / "agents").mkdir()
        (self.skill / "agents/openai.yaml").write_text(
            "interface:\n  display_name: Example\n  short_description: Neutral tool\n"
            "  default_prompt: Use $workflow-tool to change this workflow.\n"
            "  icon_small: assets/icon.svg\n  icon_large: assets/icon.svg\n"
            "policy:\n  allow_implicit_invocation: true\n")
        self.cases = {"schema_version": 1, "cases": [
            {"id": "positive", "kind": "positive", "prompt": "Change a neutral workflow.",
             "required_skills": ["workflow-tool"], "forbidden_skills": [], "forbid_all": False,
             "review_criteria": {"bounded": "Preserve the stated boundary."}},
            {"id": "negative", "kind": "negative", "prompt": "What is two plus two?",
             "required_skills": [], "forbidden_skills": [], "forbid_all": True,
             "review_criteria": {"direct": "Answer directly."}}]}
        write_json(self.root / "assurance/activation-cases.json", self.cases)

    def mutate_json(self, path, update):
        data = json.loads(path.read_text())
        update(data)
        write_json(path, data)

    def assert_invalid(self, pattern=None):
        with self.assertRaisesRegex((Invalid, ValueError), pattern or ".*"):
            validate(self.root)

    def evidence(self):
        folder = Path(self.temp.name) / "observations"
        folder.mkdir(exist_ok=True)
        evidence = plan(self.root)
        evidence.update(host="synthetic test harness", model="no model invoked", reviewer="unit test",
                        candidate_sha="a" * 40, observed_at="2026-01-01T00:00:00Z")
        for record in evidence["cases"]:
            activated = ["workflow-tool"] if record["id"] == "positive" else []
            record["activated_skills"] = activated
            trace = "SYNTHETIC: loaded workflow-tool" if activated else "SYNTHETIC: no skills loaded"
            response = "SYNTHETIC: approved outcome."
            for kind, text in [("trace", trace), ("response", response)]:
                path = folder / (record["id"] + "." + kind + ".txt")
                path.write_text(text)
                record[kind] = {"path": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            record["activation_evidence"] = {name: trace for name in activated}
            record["review"] = {key: {"passed": True, "excerpt": response} for key in record["review"]}
        path = folder / "results.json"
        write_json(path, evidence)
        return path, evidence

    def test_valid_distribution(self):
        self.assertEqual(validate(self.root)["skills"], 1)

    def test_version_mismatch(self):
        (self.root / "VERSION").write_text("1.0.1")
        self.assert_invalid("mismatch")

    def test_readme_version_mismatch(self):
        (self.root / "README.md").write_text("Version 1.0.2")
        self.assert_invalid("README")

    def test_manifest_name_mismatch(self):
        self.mutate_json(self.plugin / ".codex-plugin/plugin.json", lambda x: x.update(name="other"))
        self.assert_invalid("manifest name")

    def test_remote_marketplace_source_rejected(self):
        self.mutate_json(self.root / ".agents/plugins/marketplace.json", lambda x: x["plugins"][0]["source"].update(source="github"))
        self.assert_invalid("local bundle")

    def test_unreviewed_manifest_component_rejected(self):
        self.mutate_json(self.plugin / ".codex-plugin/plugin.json", lambda x: x.update(mcpServers={"new-server": {}}))
        self.assert_invalid("unreviewed plugin component")

    def test_changed_installation_policy_rejected(self):
        self.mutate_json(self.root / ".agents/plugins/marketplace.json", lambda x: x["plugins"][0]["policy"].update(authentication="NEVER"))
        self.assert_invalid("unreviewed installation")

    def test_marketplace_traversal_rejected(self):
        self.mutate_json(self.root / ".agents/plugins/marketplace.json", lambda x: x["plugins"][0]["source"].update(path="../"))
        self.assert_invalid("escapes")

    def test_duplicate_json_key_rejected(self):
        (self.plugin / ".codex-plugin/plugin.json").write_text('{"name":"one","name":"two"}')
        self.assert_invalid("duplicate key")

    def test_duplicate_yaml_key_rejected(self):
        (self.skill / "SKILL.md").write_text("---\nname: workflow-tool\nname: other\n---\n")
        self.assert_invalid("duplicate key")

    def test_missing_resource_rejected(self):
        (self.skill / "references/guide.md").unlink()
        self.assert_invalid("missing file")

    def test_nested_reference_is_checked(self):
        (self.skill / "references/guide.md").write_text("Read [next][n].\n[n]: missing.md\n")
        self.assert_invalid("missing file")

    def test_encoded_traversal_rejected(self):
        with (self.skill / "SKILL.md").open("a") as f:
            f.write("Read [outside](%2e%2e/%2e%2e/%2e%2e/README.md).\n")
        self.assert_invalid("escapes")

    def test_absolute_icon_rejected(self):
        path = self.skill / "agents/openai.yaml"
        path.write_text(path.read_text().replace("assets/icon.svg", str(self.skill / "assets/icon.svg")))
        self.assert_invalid("invalid resource path")

    def test_symlink_rejected_even_when_target_is_inside_bundle(self):
        path = self.skill / "references/alias.md"
        path.symlink_to("guide.md")
        self.assert_invalid("symlink")

    def test_unknown_skill_rejected(self):
        (self.plugin / "skills/extra").mkdir()
        self.assert_invalid("inventory changed")

    def test_wrong_prompt_invocation_rejected(self):
        path = self.skill / "agents/openai.yaml"
        path.write_text(path.read_text().replace("$workflow-tool", "$workflow-tool-extra"))
        self.assert_invalid("does not invoke")

    def test_private_identifier_rejected(self):
        (self.skill / "references/guide.md").write_text("private-example-guidance")
        self.assert_invalid("private distribution identifier")

    def test_negative_case_is_required(self):
        self.cases["cases"].pop()
        write_json(self.root / "assurance/activation-cases.json", self.cases)
        self.assert_invalid("positive and negative")

    def test_unknown_activation_skill_rejected(self):
        self.cases["cases"][0]["required_skills"] = ["absent"]
        write_json(self.root / "assurance/activation-cases.json", self.cases)
        self.assert_invalid("unknown skill")

    def test_contradictory_expectations_rejected(self):
        self.cases["cases"][0]["forbid_all"] = True
        write_json(self.root / "assurance/activation-cases.json", self.cases)
        self.assert_invalid("contradictory")

    def test_plan_is_explicitly_unobserved(self):
        self.assertIsNone(plan(self.root)["cases"][0]["activated_skills"])

    def test_synthetic_observations_exercise_scorer(self):
        path, _ = self.evidence()
        self.assertEqual(score(self.root, path)["cases"], 2)

    def test_required_activation_failure(self):
        path, data = self.evidence()
        data["cases"][0]["activated_skills"] = []
        write_json(path, data)
        with self.assertRaisesRegex(Invalid, "required activation"):
            score(self.root, path)

    def test_negative_overactivation_failure(self):
        path, data = self.evidence()
        data["cases"][1]["activated_skills"] = ["workflow-tool"]
        write_json(path, data)
        with self.assertRaisesRegex(Invalid, "overactivated"):
            score(self.root, path)

    def test_specific_forbidden_activation_failure(self):
        self.cases["cases"][1].update(forbid_all=False, forbidden_skills=["workflow-tool"])
        write_json(self.root / "assurance/activation-cases.json", self.cases)
        path, data = self.evidence()
        data["cases"][1]["activated_skills"] = ["workflow-tool"]
        write_json(path, data)
        with self.assertRaisesRegex(Invalid, "forbidden activation"):
            score(self.root, path)

    def test_unreviewed_rubric_fails(self):
        path, data = self.evidence()
        data["cases"][0]["review"]["bounded"]["passed"] = None
        write_json(path, data)
        with self.assertRaisesRegex(Invalid, "unreviewed"):
            score(self.root, path)

    def test_changed_artifact_fails(self):
        path, data = self.evidence()
        (path.parent / data["cases"][0]["trace"]["path"]).write_text("altered")
        with self.assertRaisesRegex(Invalid, "digest mismatch"):
            score(self.root, path)

    def test_missing_trace_anchor_fails(self):
        path, data = self.evidence()
        data["cases"][0]["activation_evidence"]["workflow-tool"] = "invented trace excerpt"
        write_json(path, data)
        with self.assertRaisesRegex(Invalid, "anchor absent"):
            score(self.root, path)

    def test_evidence_cannot_escape_folder(self):
        path, data = self.evidence()
        data["cases"][0]["trace"]["path"] = "../repo/README.md"
        write_json(path, data)
        with self.assertRaisesRegex(Invalid, "escapes"):
            score(self.root, path)

    def test_stale_distribution_fails(self):
        path, _ = self.evidence()
        (self.skill / "references/guide.md").write_text("A changed neutral guide.")
        with self.assertRaisesRegex(Invalid, "stale distribution"):
            score(self.root, path)

    def test_stale_rubric_fails(self):
        path, _ = self.evidence()
        self.cases["cases"][0]["review_criteria"]["bounded"] = "A materially different required behavior."
        write_json(self.root / "assurance/activation-cases.json", self.cases)
        with self.assertRaisesRegex(Invalid, "stale activation suite"):
            score(self.root, path)

    def test_missing_provenance_fails(self):
        path, data = self.evidence()
        data["model"] = ""
        write_json(path, data)
        with self.assertRaisesRegex(Invalid, "provenance"):
            score(self.root, path)


if __name__ == "__main__":
    unittest.main()
