# Copy-Edit Pass — Observations and Fixes Log

_Full pass completed February 28, 2026. All chapters (0-14) of The Book of LIONSBERG reviewed file by file._

---

## Summary

| Batch | Chapters | Files Read | Fixes Made |
|---|---|---|---|
| A | Introduction + Ch.1 Genesis | 44 | 84 |
| B | Ch.2 + Ch.3 + Ch.4 | 70 | 47 |
| C | Ch.5 + Ch.6 | 51 | ~35 |
| D | Ch.7 + Ch.8 | 101 | 111 |
| E | Ch.9 + Ch.10 | 94 | 63 |
| F | Ch.11 | 85 | ~45 |
| G | Ch.12 + Ch.13 + Ch.14 | 62 | 70 |
| **Total** | **All (0-14)** | **~507** | **~455** |

### Most Common Error Types

1. **Missing words** (~100 instances) — prepositions, articles, conjunctions, verbs ("to," "the," "of," "is," "are," "that")
2. **Doubled words** (~60 instances) — "the the," "we we," "a a," "of of," "towards towards," "force force"
3. **Misspellings** (~80 instances) — "lightening/lightning," "perrennially," "cacophany," "beleagured," "instituions," "exitations," "nucelotides," "Enlightenemnt," "orthdoxy," "viscous/vicious"
4. **Wrong words** (~50 instances) — "where/were," "then/than," "your/you," "every/ever," "principle/principal," "plain/plane," "It's/Its" (possessive)
5. **Extra spaces and NBSP characters** (~30 instances) — especially before wiki links
6. **Broken wiki links** (~15 instances) — spaces inside brackets, missing brackets, single brackets where double needed
7. **Subject-verb agreement** (~15 instances)
8. **Wrong verb forms** (~10 instances) — "becomes/become," "mistook/mistaken," "chose/choose"

---

## Structural Observations (Not Fixed — Require Decision)

### Filename Issues

1. **`8.55 The Enlightenemnt.md`** — "Enlightenemnt" misspelled in filename. All wiki links reference the misspelled version. Requires simultaneous rename + link update.
2. **`8.47 The Prophesy Of Muhammad.md`** — "Prophesy" is the verb form; noun is "Prophecy." Filename change would require link updates.
3. **Duplicate section numbers:**
   - Two files numbered 8.9: "Revisiting The Outer Reaches Of Memory" and "Not So Simple"
   - Two files numbered 8.x4: "Who Can Pass Through The Gate?" and "What Can Pass Through The Gate"
   - Two files numbered 12.18: "Fairy Tales and Myths Are More Than Real" and "Hell Is Real, And We Can Co-Create It For Our Selves"
4. **"8.x" numbered files** (8.x1 through 8.x4) — draft/placeholder sections without final section numbers
5. **Heading mismatches** — Several files had `# Untitled` as their H1 heading instead of matching the filename. These were fixed during the pass: 7.18, 8.55, 8.56.

### Stub / Placeholder Sections

1. **Chapter 4**: Files 4.20, 4.21, 4.22, 4.23 contain only "Coming soon - skip ahead"
2. **Chapter 7**: Middle sections (7.20-7.40 range) are notably thinner than surrounding content
3. **Chapter 8**: Files 8.55 and 8.56 contain only "Coming Soon." File 8.53 has `[[Left Off Here]]` marker. File 8.65 also has `[[Left Off Here]]`. File 8.x4 "What Can Pass Through The Gate" is essentially empty.
4. **Chapter 12**: File 12.16 ends with "(More to come)." Files 12.15, 12.18 (Fairy Tales) lack navigation footers.
5. **Chapter 14**: Entire chapter is only 4 sections / ~2,200 words. Ends with "Temporarily The End."

### Non-Breaking Space (NBSP) Characters

Multiple files contained UTF-8 NBSP characters (0xC2A0) that appear as invisible double spaces. Fixed in individual instances, but a **global search-and-replace of NBSP characters across the entire repository** would catch any remaining ones. This appears to be caused by the Obsidian editor or copy-paste operations.

### Single-Bracket vs. Double-Bracket Links

Several files use single brackets `[term]` where double brackets `[[term]]` (wiki links) appear to be intended. These were NOT fixed because they could be intentional. Flagged locations:  
- 2.5 line ~: `[Reality]`
- 3.20 line 34: `[One] [Loves]`
- 7.8 line 79: `[Dark Matter]` and `[Dark Energy]`
- 7.10 line 82: `[Way]`
- 7.35 line 25: `[One] [Source]`
- 8.59 line 7: `[Living System]`

### Possessive "Its" vs. Contraction "It's"

The text consistently uses "It's" (contraction) where "Its" (possessive) is needed when referring to ONE/God/Spirit. Fixed where clearly wrong, but this pattern recurs throughout and may warrant a global audit. Key locations fixed: 4.24, 12.1, 13.26.

### Inconsistent Formatting Patterns

