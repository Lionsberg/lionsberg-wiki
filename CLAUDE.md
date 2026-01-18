# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **LIONSBERG Wiki** - a collaborative knowledge repository built using **Obsidian** with git-based version control. The wiki is a living document system designed to help co-create a vision of collective transformation and ultimately a New Civilization, containing formal documentation, books, blogs, and core statements about the LIONSBERG system and Meta Project.

The repository uses Obsidian's markdown-based wiki format with double-bracket `[[wiki links]]` for internal linking. Content is edited locally in Obsidian and committed/pushed to git frequently to maintain snapshots of work. A static website is automatically built via **Massive Wiki Builder** in CI/CD (not run locally).

## Core Architecture

### Content Structure

The wiki follows a hierarchical content organization with three distinct content modes:

1. **Individual Voice Content** (LIONSBERG Wiki Blogs and LIONSBERG Wiki Books)
   - Authors maintain full control and speak in their own voice
   - Requires explicit consent from authors before editing their content
   - Located in `LIONSBERG Wiki Blogs/` and `LIONSBERG Wiki Books/`

2. **Formal System Content** (Core Documents)
   - Speaks from the collective "we" voice of Lionsberg
   - Requires careful editing to maintain system coherence
   - Changes should be placed in the Suggestion Box with rationale
   - Located in `LIONSBERG Core Documents/`

3. **Community Content**
   - Meeting notes, correspondence, proposals
   - Located in `LIONSBERG Community Information/`

### Main Content Directories

- `LIONSBERG Wiki Books/` - Formal books by various authors (144+ books)
- `LIONSBERG Wiki Blogs/` - Individual journals and blog posts
- `LIONSBERG Core Documents/` - Mission, vision, values, declarations, and core statements
- `LIONSBERG Codex/` - System patterns and principles
- `LIONSBERG Experience/` - User experience and playbook materials
- `Admin and Help/How We Wiki/` - Wiki writing conventions and guidelines
- `Commentary/` - Commentary on core content
- `Workspaces/` - Working areas for projects

### Key Entry Points

- `README.md` - Welcome page ("The Gates of LIONSBERG")
- `LIONSBERG Wiki Books/THE NAMELESS BOOK/THE NAMELESS BOOK.md` - Primary guidebook for getting started
- `The LIONSBERG Playbook.md` - Core operational guidance
- `The Story of LIONSBERG.md` and `The Great Game of LIONSBERG.md` - Foundational narrative

## Wiki Editing Conventions

### Page Creation Standards

1. **First line must match filename** - Every page must start with `# Page Name` matching the filename exactly
2. **Use concept-based naming** - Pages represent concepts or chapters worth linking to
3. **Avoid special filesystem characters** - Obsidian restricts certain characters in filenames
4. **Pages should be substantial** - Aim for at least 2-3 paragraphs when fully developed

### Linking Conventions

- **Internal links**: Use double brackets `[[Page Name]]`
- **Link with alternate text**: Use `[[Page Name|display text]]`
- **External links**: Standard markdown `[text](url)`
- **Bare URLs**: Wrap in angle brackets `<https://example.com/>`
- **Incipient links**: Links to non-existent pages are encouraged as placeholders

### Markdown Style

- Use **dashes** for bullet lists (not asterisks)
- Use `_italic_` (underscore) and `**bold**` (asterisk)
- Always add blank lines between different element types (headers, lists, paragraphs)
- Use backticks for inline code/verbatim text
- Use triple backticks for code blocks

### Content Organization Principles

**Chunking** - Break information into appropriately-sized modular pieces (pages and headers)

**Naming** - Converge toward consistent naming for similar concepts across the wiki

**Linking** - Create rich interconnections between concepts; backlinks are automatically tracked

**Curating** - Wiki gardeners guide navigation and maintain coherence

## Git Workflow

**Git is used extensively in this repository** for maintaining current snapshots of work and pushing them to the cloud. This is the primary version control mechanism.

### Standard Workflow

1. **Pull before starting**: Fetch latest changes from remote
2. **Edit**: Make changes using Obsidian or any text editor
3. **Save**: Ensure files are saved before committing
4. **Commit frequently**: Create snapshots of your work with meaningful commit messages
5. **Push regularly**: Send snapshots to the cloud to back up work

### When Working via Obsidian Git Plugin

The **Obsidian Git** plugin provides keyboard shortcuts for git operations:

