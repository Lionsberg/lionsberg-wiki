# Wiki Posse, 2022-07-15

## Topics

- Goal: agree on process and tools for optimizing both creativity and content moderation in Lionsberg Wiki
- This was a good pattern, and we'd like to reflect on it, share it, refine it

## Agenda

- orient
- [[#Issue What Happened|what happened?]]  
- [[#Proposed Technical Solution|proposed technical solution]]  
    - technical implications
    - social implications
- reflect on the continuous improvement pattern we performed this time, and document for sharing

not included - see below at concerns

## Next Steps

- Jonathan and Pete to work on technical parts of branching, merging, etc. (also ask Bill)
- Pete and Jonathan split wiki into two repos (but still one website?)
- Jonathan to lead on writing skeleton of core-space training, Wendy E to help with ignorance based learning framing and connection to social dimensions and onboarding
- Pete to report out about Wiki Posse meeting
- core-system is currently Jordan pouring content from elsewhere into a collaborative container, so we can start to work on it together
    - we'll develop a ratification process to move core-system into community-ratified core
- work on a way to promote direction loosely eg metaphor - to share with the community - as a live container

### Deployment

separate subdomains,

- lionsberg.wiki - just "getting started" and a table of contents
- core.lionsberg.wiki
- community.lionsberg.wiki

or, integrate into one website, lionsberg.wiki (probably better)


## Issue / What Happened

- This dialogue is flowing from the tension between fostering creativity and agency, and content that has architect's intent / can "break" parts of the integrity if changed.
- Jordan used very carefully constructed language 
- Jonathan edited some core areas
- Jordan asked for a conversation with Jonathan
- J+J talked about separating freeform-creative and core-system
    - how do we foster flow and agency (freeform)
    - how do we ensure a more refined touch (core-system)
- suggestion:
    - two sections of the wiki
        - freeform (blogs, personal content)
        - core-system (needs architectural review)
    - Suggestion Box
- J+J posted to Wiki Posse channel
- Spirit and Pete chimed in
- Pete suggested a zoom call (and included a rough technical suggestion)
- We had a meeting (You Are Here / “You're soaking in it!” :-) )

### Concerns

- I want to make sure everyone feels involved in developing core-system
- I want to make sure that we help contributors feel like their gift of editing the wiki is accepted and that we love them
    - default to assume that a gift is valuable, rather than not valuable
    - a gift can be perceived as _wrong_, but that inspires correction or acceptance of continuing uncertainty
    - information only exists if there is difference - a different alternative 
        - where identity is personal - who I am v who you are
        - where difference is what one thing is not exactly the same (infer shades of grey not black and white, agree completely v completement disagreement)
        - difference within identity versus 
        - identity within difference

### Proposed Technical Solution

- we want the "avenue forward" to be obvious to anyone who is trained as follows:
- two_ wikis?
    - core-system, worked on (by anyone), but more carefully
        - discussion to decide what "careful" means
        - more documentation of what "careful" means
        - more training of what "careful" means
        - "careful" may depend on more sophisticated tooling (with attendant training)
        - "careful" may start off with structure, but evolve more to experience and trust
        - Jordan is the current authority on "careful"
            - this is a bottleneck until we have a regularly scheduled training class
    - freeform, more emergent
    - will end up with inter-wiki linking challenges and opportunities

- guide / coach people to support learners
- [[Careful Editing of the Core]]  
- core-system uses Git branches and GitHub issues

- sometimes merging is easy (automatic even) and sometimes it can be messy (even if everyone agrees what the end state generally should be)
- learning curve for people who want to participate
- personal energy - emotion - for people staying in the exchange that resolves the messy to accepted
- need to decide about merging rules
- switching branches: how to do, how Obsidian reacts

#### Sub-issues

- words on how to ask a question without offence being triggered
- using the principle of ignorance based learning - knowledge design and barriers and assistance to social / thinking / language solutions so we have clean entry to the problem space before we enter the solution space
    - unclear words
    - lacking data
    - ambiguous and that is useful
    - don't have a way to know
    - emotional or cultural blocker to getting the entry right
- "Suggestion Box" vs. proposing wording -> more alive within core content
- Issue / consideration is that we are editing live, and people may be reading and making decisions / implementing
- more like Google Docs / HackMD

## Git / GitHub Affordances

- branching (good inside communities)
    - look at GitFlow (as an example, we probably don't need full GitFlow)
    - how do we see the "live rendering" of a branch?
- fork and pull (i.e., pull requests) (good for external contributors)
- GitHub Issues (including commenting)

branch is very much like a fork, but can be merged back with less rigamarole

## RFIS / Submittals?
- on design build projects - this is resolved partially via
    - 1. RFIs
    - 2. Submittals
    - 3. Issue Logs

### Observations

- we all have something to give
- we all need to feel involved
- we need not to have too much process - might weigh down the contributions
- Parallel system to technical one - to help hold people through the changes - guide / coach. 
- Ability for things to move in both directions... 

## Similar Patterns Are Happening In Larger Meta Project Ecosystem

- Similar agency / feedback issue with concern of "speaking into the void" and not getting response. 
- Or speaking concerns and having them not adequately addressed
- Simultaneous  patterns may be more social in nature and relate to projects or preserving the relationships between people in Meta Project
- What we do / learn here might apply (or not) elsewhere

### Observations

- There is a process / culture needed around understanding which "side" things fit on... 
- How we move back and forth between sides - how we determine when things are "ready" to migrate from floating side to architecture side 
- There is valuable learnings to be found in where something fits 
- Quickly arriving at bounded rationality... to get something we can iterate on and negotiate
- Some areas need rough approximate guard rails, some areas need precision

## Keywords / Concepts

- Suggestion Box, Architect's Intent, Creativity, Vigilant Editing Team, etc.
- stages, processes, visible and invisible
    - knowledge design 
    - known knowns, unknown knowns, known unknowns, unknown unknowns
- elephants
- worldview
    - errors / mistakes are information
- double and triple diamond (every divergence has it's roots in convergence)
- US Constitution vs. Congressional Record

## Previous Comments from Mattermost

### Jordan from Mattermost, 2022-07-11

https://chat.collectivesensecommons.org/agora/pl/fy3bwrxgzjd4fyb7yua9cg1roa

Jonathan and I did some work on reorganizing and architecting and creating differentiated work flows to ensure that individuals are empowered to speak freely from their own voices on any topic in the Wiki Blogs or Wiki Books sections, while protecting the integrity of the Whole / System Design and its definitions. We noticed that if I had written comprehensively and in an interlinked manner on something, and then someone else changed a page that defined that [Word Tool] in a slightly different way, it could damage the coherence and integrity of the Whole. 

So we differentiated out a Community Information Section (people, groups, projects, meetings, notes)… 

A Wiki Blogs section…

A Wiki Books section…

And a Lionsberg System Design section… 

We defined a proposed system similar to what is used on complex systems and projects where proposed changes or improvements to the content of the System Design section are placed into a [[Suggestion Box]], where then the function akin to Architect can review and accept, modify, or reject with an explanation. I can handle that Architect function for a period of time as we get up to speed, but we will quickly need to assign that function to a team that is passionate about it and good at it and really understands the design of the entire System. 

### Jonathan from Mattermost, 2022-07-11

https://chat.collectivesensecommons.org/agora/pl/zctafrrqxpg6dfagiyxmfmtjkc

Reflections on my meeting with @jnicholasone. It's great to spend time with someone i respect.

i've digested the process he outlined and have some concerns. I agree wholeheartedly that cohesiveness and consistency must be ensured. This is serious business. We are talking about billions of dollars, so I get that we need to be credible and the opposite of a mish-mash.

At risk of oversimplifying it, I'd like to frame this as being about operationalizing our creativity, in spirit with the meta project. I have a concern that this process may stifle creativity by adding extra steps for the author and for the architect function and multiple copies of the same material. We are all good thinkers here, so I have two questions for us. Do we think our creative activities should be smooth, light and simple, so we can focus massively on being creative? Do we think our creativity can and should be nurtured, coached, guided, and ultimately set free to collaborate as a whole?

So, I wonder about adding a **vigilant editing team** watching all pushed changes and editing them as needed. With each edit, they offer a conference with, or a message to, the author (nurturing guidance). Would this be less overall effort for greater overall benefit? @peterkaminski Can github help? We could use pull requests, but would that also mean we would not be able to see the changes live, or too complicated/ridiculous if we have a staging site?

### Spirit from Mattermost, 2022-07-11

For me, this challenge is broken down into 3 components…

1. There is enough work to do right now that a lot of regimented coordination and structure is really not necessary as it’s more important something of the 90% unfinished work gets completed than being concerned in what order or in what way. But organizing some kind of coherent roadmap is necessary so people know what they can work on and begin self-locating in a coherent way.

2. That being said, it will be very helpful if some of the individuals in the collective are motivated to take on the role of “synergy organizer” (or some better name). The role will essentially be people who love coming in behind work that’s been done and brushing it up, editing, making it smooth, filling in the gaps, finishing the last little bits, connecting it to other relevant pieces (eg backlinks, front links, unlinked references, unlinked aliases), etc…

3. If there are those who are inspired to take on this role, they will explicitly/directly or implicitly/indirectly “teach” others how to work in a more “tidy” manner as well. Not that everyone has to be an expert at this skill. Small improvements over time make a big difference. And I hope all our gifts rub off on each other over time to help each of us collectively enhance our abilities and expand our consciousness. 

Also, there will be some who simply don’t work in a “tidy” manner at all because it is not in the nature of their gift(s) to do so. If only a small percentage (10ish%) of people work in a relatively “untidy” manner,  that’s fine. No need to be concerned about that if there are “synergy organizers” and the rest (90ish%) more or less do work in a “tidy” manner. 

In any “real/living” system, I think we always have to accept there will be 10ish% outliers who simply don’t comply with the standards of that system. The goal is to integrate their gifts and for the other 90% to be efficient enough to make up for that loss rather than try to compel each other to change core parts of ourself (of course with the exception of extreme violations, etc)…

### Pete from Mattermost, 2022-07-12

https://chat.collectivesensecommons.org/agora/pl/w1amk4srttyhufi76gbc4j76oo

My sense is that we're looking at:

- multiple wikis, probably with different stewarding circles
    - figuring out how inter-linking wikis might be made as practical as possible
- git- or github-style collaboration (perhaps branches, but maybe fork/pull) rather than Suggestion Box