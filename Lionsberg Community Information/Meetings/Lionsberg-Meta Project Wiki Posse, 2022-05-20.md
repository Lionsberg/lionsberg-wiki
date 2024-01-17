# Lionsberg-Meta Project Wiki Posse, 2022-05-20

## History
- Jordan and Pete have done a bunch of work to go through why Wiki, why Massive Wiki, why tools...
- Pete and Bill have gone through a bunch of work to know we probably want to use Obsidian and SyncThing?

## Concerns

- access and authorization
- practical accessibility for different kinds of people
- not forcing people to use Massive Wiki, even though they can easily utilize the components and contribute to a Massive Wiki in other ways

## Primary Goals (for this meeting)

- 1. Have a Wiki: Start a Lionsberg | Meta Project wiki website with a primary goal to gather a set of documents / “The Way” / the plans and specifications with the hope that it would help provide context and clarity for everyone.
- 2. Know how to use wiki: Make sure Jordan can write on the wiki.
- 3. Document how others can comment and collaborate.
    - This may be something like how a diverse group of specialists collaborates on a set of plans and specifications on a building project. 
    - Roles, access structures, authorizations, etc.
    - How to tie these written words out to the other visualizations etc.  
- 4. Make sure anyone on the web can read the wiki.

## Secondary Goals (as best currently understood)

- Create a project charter for the Wiki Posse
- Find / rewrite "why Massive Wiki"?

## Skills
- Write in Markdown... 
- Structured Writing
- Use [[Double Brackets]] instead of [Single Brackets] Jordan has been using...
- Develop a [[Semantics]] of [[How We Write]]... 
    - and compare/contrast [[How We Write]] and [[Wiki Languaging]]
    - as an example of a semantic "language" or semantic patterning, [[C2]]-style wikis use [[Short Noun Phrases]].
- Develop a [[Syntax]] of how we write... 
- a [[set of important words]]] that is like [[semantic language]] - and how we tie these various standards together in a way we can make sense of... 
- How to take [[Semantic Content]] into some kind of mathematical langauge like (maybe) [[TLA+]] 
- How to take [[TLA+]] into code.

## Tech Infrastructure

- Obsidian, a PKM and also a good Massive Wiki client
- HackMD, a collaborative Markdown editor
- Syncthing, a way to keep multiple people's copies of a wiki in sync
    - Sits on both places, ensures that changes happen in all places... 
    - Why this vs. something like Box / Google Drive... 
        - Syncthing is open source... 
        - Difference of architecture... used to have centralized architecture, Massive Wiki is inside out... everyone gets a copy of wiki on their own computer... decenetrlaization, privacy, redundancy... Everyone has own copy, and GIT or syncthing keeps them up to date... 
        - And things we have to deal with to realize those benefits...
        - Could centralize with Box etc... 
        - Because we want to be open source and P2P... it is literally that way... 
        - Decentralization, sovereigns, etc. 
        - LOCKSS - Lots of Copies Keep Stuff Safe
    - Syncthing across trusted allies... one or more gatekeeper who can manage GIT... 
    - For Lionsberg | Meta Project
        - Might be forks... different authorization domains... 
        - Lots of similar copies of same original starting place... with lots of clones / forks... that can be back-folded into original... 
        - Each clone has different authorization domain... 
        - We have one trusted place... keep adding that to that... 
        - Then a gatekeeper... can run GIT... 
            - Gatekeeper Responsibilities
                - be part of the Syncthing cloud
                - make regular (at least daily) archival copies to a safe, versioned repository
                    - With GIT - to GitHub or CSC Git host
        - GIT is very careful when making copies... have to have a login... public can read not write... GIT makes a snapshot of every change... 
        - GIT - protocol for exchangign files with safety, authorization, and versioning... 
        - to centralize that use something like GitHub... 
        - Mulitiple teams doing fork and pull... different teams with different access control... 
        - Experience - GIT not very rewarding... not much benefit... 
        - A joy to be interlinking text changes, with fine grained control... the satisfaction of a team sport... what you are doing, how everyone operates, passing the ball effortlessly, infrastructural skills melt away and be in collaboration... GIT and GITHUB do that... 

- Syncthing 2
    - Click icon on top bar. opens browser. 
    - Placing of sync'd files on computer so you can find them. 
    - Install syncthing... give Pete Code that says who my computer is... Pete plugs back in devide ID... and away we go... 

- Git
- GitHub
- Massive Wiki Builder, converts a Massive Wiki into a static website
- `*.gardens.wiki`, the CSC wiki farm
    - e.g., peterkaminski.gardens.wiki
    - metaproject.gardens.wiki
    - mp-wiki-posse.gardens.wiki
    - mp-sandbox.gardens.wiki
- What creates the overview and knowing what to find where? 

## Other Stuff

- expressing structure in a mathematical language like [[TLA+]]

## Notes
- Obsidian calls them Vaults... Git calls them Repos... 
- You can look at it as a file and folder structure... 
    - Just files and folders on your computer... it is files and folders, so it works like files and folders... 
    - Right click, show in system explorer. 
    - Can open with different kinds of editors... Typora, etc. 
    - Typora doesn't understand wikilinks... but understands markdown 
- Obsidian - settings... 
    - appearance... light mode. settings saved per vault on your computer. 
    - Core Plugins
        - Keyboard search
        - Backlinks
    - Plugins
        - Some good / some not
        - Collapse All
        - 
- Where is Lionsberg | Meta Project stored... 
    - Was originally going to be wiki.lionsberg.org
    - Preacing sovereigns, decentralization, federation, multiple service providers for core stuff...
    - So realized that we need lots of wikis... 
    - and one startpage that points to - the various amazing wikis... some people, some sovereigns, etc. will end up with different focuses, sets of rules etc.
- Standardized way to use comments - to add comments... hypothesis... wiki maintainer comes along and sweeps into the wiki... 
- 