- `Cmd+L` - Pull from remote
- `Cmd+U` - Create backup and push to remote
- `Cmd+S` - Save current file (always do this before pushing)

**Best practices**:
- Pull at the start of any editing session
- Push at the end to ensure cloud has your updates
- Commit/push frequently to maintain current snapshots

### When Working via Command Line

Standard git commands work as expected:

```bash
git pull                    # Get latest changes
git add .                   # Stage changes
git commit -m "message"     # Create snapshot
git push                    # Send to cloud
```

### Git Repository

- **Remote**: `git@github.com:Lionsberg/lionsberg-wiki.git`
- **Default branch**: `main`

## Massive Wiki Builder (CI/CD Only)

**Important: Massive Wiki Builder is NOT used locally.** It runs automatically in CI/CD to build the static website. You do not need to install or run MWB when working with this repository.

The wiki is automatically built into a static website using **Massive Wiki Builder** (MWB) when changes are pushed to the repository.

### Configuration (Reference Only)

- **Config file**: `.massivewikibuilder/mwb.yaml`
- **Wiki title**: "Lionsberg Wiki"
- **Author**: "the Lionsberg Wiki Team"
- **License**: Creative Commons Attribution 4.0 International
- **Sidebar**: `Sidebar.md`

### Build Output

- **Output directory**: `.massivewikibuilder/output/` (gitignored, not created locally)

## Critical Editing Protocols

### Before Editing Core Documents

1. **Read the content carefully** - Understand the existing voice and system architecture
2. **Understand dependencies** - Core documents are designed as an integrated system
3. **Use the Suggestion Box** - Propose changes rather than directly editing
4. **Maintain coherence** - Ensure changes don't conflict with other system elements

### Before Editing Individual Content

1. **Check authorship** - Wiki Blogs and Wiki Books are author-controlled
2. **Obtain consent** - Get explicit approval before editing another author's work
3. **Preserve voice** - Maintain the author's individual perspective and style

### Writing Voice

- **Formal content**: Third person, collective "we" voice
- **Individual content**: First person, author's own voice
- **Attribution**: Generally avoid attributing text to individuals in formal docs
- **Page maturity**: Consider using lifecycle tags (seed, sprout, seedling, sapling, adult)

## Common Patterns

### Embedding YouTube Videos

```html
<div style="text-align:center"><iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
```

### Cross-References

Link liberally to related concepts using `[[wiki links]]`. The system is designed for rich interconnection of ideas.

## System Philosophy

The Lionsberg Wiki embodies several key principles:

- **Coherence**: Core content functions as integrated system design (like architectural plans)
- **Modularity**: Content is chunked into reusable, linkable pieces
- **Emergence**: Content evolves through collaborative contribution
- **Sovereignty**: Individuals maintain autonomy while contributing to the whole
- **Quality Control**: Architect function ensures system integrity (currently Jordan's role)

## Special Considerations

- **Case sensitivity**: Links are case-sensitive
- **Attachments**: Store in `_attachments/` directory
- **Obsidian vault**: This is an Obsidian vault (`.obsidian/` config directory)
- **Massive spell check**: Periodic spell checking is performed (see Pete's Journal)
- **Page maturity**: Content has lifecycle stages from seed to mature
- **LIONSBERG capitalization**: Always use "LIONSBERG" in all caps as the standard

## Troubleshooting Common Issues

### Massive Wiki Builder Not Showing Updated Pages

**Symptom**: A page exists locally and in git, but shows "coming soon" or doesn't appear on the published website.

**Common Cause**: MWB CI/CD build process may cache old file states or have case-sensitivity issues, particularly with filename changes (e.g., "lionsberg" vs "LIONSBERG").

**Workaround**:
1. Rename the file to a temporary placeholder (e.g., "The Story of LIONSBERG.md" → "The Story of X.md")
2. Commit and push the renamed file
3. Rename back to the correct filename (e.g., "The Story of X.md" → "The Story of LIONSBERG.md")
4. Commit and push again

This forces MWB to recognize it as a "new" file and regenerate the page properly.

**Prevention**: When renaming files, especially changing capitalization, be aware that the build process may need this two-step push to fully update.

### Broken Links After Renaming

**Issue**: Renaming pages can break existing wiki links throughout the repository.

**Solution**: See `Claude Code/Longterm Project - Fixing Broken Links.md` for the systematic approach to identifying and fixing broken links.
