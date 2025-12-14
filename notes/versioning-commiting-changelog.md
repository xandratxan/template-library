# How to automatically generate a changelog between tags

For most modern projects, the best approach is to:

1. Enforce a Commit Convention (like Conventional Commits).
2. Use a Dedicated Tool (like auto-changelog or conventional-changelog-cli) to generate the formatted Markdown file automatically.
3. Integrate with CI/CD or your hosting platform (GitHub/GitLab) to run the generation step when a new tag is pushed.

Which tool are you leaning towards, or which Git hosting platform are you using? I can provide a more specific example command!

I want to keep it simple. The only thing I know is that I want to use GitHub Releases.


That is a perfect starting point! If you are using **GitHub for releases**, you can use the simplest and most integrated method available, which requires **no extra tools or custom scripting**.

This method relies on GitHub's built-in **Automatic Release Notes Generation**.

### 🚀 The Simplest Approach: GitHub Automatic Release Notes

GitHub can automatically look at the commits and Pull Requests (PRs) between your new tag and the previous release tag, and generate a clean summary for you.

#### **How to Do It:**

1.  **Navigate to Releases:** Go to your repository on GitHub and click on the **"Releases"** tab.
2.  **Click "Draft a new release":** (Usually on the right side).
3.  **Choose the Tag:**
    * In the **"Choose a tag"** field, type the name of your new version tag (e.g., `v1.2.0`). GitHub will offer to create this new tag when you publish the release.
4.  **Use the Magic Button:**
    * Click the **"Generate release notes"** button.

#### **What GitHub Does Automatically:**

GitHub will instantly scan the Git history between the tag you just entered (e.g., `v1.2.0`) and the last official release tag (e.g., `v1.1.0`).

It will generate notes structured into the following sections:

* **✨ What's Changed:** A list of all merged Pull Requests (PRs) since the last release, usually linking to the PR title.
* **📚 New Contributors:** A list of GitHub users who contributed for the first time.
* **Full Changelog:** A link to the raw Git diff between the two tags.

### 💡 Next Level: Using Commit Conventions to Make it Cleaner

While the method above works with **any** commit history, it works even better if you use basic conventions in your **Pull Request titles** (or commit messages, if you use squash/merge).

For instance, if you use a title like:

* `feat: Add user profile endpoint`
* `fix: Correct form validation bug`
* `docs: Update installation guide`

GitHub's automatically generated list of changes will be much clearer for your users.

### ✅ Recommendation

Start by using the **"Generate release notes"** button on GitHub. It's the simplest, zero-setup way to get an automatic changelog between tags.

Would you like to try generating release notes for one of your existing tags?

Once GitHub Generate release notes, can I review and edit them?

Yes, absolutely! The best part about using GitHub's **Automatic Release Notes Generation** is that it provides a great *starting point* that you can easily review, customize, and edit before you publish it.

### Review and Edit Workflow

When you click the **"Generate release notes"** button on the "Draft a new release" page, GitHub populates the main **"Describe this release"** text box with the Markdown content.

Here's how the process works and what you can do:

