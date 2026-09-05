#!/usr/bin/env python3
"""Validate this repository's supported, local-only marketplace contract.

This is distribution integrity evidence, not a model-behavior evaluation or a
complete implementation of every Codex manifest extension.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate key: {key}")
        result[key] = value
    return result


class UniqueLoader(yaml.SafeLoader):
    pass


def yaml_mapping(loader, node):
    return unique_pairs((loader.construct_object(k), loader.construct_object(v))
                        for k, v in node.value)


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, yaml_mapping)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)


def local_path(base, value, boundary, kind="file"):
    require(isinstance(value, str) and bool(value.strip()), "empty local path")
    parsed = urlsplit(value)
    require(not parsed.scheme and not parsed.netloc and not parsed.query,
            f"resource must be local: {value}")
    decoded = unquote(parsed.path)
    require(decoded and not Path(decoded).is_absolute() and "\\" not in decoded,
            f"invalid resource path: {value}")
    path = base / decoded
    # Reject symlinks rather than following one into another distribution.
    for parent in [path, *path.parents]:
        if parent == boundary.parent:
            break
        require(not parent.is_symlink(), f"symlink resource: {value}")
    resolved = path.resolve()
    require(resolved.is_relative_to(boundary.resolve()), f"resource escapes boundary: {value}")
    require(resolved.is_dir() if kind == "dir" else resolved.is_file(),
            f"missing {kind}: {value}")
    return resolved


def markdown_resources(path, boundary):
    content = path.read_text(encoding="utf-8")
    # The bundles use inline Markdown links; reference-style definitions are
    # checked too. Anchor-only links and public web/mail links need no local file.
    targets = re.findall(r"\]\(\s*(<[^>]+>|[^\s)]+)", content)
    targets += re.findall(r"^\s*\[[^\]]+\]:\s*(\S+)", content, re.MULTILINE)
    for target in targets:
        target = target.strip("<>")
        if target.startswith("#"):
            continue
        parsed = urlsplit(target)
        if parsed.scheme in {"https", "http", "mailto"}:
            continue
        local_path(path.parent, target, boundary)


def skill_metadata(skill):
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    parts = text.split("---", 2)
    require(len(parts) == 3 and not parts[0].strip(), f"missing frontmatter: {skill.name}")
    meta = yaml.load(parts[1], Loader=UniqueLoader)
    require(isinstance(meta, dict), f"invalid frontmatter: {skill.name}")
    require(meta.get("name") == skill.name, f"skill name mismatch: {skill.name}")
    require(isinstance(meta.get("description"), str) and meta["description"].strip(),
            f"missing description: {skill.name}")
    config = yaml.load((skill / "agents/openai.yaml").read_text(), Loader=UniqueLoader)
    require(isinstance(config, dict) and isinstance(config.get("interface"), dict),
            f"missing interface: {skill.name}")
    interface = config["interface"]
    for key in ["display_name", "short_description", "default_prompt"]:
        require(isinstance(interface.get(key), str) and interface[key].strip(),
                f"missing {key}: {skill.name}")
    require(re.search(r"\$" + re.escape(skill.name) + r"(?![a-z0-9-])", interface["default_prompt"]),
            f"default prompt does not invoke its skill: {skill.name}")
    for key in ["icon_small", "icon_large"]:
        local_path(skill, interface.get(key), skill)
    policy = config.get("policy", {})
    require(type(policy.get("allow_implicit_invocation")) is bool,
            f"implicit invocation policy must be boolean: {skill.name}")
    for resource in skill.rglob("*.md"):
        markdown_resources(resource, skill)


def validate_cases(root, skills):
    cases = read_json(root / "assurance/activation-cases.json")
    require(cases.get("schema_version") == 1, "unsupported activation contract")
    require(isinstance(cases.get("cases"), list) and cases["cases"], "empty activation suite")
    ids = set()
    polarities = set()
    for case in cases["cases"]:
        require(isinstance(case.get("id"), str) and re.fullmatch(r"[a-z0-9-]+", case["id"]), "invalid case id")
        require(case["id"] not in ids, "duplicate activation case")
        ids.add(case["id"])
        require(case.get("kind") in {"positive", "negative"}, "invalid case kind")
        polarities.add(case["kind"])
        require(isinstance(case.get("prompt"), str) and case["prompt"].strip(), "missing prompt")
        for key in ["required_skills", "forbidden_skills"]:
            require(isinstance(case.get(key), list), f"missing {key}")
            require(len(case[key]) == len(set(case[key])), f"duplicate {key}")
            require(set(case[key]) <= skills, f"unknown skill in {case['id']}")
        require(not set(case["required_skills"]) & set(case["forbidden_skills"]), "contradictory expectations")
        require(type(case.get("forbid_all")) is bool, "missing forbid_all")
        require(not (case["forbid_all"] and case["required_skills"]), "contradictory forbid_all")
        if case["kind"] == "positive":
            require(case["required_skills"], "positive case requires no skill")
        else:
            require(case["forbid_all"] or case["forbidden_skills"], "negative case excludes no skill")
        require(isinstance(case.get("review_criteria"), dict) and case["review_criteria"], "missing human rubric")
        require(all(isinstance(k, str) and isinstance(v, str) and v.strip()
                    for k, v in case["review_criteria"].items()), "invalid human rubric")
    require(polarities == {"positive", "negative"}, "suite needs positive and negative cases")
    if cases.get("source"):
        source = local_path(root, cases["source"], root).read_text(encoding="utf-8")
        documented = re.findall("Prompt: “(.*?)”", source)
        require(documented == [c["prompt"] for c in cases["cases"]], "activation prompts drifted from submission cases")
    return cases


def distribution_digest(root):
    """Bind behavior evidence to the exact marketplace and distributed files."""
    paths = [root / ".agents/plugins/marketplace.json"]
    paths += sorted(p for p in (root / "plugins").rglob("*") if p.is_file())
    digest = hashlib.sha256()
    for path in paths:
        digest.update(str(path.relative_to(root)).encode() + b"\0" + path.read_bytes() + b"\0")
    return digest.hexdigest()


def validate(root):
    root = root.resolve()
    contract = read_json(root / "assurance/distribution.json")
    require(contract.get("schema_version") == 1, "unsupported distribution contract")
    require(contract.get("visibility") in {"public", "private"}, "invalid distribution visibility")
    name = contract["plugin_name"]
    require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name), "invalid plugin name")
    catalog = read_json(root / ".agents/plugins/marketplace.json")
    require(catalog.get("name") == contract["marketplace_name"], "marketplace name mismatch")
    require(isinstance(catalog.get("interface"), dict) and catalog["interface"].get("displayName"), "missing marketplace interface")
    require(len(catalog.get("plugins", [])) == 1, "review contract before adding marketplace entries")
    entry = catalog["plugins"][0]
    require(entry.get("name") == name, "marketplace/plugin name mismatch")
    require(entry.get("policy") == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "unreviewed installation/authentication policy")
    source = entry.get("source", {})
    require(source.get("source") == "local", "only local bundle sources are approved")
    plugin = local_path(root, source.get("path"), root, "dir")
    require(plugin == root / "plugins" / name, "marketplace points to the wrong bundle")
    for path in (root / "plugins").rglob("*"):
        require(not path.is_symlink(), f"symlink in distribution: {path.relative_to(root)}")
        require(path.is_relative_to(plugin) or path == plugin, "unexpected plugin directory")
    manifest = read_json(plugin / ".codex-plugin/plugin.json")
    require(set(manifest) <= {"name", "version", "description", "author", "skills", "interface"},
            "unreviewed plugin component or manifest extension")
    require(manifest.get("name") == name, "manifest name mismatch")
    version = (root / "VERSION").read_text().strip()
    require(re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", version), "invalid version")
    require(manifest.get("version") == version, "manifest/VERSION mismatch")
    require(entry.get("version", version) == version, "marketplace version mismatch")
    for found in re.findall(r"\bVersion\s+(\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)", (root / "README.md").read_text()):
        require(found == version, "README version mismatch")
    require(isinstance(manifest.get("description"), str) and manifest["description"].strip(), "missing plugin description")
    require(isinstance(manifest.get("interface"), dict) and manifest["interface"].get("displayName"), "missing plugin interface")
    require(manifest["interface"]["displayName"] == catalog["interface"]["displayName"], "marketplace display name mismatch")
    require(entry.get("category") == manifest["interface"].get("category") == "Productivity", "category mismatch")
    require(manifest["interface"].get("capabilities") == [], "unreviewed plugin capabilities")
    skills_root = local_path(plugin, manifest.get("skills"), plugin, "dir")
    require(skills_root == plugin / "skills", "unexpected skills root")
    skills = {p.name for p in skills_root.iterdir() if p.is_dir()}
    require(len(contract["skills"]) == len(set(contract["skills"])), "duplicate contract skill")
    require(skills == set(contract["skills"]), "skill inventory changed; review distribution contract")
    for skill in sorted(skills):
        skill_metadata(skills_root / skill)
    if contract["visibility"] == "public":
        for path in plugin.rglob("*"):
            if path.is_file() and path.suffix in {".md", ".yaml", ".json", ".svg"}:
                content = path.read_text(encoding="utf-8")
                for token in contract.get("forbidden_identifiers", []):
                    require(token not in content, f"private distribution identifier in {path.relative_to(root)}")
    cases = validate_cases(root, skills)
    return {"plugin": name, "version": version, "skills": len(skills),
            "activation_cases": len(cases["cases"]), "distribution_sha256": distribution_digest(root),
            "evidence_scope": "distribution integrity and scenario contract; no model run"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        print(json.dumps(validate(args.root), indent=2))
    except (Invalid, KeyError, TypeError, OSError, ValueError, yaml.YAMLError) as error:
        parser.exit(1, f"distribution validation failed: {error}\n")


if __name__ == "__main__":
    main()
