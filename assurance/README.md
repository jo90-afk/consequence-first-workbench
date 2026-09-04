# Distribution assurance

Run with Python 3.11 or later:

```sh
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
python3 scripts/validate_distribution.py
```

GitHub Actions runs the harness regressions as Quality, then validates the actual
distribution as Assurance. The checks cover the marketplace-to-plugin mapping,
the explicit eleven-skill inventory, manifest/VERSION/README consistency, YAML
frontmatter, invocation prompts, icons, local Markdown resources, duplicate keys,
and encoded or symlink path escapes. The validator deliberately supports this
repository's local-only bundle contract, not every possible Codex extension.

The public gate also rejects private distribution identifiers. It has no access
to private repository content or credentials. The private repository separately
checks public candidates for copied protected passages using fingerprints kept
only in that private repository. These checks catch known accidental copying;
they cannot establish that arbitrary newly written prose contains no private
information. Review intentional public changes against the author-neutral scope.

## Activation observations

`activation-cases.json` encodes the five positive and three negative scenarios in
the submission test cases. Required/forbidden activation sets are executable;
the expected reasoning and resulting behavior are human-reviewed criteria.
The fixtures in the unit tests are entirely neutral and synthetic. A passing
Actions run proves the distribution and evaluation harness, not model behavior.

To evaluate an installed candidate:

1. Install the exact candidate bundle in an isolated host profile. Start a fresh
   conversation for every case; enable only this workbench distribution so that
   other installed copies cannot produce an ambiguous activation trace.
2. Prepare a blank observation record:

   ```sh
   mkdir -p .evaluation
   python3 scripts/evaluate_activation.py plan > .evaluation/results.json
   ```

3. Use each exact prompt and its `setup` instructions. Keep all fixtures neutral.
   Record the host, model, full candidate Git SHA, time and independent reviewer.
   Save the host's full skill/tool trace and assistant response alongside the
   observation record. Include fixture inputs and before/after evidence when a
   criterion concerns a file change. Do not infer activation from answer wording.
4. Fill `activated_skills` with this bundle's skills observed in that trace.
   Supply an exact trace excerpt for each in `activation_evidence`. An empty list
   is a measured negative observation; `null` means not yet evaluated. The reviewer
   must inspect the complete trace to establish absence for negative cases.
5. Fill each trace/response path and its SHA-256 digest. Paths must remain inside
   the observation directory. Review every criterion; set `passed` only after
   checking actual behavior and retain an exact response or trace excerpt.
6. Score the recorded evidence:

   ```sh
   python3 scripts/evaluate_activation.py score .evaluation/results.json
   ```

The scorer rejects incomplete observations, stale distribution digests, missing
provenance, altered evidence, required or forbidden activation failures and
unreviewed/failed criteria. Its acceptance reports checks on recorded evidence;
human rubric judgments remain judgments. No provider is invoked, no paid model
run is started, and no trace is fabricated. Keep real evaluation output out of
the public repository by default; share only deliberately reviewed, neutral runs.

Version 1.0.0 remains the distributed plugin version because this change adds
repository assurance without changing the installed skill contents.
