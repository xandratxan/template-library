# Publishing a Release on GitHub

This document explains what a "release" is, why you create releases, the general process and governance around them, and provides concrete, step-by-step instructions for publishing a release on GitHub manually, with the GitHub CLI, and automatically using GitHub Actions. It also lists common post-release tasks and useful tips.

## What is a release (and why create one)?

A release is a snapshot of your project at a specific point in time. It typically corresponds to a tagged commit and may include:
- Release notes / changelog that summarize user-visible changes.
- Built artifacts (wheels, tarballs, binaries, Docker images, installers).
- Metadata such as release name, tag, and (optionally) release assets uploaded to GitHub.

Releases are important because they provide reproducible, discoverable versions for users and downstream automation (CI, package indexes, OS distributions). They also provide a canonical place to record what changed and why.

Typical goals of a release process:
- Provide clear versioning (e.g., Semantic Versioning: MAJOR.MINOR.PATCH).
- Ensure tests and quality gates pass before publishing.
- Produce and publish artifacts reliably and securely.
- Record a changelog and release notes for users.

## High-level workflow (general explanation)

1. Development: work happens on branches (feature branches, main/develop, release branches).
2. Prepare: when ready, update the version, changelog, and ensure the test suite & linters pass.
3. Create a tag: create an annotated Git tag that marks the release commit.
4. Build artifacts: build wheels, tarballs, or other distributables.
5. Publish artifacts: upload to package registries (PyPI, npm, Docker Hub) or attach to the GitHub Release.
6. Announce & post-release tasks: update documentation, notify users, create releases notes, and close milestones.

This workflow can be executed manually or automated (recommended for consistent, repeatable releases).

## Pre-release checklist (what to verify before publishing)

- Tests: unit & integration tests pass in CI for the release commit.
- Version: the repository version is bumped (in code/packaging metadata) and matches the tag to be created.
- Changelog/Release notes: entries are prepared and reviewed.
- CI pipeline: artifact build & signing (if applicable) succeeds.
- Commit hygiene: the release commit has the intended contents, no secrets, and license files are in place.
- Access: whoever publishes has the required GitHub permissions and (if relevant) package registry credentials.

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

## Manual release (Git + GitHub web UI)

1. Make sure your working tree is clean and you've pushed the release commit to the remote main branch:

   git add .
   git commit -m "Bump version to vX.Y.Z"  # or your normal flow
   git push origin main

2. Create an annotated tag locally and push it:

   git tag -a vX.Y.Z -m "Release vX.Y.Z\n\nShort summary or link to CHANGELOG" 
   git push origin vX.Y.Z

   - Use annotated tags (not lightweight) because they store tagger, date, and a message.

3. Create the GitHub Release (web UI):
   - Go to the repository on GitHub → "Releases" → "Draft a new release".
   - Select the tag `vX.Y.Z` (you can create it from here if you didn't push it locally).
   - Fill in the release title and body (release notes). Prefer referencing the relevant CHANGELOG entry.
   - Optionally attach built artifacts (wheel, tar.gz, binary) by drag-and-drop.
   - Mark as "Pre-release" if it's not a full stable release.
   - Publish the release.

4. Post-release: verify assets are downloadable, update documentation and any downstream registries if needed.

## Release using GitHub CLI (gh)

The GitHub CLI (`gh`) makes scripted releases easy. Example:

   # Create and push a tag and draft a release using gh
   git tag -a vX.Y.Z -m "Release vX.Y.Z"
   git push origin vX.Y.Z

   # Create a draft release from the pushed tag
   gh release create vX.Y.Z --title "vX.Y.Z" --notes-file CHANGELOG.md --draft

   # To publish immediately instead of draft:
   gh release create vX.Y.Z --title "vX.Y.Z" --notes-file CHANGELOG.md

To upload release assets:

   gh release upload vX.Y.Z dist/*.whl dist/*.tar.gz

Note: authenticate `gh auth login` beforehand and ensure it has repo scope.

## Automated releases with GitHub Actions

Automation is recommended for consistency. Typical approach:

- Create a workflow that triggers on push of a tag (e.g., `push` with `tags: ['v*']`) or on creation of a GitHub Release.
- The workflow runs tests, builds artifacts, and then uses actions to create or complete the GitHub Release and upload assets.
- Optionally, the workflow can publish to PyPI or Docker Hub (use secrets for credentials).

Example minimal workflow (conceptual):

```yaml
name: Release
on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install deps
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest -q
      - name: Build
        run: python -m build
      - name: Create GitHub Release and upload assets
        uses: softprops/action-gh-release@v1
        with:
          files: 'dist/*'
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - name: Publish to PyPI
        if: success() && needs.publish.outputs.should_publish == 'true'
        run: twine upload dist/* -u __token__ -p ${{ secrets.PYPI_API_TOKEN }}
```

This example uses `softprops/action-gh-release` to create a release from the tag and upload the built files. Adjust to your build and publish steps.

Security note: use GitHub secrets (not hardcoded tokens) to store credentials. Prefer short-lived tokens or the built-in `GITHUB_TOKEN` for repository-scoped actions.

## Signing and verification

- For higher confidence, sign release artifacts (GPG or code signing certificates). For Python packages, consider signing distributions or using PyPI's recommended practices.
- Git tags can be GPG-signed (`git tag -s vX.Y.Z -m "..."`) and GitHub will display the verified signature on the tag/release.

## Release types and strategies

- Semantic Versioning: use MAJOR.MINOR.PATCH to communicate compatibility guarantees.
- Canary / pre-release: use pre-release tags like `v1.2.0-rc.1` or GitHub's "Pre-release" checkbox for release candidates.
- Release branches: some teams maintain a `release/*` branch for staging releases or long-term-support branches.

## Rollback and hotfixes

- If a release has a critical bug, create a hotfix branch from the tag (or branching point), fix, bump patch version, and create a new release (e.g., `v1.2.1`).
- Do NOT rewrite tags that have been published to shared remotes (avoid `git push --force` on tags). If you absolutely must remove a tag, delete it locally and remotely and create a new annotated tag with a new version.

## Post-release checklist

- Verify published artifacts and checksums.
- Update docs (for example, release notes, API docs, and versioned docs on ReadTheDocs or GitHub Pages).
- Notify stakeholders and update project boards/milestones.
- Monitor error reporting and roll out hotfixes if needed.

## Example commands quick reference

```bash
# Create an annotated tag and push it
git tag -a v1.2.0 -m "Release v1.2.0"
git push origin v1.2.0

# Create a draft release with gh and upload assets
gh release create v1.2.0 --title "v1.2.0" --notes-file CHANGELOG.md --draft
gh release upload v1.2.0 dist/*.whl

# Create a signed tag (GPG) and push
git tag -s v1.2.0 -m "Release v1.2.0"
git push origin v1.2.0
```

## Tips and best practices

- Automate builds & tests; require a green pipeline before release.
- Keep a clear, user-facing changelog (e.g., maintain a `CHANGELOG.md` and automate entries when possible).
- Use annotated tags and, if applicable, GPG-signed tags.
- Prefer small, frequent releases rather than large infrequent ones.
- Use draft releases for final verification before publishing.
- Store and rotate credentials securely; restrict tokens to least privilege.

## Further reading

- GitHub Releases documentation: https://docs.github.com/en/repositories/releasing-projects-on-github
- Semantic Versioning: https://semver.org/
- Git tagging docs: https://git-scm.com/docs/git-tag
- GitHub Actions: https://docs.github.com/en/actions
