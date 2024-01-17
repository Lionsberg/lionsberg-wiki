# Git Branch Naming

## Main Branch

We prefer "main" for the main branch.  For background, see:

- [Regarding Git and Branch Naming \- Software Freedom Conservancy](https://sfconservancy.org/news/2020/jun/23/gitbranchname/)
- [github/renaming: Guidance for changing the default branch name for GitHub repositories](https://github.com/github/renaming/)
- [The default branch for newly\-created repositories is now main \| GitHub Changelog](https://github.blog/changelog/2020-10-01-the-default-branch-for-newly-created-repositories-is-now-main/)

## Branching Models

- [GitFlow](https://nvie.com/posts/a-successful-git-branching-model/)
- [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow)

We currently use this structure; we use "work branches" (similar to "feature" branches) to make proposed changes, and they get merged by someone else to main.

- main
	- work branches

### Branch Naming

We typically name work branches with three components:

- identifier of the lead on the changes (usually, two or three initials)
- short name of the gist of the work (keep it very short, e.g., 10 characters)
- date in YYYYMMDD format

Examples:

- jrs-traction-2022-07-19
- pk-expanding-system-design-2022-07-19