1. **Ellipsis styles**: Inconsistent use of `...` (three dots), `…` (unicode ellipsis), and `....` (four dots) throughout
2. **Prayer/liturgical sections**: Inconsistent italic formatting in prayer passages (e.g., 13.20 lines 67-82)
3. **Numbered list formatting**: Some sections use unusual spacing before numbered items (e.g., 12.4)

---

## Suggested Changes (Requiring Author Decision)

### Word Choice Questions

1. **3.8**: "What is partnered with" — should this be "What if partnered with"? (surrounding sentences are "What if..." questions)
2. **3.21**: Pronoun shift — "Her Potential... Yet she is bound by chains that **it** cannot break free from alone." Should "it" be "she"?
3. **4.24**: "Prophesy" — verb form used as noun. Change to "Prophecy"?
4. **4.29**: "you have mistook" — standard is "you have mistaken," but "mistook" has archaic/poetic force. Intentional?
5. **12.2**: "sulking in the shadows" — should this be "skulking" (prowling stealthily)?
6. **13.9**: "There are no Predecessors to beginning to act" — ✅ RESOLVED: "Predecessors" is the correct term. It is a technical term from Integrated Program Delivery (IPD) and the AEC industry, describing task sequencing in complex programs. Its use here is intentional — applying the IPD concept fractally to convey that no task must come first before you begin the Quest.
7. **13.25**: "These vile, overt, and openly stated demand" — should "demand" be "demands" (plural)?
8. **14.3**: "but who the knowing that makes us a self today is" — intentionally paradoxical construction, or garbled?

### Structural Suggestions

1. **Chapter 7 TOC in The Book of LIONSBERG.md** — Sections 7.24-7.33 were listed twice (duplicate removed in this session's TOC fix)
2. **Chapter 8 "8.9" duplication** — Two different files share section number 8.9. One should be renumbered.
3. **Chapter 12 "12.18" duplication** — Two different files share section number 12.18. One should be renumbered.
4. **Chapter 8 "8.x" files** — Need final section numbers assigned
5. **Missing navigation footers** — Several files in Chapters 12 lack forward/back navigation links at the bottom

---

## Chapter-by-Chapter Notes

### Chapter 0 - Introduction (8 files)
Clean. Minimal errors found.

### Chapter 1 - Genesis (36 files)
Moderate error density. Most errors were misspellings and missing/extra words. The Caves section (1.5) was notably clean — appears to have been carefully edited previously.

### Chapter 2 - The Quest to Perceive (10 files)
Low error density. A few broken wiki links in 2.9 and 2.10.

### Chapter 3 - The Meta Quest (26 files)
Moderate error density. Several doubled words and misspellings. The "Spiraling Up or Down" section had duplicated word "towards."

### Chapter 4 - The Quest to Navigate (34 files)
Higher error density, particularly in 4.24 (The Reciprocal Opening of Being and Doing) which had multiple broken wiki links with spaces inside brackets. Several stub sections (4.20-4.23).

### Chapter 5 - Quest for Purpose and Meaning (23 files)
Low-moderate error density. Standard typo/missing word fixes.

### Chapter 6 - The Quest of the Creative One (28 files)
Low-moderate error density. The Song of Creation (6.4) was clean. Some misspellings in the philosophical sections.

### Chapter 7 - The Quest of the Living System (36 files)
High error density — the scientific/technical content had the most typos. File 7.10 (What Is Fundamental?) had 8 errors alone. File 7.18 (Elementary Subatomic Matter) had a heading that didn't match the filename and multiple typos including "exitations" (5 occurrences). Non-breaking space characters found in multiple files.

### Chapter 8 - The Quest of Humanity (65 files)
High error density. Multiple NBSP characters. Several files with "Coming Soon" stubs. Two misspelled filenames. The historical survey sections (8.42 Rise of Rome, 8.45 Jesus, 8.47 Muhammad, 8.52 Another Millennia) had notable error concentrations, likely due to rapid writing of factual content.

### Chapter 9 - The Quest for Sovereignty (53 files)
Moderate error density. About 63 fixes across 53 files. Doubled words and missing prepositions were the dominant error types.

### Chapter 10 - The Quest for Unity (41 files)
Low-moderate error density. Standard fixes.

### Chapter 11 - The Meta Game (85 files)
Moderate error density across the largest chapter. About 45 fixes across 85 files.

### Chapter 12 - The Anti-Quest (20 files)
Moderate error density. Possessive "Its" vs. contraction "It's" confusion was particularly common. Two files share section number 12.18.

### Chapter 13 - The Quest of the Heroes (38 files)
High error density — 47 fixes across 38 files. The confession/prayer sections (13.19-13.20) had the most errors, suggesting rapid emotional writing. File 13.25 had notable issues with verb forms and agreement.

### Chapter 14 - The Art and Science of the Way (4 files)
Low error density (only 3 fixes) but the chapter is very short (4 files, ~2,200 words). Marked as "Temporarily The End."

---

_This log covers the original Chapters 0-14. The Great Game (Ch.15), Playbook (Ch.16), and Program Delivery Guide (Ch.17) were written and edited in separate sessions._
