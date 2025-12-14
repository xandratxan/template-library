# Pre-release checklist template (fill before tagging)

Copy this template into your release issue or checklist, fill the metadata fields, and check items as you complete them.

```
RELEASE METADATA
- Release tag: v0.0.5
- Target branch: main
- Release manager: Xandra Campo
- Date (planned):
- CI run URL: 
- CHANGELOG entry link or path: 

CHECKLIST
[ ] 1. Versioning
    - [ ] Repository version bumped to release version (e.g., pyproject.toml / package.json)
    - [ ] Version in code/docs matches tag

[ ] 2. Changelog & Release Notes
    - [ ] CHANGELOG.md updated with user-facing notes
    - [ ] Release notes drafted and reviewed (link or file)

[ ] 3. Tests & CI
    - [ ] Unit tests passing (link to CI run)
    - [ ] Integration / end-to-end tests passing (if applicable)
    - [ ] Linting / static checks green

[ ] 4. Security & Compliance
    - [ ] Secrets scan completed (no sensitive data in the release commit)
    - [ ] Dependency security scan results reviewed
    - [ ] License files present and correct

[ ] 5. Build & Artifacts
    - [ ] Build completed locally or in CI (list commands run)
    - [ ] Built artifacts present in `dist/` or artifacts storage
    - [ ] Artifacts checksums generated (sha256) and recorded
    - [ ] Artifacts signed (GPG or code-signing), if required

[ ] 6. Tagging & Git
    - [ ] Annotated tag created locally: `git tag -a <tag> -m "Release <tag>"`
    - [ ] (Optional) Tag signed: `git tag -s <tag> -m "Release <tag>"`
    - [ ] Tag pushed to origin: `git push origin <tag>`

[ ] 7. GitHub Release & Assets
    - [ ] Draft GitHub Release created (or planned automation configured)
    - [ ] Release notes copied into release body
    - [ ] Built artifacts uploaded to Release or available for package publish

[ ] 8. Publishing to package registries
    - [ ] PyPI / npm / Docker credentials present and valid
    - [ ] Publish to registries executed (or scheduled by CI)
    - [ ] Publish verification completed (pip install / docker pull smoke test)

[ ] 9. Documentation & Post-release
    - [ ] Docs updated (if version-specific docs required)
    - [ ] Versioned docs built and published (if applicable)
    - [ ] CHANGELOG or release notes linked from main docs

[ ] 10. Communication & Monitoring
    - [ ] Announcement draft ready (email, Slack, Twitter, etc.)
    - [ ] Stakeholders and on-call notified of release window
    - [ ] Monitoring/alerts watched for regressions after release

[ ] 11. Rollback / Hotfix plan
    - [ ] Hotfix branch strategy decided (branch name / owner)
    - [ ] Rollback instructions noted (what to revert and how)

POST-RELEASE SMOKE TEST (perform immediately after publishing)
- [ ] Install or download the published artifact and run a quick smoke test
- [ ] Confirm basic functionality (describe expected steps)
- [ ] Verify checksums and signatures (if applicable)

NOTES / LINKS
- Links to CI runs / build artifacts / relevant issues:
```