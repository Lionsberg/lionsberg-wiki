# Testing Git Branching

This folder has pages related to some work on Git branching, for future use for parts of Lionsberg Wiki.

Check with [[Jonathan Sand]] or [[Peter Kaminski]] for more details.

To see the Obsidian debug console: **Cmd+Option+I**

## Creating branch

```
git checkout -b pk-first-branch-test-2022-07-19
git push --set-upstream origin pk-first-branch-test-2022-07-19
```

(or, there's `git switch`)

## If upstream branch is not set and you try to push with Obsidian Git:

```
'null': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'
```

```
git obsidian error: Did not push. No upstream-branch is set!
```
