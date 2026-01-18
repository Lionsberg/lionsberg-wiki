# Longterm Project - Fixing Broken Links
_AI generated in dialogue with humans. Not fully reviewed._

## Purpose

This is an ongoing maintenance project to identify and fix broken wiki links throughout the Lionsberg Wiki. The work will be done incrementally, a bit at a time, as part of regular wiki maintenance.

## Context

The Lionsberg Wiki contains thousands of markdown files with extensive cross-linking using Obsidian's `[[double bracket]]` link syntax. Over time, as pages are moved, renamed, or deleted, links can break. Additionally, there are "incipient links" - intentional placeholders linking to pages that don't exist yet but should.

## Project Goals

1. **Identify all broken links** - Links that point to non-existent pages
2. **Distinguish incipient links from errors** - Some broken links are intentional placeholders
3. **Fix actual broken links** - Update or remove links that are truly errors
4. **Document patterns** - Track common link issues to prevent future problems
5. **Create maintainable process** - Establish a repeatable workflow for ongoing link health

## Approach Overview

This is NOT a "fix everything at once" project. Instead, we work on it periodically:
- Fix a batch of links in one session
- Document what was done
- Return later to fix another batch
- Build up wiki link health over time

## Phase 1: Discovery & Analysis

### 1.1 Collect All Page Titles
**Goal**: Create a master list of every markdown file in the wiki

**Method**:
```bash
find . -name "*.md" -type f > all-pages.txt
```

**Output**: A text file listing every `.md` file path in the repository

### 1.2 Find All Wiki Links
**Goal**: Identify every `[[wiki link]]` used throughout the wiki

**Method**:
- Search for all double-bracket patterns: `\[\[.*?\]\]`
- Extract the link text
- Handle variants like `[[Page Name|Display Text]]`
- Create a list of unique links

**Output**: A list of all wiki links found in the content

### 1.3 Cross-Reference Links to Pages
**Goal**: Determine which links point to existing pages vs. non-existent pages

**Method**:
- Compare the list of wiki links against the list of actual files
- Account for:
  - Case sensitivity
  - Spaces in filenames
  - Links with alternate display text
  - Links in subdirectories

**Output**: Three lists:
1. **Valid links** - Point to existing pages
2. **Broken links** - Point to non-existent pages
3. **Ambiguous links** - May match multiple pages

### 1.4 Categorize Broken Links
**Goal**: Distinguish intentional incipient links from actual errors

**Method**:
- Review broken links in context
- Identify patterns (certain concepts are commonly linked but not yet created)
- Check if the linked concept appears elsewhere in the wiki
- Look for common typos or misspellings

**Output**:
- **Incipient links** (intentional) - Keep as placeholders
- **Typos/errors** (unintentional) - Fix or remove
- **Moved pages** - Update to new location
- **Deleted concepts** - Remove links

## Phase 2: Fixing Broken Links

### 2.1 Establish Priorities
Work on broken links in this order:
1. **High-traffic pages** - Core documents, main navigation
2. **Recent changes** - Links broken by recent edits
3. **Common errors** - Patterns that appear multiple times
4. **Older content** - Historical pages that need cleanup

### 2.2 Fix in Batches
For each work session:
1. Choose a batch size (10-50 broken links)
2. Review each link in context
3. Decide on action:
   - Fix typo/spelling
   - Update to correct page name
   - Create the missing page
   - Remove the link if concept is obsolete
   - Mark as intentional incipient link
4. Make the changes
5. Commit to git with descriptive message
6. Document what was done

### 2.3 Create Missing Pages (Selectively)
For incipient links that point to important concepts:
- Create a stub page with the correct filename
- Add minimal content (title, brief description)
- Mark as "stub" or "to be expanded"
- This converts broken link to valid link

## Phase 3: Documentation & Maintenance

### 3.1 Work Log
For each work session, document:
- Date of session
- Number of links reviewed
- Number of links fixed
- Common patterns discovered
- Links remaining to review
- Next priorities

### 3.2 Pattern Tracking
Keep notes on:
- Common misspellings
- Pages that were renamed (old → new mapping)
- Concepts frequently linked but not yet created
- Directories where broken links cluster

### 3.3 Prevention Strategies
Based on patterns discovered:
- Create guidelines for common page naming
- Document frequently-referenced-but-missing concepts
- Establish naming conventions for new pages
- Consider creating index pages for major topic areas

## Technical Implementation

### Automated Discovery Tools

**Find all broken links (basic approach)**:
```bash
# This is a simplified example - actual implementation needs refinement
grep -r '\[\[.*?\]\]' . --include="*.md" | \
  sort | uniq > all-links.txt
```

**Better approach using specialized tools**:
- Use Obsidian's built-in link checker
- Write a Python script to parse markdown and extract links
- Use existing markdown link-checking tools (adapt for wiki links)

### Semi-Automated Fixes

Some fixes can be automated:
- Simple typos with clear corrections
- Case inconsistencies
- Links to recently renamed files (if we track renames)

Others require human judgment:
- Ambiguous links
- Deciding whether to create missing pages
- Understanding context and intent

## Work Session Template

When working on broken links, follow this template:

### Session: [Date]

**Batch**: [Which set of links - e.g., "Core Documents", "Wiki Books", "Pages A-D"]

**Links Reviewed**: [Number]

**Actions Taken**:
- Fixed typos: [List]
- Updated renamed pages: [List]
- Removed obsolete links: [List]
- Created stub pages: [List]
- Marked as intentional incipient: [List]

**Patterns Noticed**:
- [Any common issues]

**Next Session Should Focus On**:
- [Recommendations for next batch]

**Git Commit**: [Commit hash or message]

## Important Considerations

### Don't Over-Fix
Not every broken link needs to be "fixed":
- Incipient links are a feature, not a bug
- They show where content should eventually exist
- Removing them loses valuable information about the wiki's knowledge graph

### Preserve Intent
When fixing links, understand the author's intent:
- What were they trying to link to?
- Is there an existing page that serves that purpose under a different name?
- Should a new page be created?

### Respect Content Modes
Remember the wiki's three content types:
- **Individual Voice** (Blogs/Books): Get author permission before changing their links
- **Formal System** (Core Docs): Requires careful review to maintain coherence
- **Community Content**: Generally safe to fix obvious errors

### Commit Frequently
When fixing links:
- Commit after each logical batch
- Write clear commit messages: "Fixed broken links in Core Documents - typos and renamed pages"
- This makes it easy to review or revert if needed

## Getting Started

### First Session Checklist
- [ ] Run discovery phase to understand scope
- [ ] Choose a small, manageable area to start (e.g., one directory)
- [ ] Review 10-20 broken links to get a feel for the work
- [ ] Document your process and findings
- [ ] Commit your fixes
- [ ] Update this project plan with any learnings

### Recommended Starting Points
1. **LIONSBERG Core Documents** - High priority, high visibility
2. **README.md and main navigation** - Ensure entry points work
3. **THE NAMELESS BOOK** - Key user-facing content
4. **Recent additions** - Fix links while context is fresh

## Long-Term Vision

Eventually, this work will result in:
- A healthier wiki knowledge graph
- Clear understanding of which concepts need pages created
- Established patterns and guidelines for link maintenance
- Reduced friction when navigating the wiki
- Better user experience for readers

But remember: **This is marathon work, not a sprint.** Do it bit by bit, maintain momentum, and the wiki will gradually improve.
