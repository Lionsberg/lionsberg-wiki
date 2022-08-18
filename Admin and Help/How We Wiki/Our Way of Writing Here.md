# Our Way of Writing Here

Also see: [[The "Way"]]

Here we describe the syntax / semantics / our “Way” of writing on this wiki website. ([[Why We Say Wiki Website Instead of Wiki]])

## Writing As A Team
We are trying to learn how to write as a team, and reflect both our individual and collective voices and [[Current Best Understanding]]. 

There are several elements or "parts" of the Wiki.

Each section requires a varying level of coordination, depending on how it affects other elements of Lionsberg and the Meta Project. 

Because Lionsberg is being co-created as a coherent System, words and concepts matter a lot, just like they would in a set of plans and specifications for a complex system or building. 

### Imagery

If you were to imagine a community working together to design and build something, you could imagine that every member of the community is always welcomed to speak truthfully and freely and share their own voice, perspective and experience. This can be done in sections of the Wiki that are purpose-built for this, such as the [[Membership]] pages, and [[Lionsberg Wiki Blogs]] section. These were built so that each individual can freely speak and represent their own best understanding, thoughts, suggestions, etc. 

You could also imagine that if someone changed a definition in the main body of work, or set of plans and specifications, without fully understanding the total philosophy and system architecture, it could potentially "break" the integrity of the system or confuse other co-creators. 

In order to address this, we are using a framework similar to what is used on large scale design build projects. 

### Lionsberg Wiki Blogs (aka Journals)
The [[Lionsberg Wiki Blogs]] (aka Journals) section was co-created to create the empowerment and freedom for each individual to speak freely and openly from their own perspective and point of view. In this section, we want to bring forth as much truthful diversity and perspective as possible, and our [[Current Best Understanding]] does not need to be reconciled or cohered. We can simply be free to individually think and speak as accurately as we can. 

If you would like to co-Author or edit another Author's blog, please obtain their consent and approval of any proposed changes. 

In order to preserve the integrity and values of the Lionsberg System and prevent intentional disruption, Lionsberg reserves the right to decide who can establish a blog on the main Lionsberg.Wiki site. 

### Lionsberg Wiki Books
The [[Wiki Book Template|Wiki Books]] section was co-created to empower individuals to bring forth more formalized, coherent, and persistent bodies of work. Like blogs, these books do not speak from the voice of Lionsberg as "we", and therefore do not necessarily need to reflect the collective best understanding. They can freely speak from the voice of each author. 

If you would like to co-Author or edit another Author's books, please obtain their consent and approval of any proposed changes. 

In order to preserve the integrity and values of the Lionsberg System and prevent intentional disruption, Lionsberg preserves the right to decide what books can be published on the main Lionsberg.Wiki site. 

### Lionsberg Formal Body of Work / System Design 
There is also a formal body of work that exists on the Wiki, that speaks from the voice of Lionsberg as "we", and contains things like Declarations, Core Documents, Plans and Specifications, Guides, etc. 

Like a complicated system, device, or building, each of these elements is intentionally designed and built to co-operate and interact as part of one coherent Whole. 

Because of this, the formal body of work needs to be treated with the integrity and quality control processes found on large scale design build projects. 

For now, the process is as follows: 
- Jordan is acting in the functional role of [[Architect Working Group]], and making sure that the pieces fit together properly, don't conflict, and that the entire System works in the end. This [[Architect Working Group]] needs new members dedicated to this function so that no one person becomes a bottleneck or single point of failure. 
- Everyone is acting as co-creators, and is taking responsibility for designing and building various elements of the System.
- The simple process is intended to create freedom and agency for anyone to propose any change without needing permission, while simultaneously ensuring the integrity and coherence of the Whole is maintained.
	- Any co-creator can propose an improvement to any part of the System Design at any time. The entire idea is to ensure it gets a little better every day. 
	- Proposed improvements are placed in the [[Suggestion Box]] and a message sent to the Lionsberg Wiki Posse mattermost channel. 
	- The Architect function reviews and has the responsibility to either accept and incorporate the changes, modify them, or reject if they are not compatible with the Whole. 
	- The Architect should accompany any rejection or modification with an explanation that helps improve understanding and encourages forward momentum. 

### Agency and Ease
We gratefully accept and appreciate any new information and thoughts in the form of an individual Wiki Blog or Wiki Book. Feel free to link to and cross reference to any concepts or any parts of the System you would like to discuss. 