1.  **Automatic Generation:** GitHub analyzes the commits/PRs between the selected tags and fills the description field.
2.  **Review and Edit:** You can now treat this auto-generated text like any other markdown content you'd manually write.
    * **Add Highlights:** Write a brief, user-friendly summary paragraph at the top to highlight the most important changes (e.g., "This is a major release with a new dark mode!").
    * **Filter/Tweak:** Delete irrelevant entries (like internal maintenance PRs that GitHub's filter might have missed).
    * **Reorganize:** Move PRs under custom headers you create (e.g., separating "Bug Fixes" from "New Features").
    * **Format:** Add bolding or emojis to draw attention to key items.
3.  **Save as Draft:** If you are not ready to publish, click **"Save draft."** The drafted release, along with your edited notes, will be saved and visible only to those with repository access. You can return and edit the draft as many times as you like.
4.  **Publish:** Once you are satisfied with the notes and have attached any necessary assets (like binary files), click **"Publish release."**

### Advanced Customization

For teams that want more control over the *initial* generated notes (before manual editing), you can use a configuration file:

* **The `.github/release.yml` File:** You can create this file in your repository to tell GitHub exactly how to categorize changes.
    * You define **custom categories** (e.g., "Breaking Changes," "Performance Improvements").
    * You map these categories to **Pull Request labels** (e.g., any PR with the label `bug` goes under the "Bug Fixes" category).
    * You can also explicitly **exclude** PRs based on labels (e.g., exclude `skip-changelog` or `dependencies`) or by author (e.g., exclude bot accounts).

This configuration helps ensure the automated notes are nearly perfect before you even start your manual review.

The process of managing releases on GitHub is shown in this video.
[AUTOMATED Release Notes - GitHub Checkout](https://www.youtube.com/watch?v=88FWrfHCIqo) is a video that demonstrates the automatic release note generation feature on GitHub.

http://googleusercontent.com/youtube_content/0

# Does python recommend something specific about commit conventions?

That's a very specific and insightful question!

Unlike its strong recommendations for code style (like PEP 8), **Python does not have an official, universally-adopted PEP that mandates a specific *commit* convention** (like Conventional Commits).

However, the Python community, particularly the largest scientific libraries and the Python Software Foundation (PSF), has adopted a few **de facto standards** and highly-recommended practices:

### 1. 🐍 Python's De Facto Standard: The NumPy/SciPy Convention

The most prominent and influential commit convention in the Python world comes from the large scientific computing stack (NumPy, SciPy, pandas, Matplotlib). This convention is characterized by its capitalized prefixes:

* **Structure:** They prefix the subject line with an all-caps tag followed by a colon.
* **Purpose:** This allows release managers to quickly scan the history and determine which changes are user-facing (e.g., features and fixes) and which are internal (maintenance and testing).

| Prefix | Intent/Category |
| :--- | :--- |
| **`ENH:`** | **Enhancement/New Feature** |
| **`FIX:`** | **Bug Fix** |
| **`MAINT:`** | Maintenance, refactoring, build system changes. |
| **`DOC:`** | Documentation changes. |
| **`TST:`** | New or updated tests. |

### 2. General Community Consensus (Based on Git Best Practices)

Most Python projects, including core Python development itself, adhere to the fundamental best practices inherited from the broader Git community:

* **Imperative Mood:** The commit message should be in the imperative mood. (e.g., "**Fix** bug," not "Fixed bug" or "Fixes bug").
* **Concise Subject:** The subject line should be a brief summary of the change.
* **Detailed Body:** Use the commit body to explain *why* the change was made and any relevant context (e.g., linking to the GitHub issue or PR).

### 3. Conventional Commits Adoption

While it wasn't born in the Python community, **Conventional Commits** (e.g., `feat:`, `fix:`) is gaining popularity in newer and smaller Python projects, primarily because the tooling for automated versioning and changelog generation is so robust. It offers the same benefits as the NumPy style but with a larger, cross-language ecosystem of tools.

---

### **Summary**

| Standard | Status in Python | Use Case |
| :--- | :--- | :--- |
| **NumPy/SciPy Tags** | **De Facto Standard** | Recommended for large, mature libraries, especially scientific ones. |
| **Basic Git Best Practices** | **Universal** | Required for all projects (imperative mood, clear subject/body). |
| **Conventional Commits** | **Growing Adoption** | Recommended for projects prioritizing automation, particularly with tools like `semantic-release`. |

If you are working on a project that relies on the NumPy stack, the NumPy-style convention is the most contextual choice. For a brand-new, general-purpose library focused on automation, Conventional Commits is often the easiest path.

# Does python recommend something specific about versioning?

Yes, while Python doesn't enforce versioning via a PEP in the way it does code style (PEP 8), it **strongly recommends** a well-known, external standard: **Semantic Versioning (SemVer)**.

This recommendation is the **de facto standard** used by virtually all significant Python packages, including those on PyPI (the Python Package Index).

---

### 1. 🥇 Semantic Versioning (SemVer)

Python projects recommend following the SemVer 2.0.0 specification. It defines a standard three-part version number:

$$\text{MAJOR}.\text{MINOR}.\text{PATCH}$$

* **MAJOR Version (X.y.z):** Incremented for **incompatible API changes**. This is a breaking change that requires users to modify their code.
    * *Example:* Going from `1.5.0` to `2.0.0`.
* **MINOR Version (x.Y.z):** Incremented for **new, backward-compatible functionality**. You can add features without breaking existing code.
    * *Example:* Going from `1.5.0` to `1.6.0`.
* **PATCH Version (x.y.Z):** Incremented for **backward-compatible bug fixes**.
    * *Example:* Going from `1.5.0` to `1.5.1`.

### 2. PEP 440: The Python-Specific Standard

While SemVer defines the *meaning* of the numbers, **PEP 440** (Version Identification and Dependency Specification) defines the **formal syntax** that Python tools (like `pip` and package builders) use to parse and compare version strings.

PEP 440 is essential because it standardizes how Python handles:

* **Pre-releases:** Using suffixes like `.aN` (alpha), `.bN` (beta), or `.rcN` (release candidate).
    * *Example:* `1.0a1` (alpha 1), `1.0b3` (beta 3).
* **Post-releases:** Used for distribution fixes without changing the underlying code.
    * *Example:* `1.0.1.post1`.
* **Development Releases:** Versions currently under development.
    * *Example:* `1.0.dev0`.
* **Epochs:** A mechanism for correcting versioning mistakes in older packages (rarely used in modern projects).
    * *Example:* `1!1.0.0`.

**Key Takeaway:** Any version string published to PyPI **must** be PEP 440 compliant, and it is highly recommended to follow the SemVer meaning behind the numbers.

### 3. Tooling and Automation

To manage versioning effectively, the Python community often uses tools that integrate versioning with the Git history:

* **`setuptools_scm`:** A package that automatically derives the project's version string from Git tags and commit metadata, ensuring consistency between your Git history and the packaged version.
* **Conventional Commits / `semantic-release`:** When combined with a Conventional Commit workflow, tools like `python-semantic-release` can completely automate the version bumping process based on your `feat:` and `fix:` commits.

In short, the standard is: **Follow SemVer for the philosophy, and ensure your version strings adhere to PEP 440 for technical compliance.**