# English Language Git
_AI generated in dialogue with humans. Not fully reviewed._

A plain-English explanation of git for people who want to understand what they're doing, not just memorize commands.

## The Big Picture

Git is like a time machine for your files. It lets you:
- Take snapshots of your work whenever you want
- Go back to any previous snapshot if needed
- Send copies of your snapshots to the cloud for safekeeping
- See what changed between any two snapshots

## The Three Spaces

When working with git, your files exist in three different spaces:

### 1. Your Working Directory
This is your actual files - what you see and edit in Obsidian or any text editor. This is "right now" - your current reality.

### 2. The Staging Area (also called "Index")
Think of this as a loading dock or preparation area. You put files here when you're getting ready to take a snapshot. It's like saying "these are the files I want to include in my next snapshot."

The staging area lets you be selective - you might have changed 10 files but only want to snapshot 3 of them right now.

### 3. The Repository (your local history)
This is where all your snapshots are permanently stored on your computer. Once a snapshot is here, it's safe and you can always get back to it.

## Core Actions Explained

### Stage (or "Add")
**What it means**: "I want this file in my next snapshot"

**The metaphor**: You're gathering items to photograph. You arrange them on a table (the staging area) before taking the picture.

**Command**: `git add filename` or `git add .` (for everything)

**When you do it**: After you've edited files and saved them, but before you take the snapshot

### Commit
**What it means**: "Take a snapshot right now of everything in the staging area"

**The metaphor**: Clicking the camera button. You create a permanent photograph of exactly what's on the table (staging area). This photo gets added to your album (repository) and will never change.

**Command**: `git commit -m "describe what changed"`

**What happens**:
- A snapshot is created with a unique ID
- The snapshot is stored in your local repository
- You write a message describing what this snapshot represents
- Your working directory and staging area stay exactly as they are

**Important**: A commit is LOCAL - it's only on your computer. The cloud doesn't know about it yet.

### Push
**What it means**: "Send all my local snapshots that the cloud doesn't have yet"

**The metaphor**: Uploading your photo album to cloud storage. You're synchronizing your local history with the remote backup.

**Command**: `git push`

**What happens**:
- Git looks at all commits you've made locally
- It identifies which ones the cloud repository doesn't have yet
- It uploads those commits to the cloud
- Now your local and cloud repositories are in sync

**Important**: Push ONLY uploads commits, not uncommitted changes. If you've edited files but haven't committed, those changes stay on your computer.

### Pull
**What it means**: "Get any snapshots from the cloud that I don't have yet"

**The metaphor**: Downloading updates to the photo album that others have added. You're bringing your local copy up to date with what's in the cloud.

**Command**: `git pull`

**What happens**:
- Git checks what commits exist in the cloud
- It downloads any commits you don't have locally
- It updates your working directory with the latest changes

**Important**: Always pull before starting work if others might have made changes.

## Common Workflows

### Quick Snapshot and Backup
```
1. Edit your files in Obsidian
2. Save (Cmd+S)
3. Stage everything: git add .
4. Take snapshot: git commit -m "updated chapter 3"
5. Send to cloud: git push
```

### The "Working Session" Pattern
```
Start of work:
1. Pull from cloud (get latest)

During work:
2. Edit files
3. Save frequently (Cmd+S)
4. Stage and commit whenever you complete a logical chunk
   - After finishing a section
   - After fixing a bug
   - After completing a thought

End of work:
5. Final commit if needed
6. Push everything to cloud
```

### What "Staging" Actually Means

Some people get confused by staging. Here's the deal:

**Without staging**: Every snapshot would include ALL changes to ALL files. You'd have no control.

**With staging**: You choose exactly what goes in each snapshot. This lets you:
- Commit related changes together
- Keep unrelated changes in separate commits
- Create a clear history where each commit represents one logical change

**Example**: You fixed a typo in file A and rewrote a whole section in file B. These are unrelated changes. You can:
1. Stage only file A: `git add "file A.md"`
2. Commit it: `git commit -m "fixed typo"`
3. Stage file B: `git add "file B.md"`
4. Commit it: `git commit -m "rewrote introduction"`

Now your history clearly shows two separate changes instead of one confusing mixed commit.

## The Differences

### Stage vs. Commit
- **Stage**: Preparing what goes in the snapshot (can change your mind)
- **Commit**: Actually taking the snapshot (permanent)

### Commit vs. Push
- **Commit**: Save to YOUR computer's history (local)
- **Push**: Copy to THE CLOUD's history (remote backup)

**Key insight**: You can commit 10 times locally, then push once to send all 10 commits to the cloud. Or you can push after every commit. It's up to you.

### Pull vs. Push
- **Pull**: Download FROM cloud TO you
- **Push**: Upload FROM you TO cloud

## Status Check

**Command**: `git status`

This tells you:
- What files you've changed (working directory)
- What files are staged (ready for snapshot)
- What files are not being tracked by git yet
- Whether you're ahead of or behind the cloud

Think of it as asking "what's the current state of everything?"

## Practical Advice

### How Often to Commit?

**Good rule**: Commit whenever you complete a logical unit of work that you'd want to be able to return to.

**Too often**: After every sentence (creates noise)
**Too rarely**: Once a week (can't get back to intermediate states)
**Just right**: After completing a section, fixing an issue, or finishing a coherent thought

### How Often to Push?

**Minimum**: At the end of each work session
**Better**: After each commit (if you want immediate backup)
**Best**: Whatever makes you feel your work is safely backed up

**Remember**: Committed work is safe locally. Pushed work is safe even if your computer dies.

### Writing Good Commit Messages

Bad: "updates"
Bad: "fixed stuff"
Bad: "asdfasdf"

Good: "added section on git workflows"
Good: "fixed typo in chapter 3"
Good: "restructured introduction for clarity"

**Rule of thumb**: Someone reading just your commit message should understand what changed and why.

## Common Situations

### "I edited files but haven't committed yet"
- Your changes exist only in working directory
- Not saved in git history
- A `git status` will show "modified" files
- You need to stage + commit to save a snapshot

### "I committed but haven't pushed yet"
- Your snapshot exists locally
- It's safe on your computer
- The cloud doesn't have it yet
- If you show someone the cloud version, they won't see your changes
- You need to push to back it up to the cloud

### "I want to undo my last edit"
- If you haven't committed: just re-edit the file or use Cmd+Z
- If you committed but it was wrong: make a new commit that fixes it
- Don't try to erase history - add to it

## Obsidian Git Plugin Shortcuts

The Obsidian Git plugin does these actions for you with keyboard shortcuts:

- **Cmd+L**: Pull (get latest from cloud)
- **Cmd+U**: Stage everything + Commit + Push (all in one)
- **Cmd+S**: Save the current file (not git, but important)

When you hit **Cmd+U**, behind the scenes it's doing:
1. `git add .` (stage everything)
2. `git commit -m "backup: [timestamp]"` (take snapshot)
3. `git push` (send to cloud)

## Mental Model Summary

Think of git as a three-stage process:

1. **Working Directory** = Your desk where you're actively working
2. **Staging Area** = Your outbox where you put things ready to file
3. **Repository** = Your filing cabinet where everything is permanently stored
4. **Cloud** = Your backup filing cabinet at another location

The flow is always: Desk → Outbox → Filing Cabinet → Backup

Or in git terms: Edit → Stage → Commit → Push