We also gratefully accept and appreciate any new suggestions that affect core design elements or speak from the voice of Lionsberg in the [[Suggestion Box]]. 


## Questions

(See "Making Pages" below for these questions)
- When / why / how to write in an existing file?
- When / why / how to create new files?
- When and how do we use folders in this wiki?
	- Discussed on [[Wiki Posse - Lionsberg_Meta Project, 2022-05-27]] call, and on the recording
- When and how do we use tags (aka #hashtag )

## Wiki Concepts

- also see WikiWay, WikiNature
- [[Chunking]], [[Naming]], [[Linking]]

## Sociology

We'll evolve how we write together.  Some starting thoughts:

- We write in third person, and we don't generally attribute text to any one person.
- Sometimes, we need to write from a single individual's point of view; generally, if you really need to, use a self-pronoun like "my", but add your name in parentheses after, or name yourself in third person (and then someone else might and "and TheirName"). (Pete thinks principle this is a good idea.) (It's based on my (Pete) experience with Socialtext and other wikis.)

## Page Maturity

Wiki pages have a life cycle.  Pete has used tree life cycle names, with a page describing each: seed, sprout, seedling, sapling, adult, elderly, snag or rotting log.

How do we want to signal page maturity?  The tree life cycle, or something else?  Use those in tags, or in YAML frontmatter? Etc.

## Making Pages

Make the first line of each page the same as the page filename, as a level 1 header.  (So for example, the first line of this page is `# Our "Way" of Writing Here`.) This is not strictly necessary in Obsidian, but it helps some of the other clients.

Note that Obsidian won't let you use certain characters in the page filename, because it will cause problems with the filesystem. So, don't use those characters in either the page filename or the first line of the page.

Pages can be a short chapter, or a concept. Basically, a place you'd want to land on from a link. 

Conversely, pages generally shouldn't end up super short; a page should have a couple of paragraphs at least, when it gets fully developed.

It's okay to have very little in a page when it gets started, of course.

## Some Simple Markdown Rules

- Generally, use the dash character for bullet lists rather than asterisks. (Either works, but in a few cases, the dash is better for obscure reasons.)
- Similarly, you can use either underscore or asterisk for italic and bold; prefer underscore for italic, and asterisk for bold: `_italic_` and `**bold**`.
- Different editors need or don't need an empty/blank line between different kinds of elements, such as headers and bullet lists.  In general, you should use a blank line between different kinds of elements, to be most generally compatible.

## More Advanced Markdown

To make a link to a page but have different text show in the link, use a vertical bar character.  For instance, `[[Peter Kaminski|Pete]]` produces [[Peter Kaminski|Pete]].  And `[[Choice|Choices]]` makes [[Choice|Choices]].

To make it so wikitext is displayed verbatim (rather than being parsed), in a monospaced font, enclose the wikitext in a pair of backticks.

If you want multiple lines not parsed and in monospaced font, use three backticks on one line above your lines, and three backticks on the line after your lines.

(add something here about double space characters for linebreaks, used on sidebars)

## Embedding YouTube Videos

Copy the following to embed YouTube videos (but not the lines that start with three backticks), and replace YOUTUBE_VIDEO_ID with the ID of the video you want to embed:

```html
<div style="text-align:center"><iframe width="560" height="315" src="https://www.youtube.com/embed/YOUTUBE_VIDEO_ID" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
```

## Misc. Notes
- Incipient Links - links to things that don't exist yet... are just as important as a page. You can make them, without stopping your train of thought, and they will be there as placeholders. 
	- Obsidian knows a link that doesn't exist is still a link. 
	- If you click on the [[Incipient Link]], then the page exists. 
- Hashtags - #hashtag
- Over time, we need to evolve towards both the right kinds of hierarchy and linking, and have wiki gardeners develop guidance nodes, jump pages, and other tools. 
- Table of contents page, and jump page are similar. 
- [[wiki link]] = `[[wiki link]]`
- [external link to somewhere on the web](https://www.example.com/) =  `[external link to somewhere on the web](https://www.example.com/)`
- For a bare URL, use angle brackets around it, `<https://example.com/>` or `<mailto:someone@example.com>`. Without angle brackets, some wiki clients will make it a live link, and some won't.

