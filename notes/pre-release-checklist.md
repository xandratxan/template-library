## Pre-release checklist template (fill before tagging)

Copy this template into your release issue or checklist, fill the metadata fields, and check items as you complete them.

```
RELEASE METADATA
- Release tag: v0.0.4
- Target branch: main
- Release manager: Xandra Campo
- Date (planned): 2025/12/14
- CI run URL: 
- CHANGELOG entry link or path: 

CHECKLIST
[ ] 1. Versioning
    - [ ] Repository version bumped to release version (e.g., pyproject.toml / package.json)
    - [ ] Version in code/docs matches tag

[ ] 2. Changelog & Release Notes
    - [ ] CHANGELOG.md updated with user-facing notes
    - [ ] Release notes drafted and reviewed (link or file)

[NA] 3. Tests & CI
    - [X] Unit tests passing (link to CI run)
    - [X] Integration / end-to-end tests passing (if applicable)
    - [NA] Linting / static checks green

[NA] 4. Security & Compliance
    - [X] Secrets scan completed (no sensitive data in the release commit)
    - [X] Dependency security scan results reviewed
    - [X] License files present and correct

[NA] 5. Build & Artifacts
    - [NA] Build completed locally or in CI (list commands run)
    - [NA] Built artifacts present in `dist/` or artifacts storage
    - [NA] Artifacts checksums generated (sha256) and recorded
    - [NA] Artifacts signed (GPG or code-signing), if required

[NA] 6. Tagging & Git
    - [NA] Annotated tag created locally: `git tag -a <tag> -m "Release <tag>"`
    - [NA] (Optional) Tag signed: `git tag -s <tag> -m "Release <tag>"`
    - [NA] Tag pushed to origin: `git push origin <tag>`

[ ] 7. GitHub Release & Assets
    - [ ] Draft GitHub Release created (or planned automation configured)
    - [ ] Release notes copied into release body
    - [ ] Built artifacts uploaded to Release or available for package publish

[NA] 8. Publishing to package registries
    - [NA] PyPI / npm / Docker credentials present and valid
    - [NA] Publish to registries executed (or scheduled by CI)
    - [NA] Publish verification completed (pip install / docker pull smoke test)

[ ] 9. Documentation & Post-release
    - [ ] Docs updated (if version-specific docs required)
    - [ ] Versioned docs built and published (if applicable)
    - [ ] CHANGELOG or release notes linked from main docs

[NA] 10. Communication & Monitoring
    - [NA] Announcement draft ready (email, Slack, Twitter, etc.)
    - [NA] Stakeholders and on-call notified of release window
    - [NA] Monitoring/alerts watched for regressions after release

[NA] 11. Rollback / Hotfix plan
    - [NA] Hotfix branch strategy decided (branch name / owner)
    - [NA] Rollback instructions noted (what to revert and how)

POST-RELEASE SMOKE TEST (perform immediately after publishing)
- [NA] Install or download the published artifact and run a quick smoke test
- [NA] Confirm basic functionality (describe expected steps)
- [NA] Verify checksums and signatures (if applicable)

NOTES / LINKS
- Links to CI runs / build artifacts / relevant issues:

```