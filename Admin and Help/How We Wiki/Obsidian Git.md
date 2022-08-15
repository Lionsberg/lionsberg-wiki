# Obsidian Git
On July 8, 2022, we transitioned the Lionsberg Wiki to Git. 

## Some common commands

- Command + L - pull from the cloud
	- Command name for setting hotkey: `Obsidian Git: Pull`
- Command + U - push back to the cloud
	- Command name for setting hotkey: `Obsidian Git: Create backup with specific message`
	- Recommendation - If you've been editing a file, before you Push, press Command + S to make sure that the current page is saved. If you type something and immediately hit Push, the push may miss the most recent edits.

## Best practices

### Pull at the start of editing session, Push at the end

Pull (Cmd+L) at the start of any editing session with the wiki, just to make sure you and the cloud are in right relationship before you start making changes.

We don't think you need to do a Cmd+L before every Cmd+U, that is built into Obsidian Git. Just Cmd+L once when you start, if it's been a while since your last Pull.

End your session with Cmd+U, to make sure the cloud gets all your updates.

## Obsidian Git Suggested Settings

- **Show changes files count in status bar** = on