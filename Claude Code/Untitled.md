# Claude Code 201

Encouragement From Pete February 2026: 

btw, if you're starting to use Claude more, you should explore "skills", they're super powerful.

here's an email i sent to OGM about moving a description of yourself by ChatGPT into Claude. that particular task isn't important to you, but skills in general will be. use this email as a way to start learning about skills, is all.

I haven't A/B tested ChatGPT vs. Claude memories and conversation recall too much, but I'm guessing you'll find that while ChatGPT's memories about you form more automatically, Claude's are less automatic, but a lot more powerful if you work the system a little.

Now for the next part of moving into Claude: getting the profile from ChatGPT, enhanced by a conversation with Claude, into Claude more systemically. I think just having a conversation won't affect other conversations much.

Step 1, turn on the appropriate settings in Claude.

Settings -> Capabilities -> Memory -> Search and reference chats -> On (note that the docs say you can fuzzy-ask Claude to remember something from past chats, but I get the impression it might not do it automatically the way ChatGPT does,

Settings -> Capabilities -> Memory -> Generate memory from chat history -> On,

Settings -> Capabilities -> Generate memory from chat history -> Memory from your chats (you can try editing this, but I'm not sure I would, see the discussion of Skills below),

Step 2, build a "Think with Name" skill

Settings -> Capabilities -> Skills -> Example skills -> skill-creator -> On,

After ensuring "skill-creator" is enabled, click the three-dot menu and then "Try in chat".

In the resulting chat, here's what I used as a prompt:

Hey Claude—can you make something amazing with my "skill-creator" skill? I want a skill that tells Claude how their user thinks, and how to work with them best. I've attached a profile.

I attached the profile of me (actually two profiles from ChatGPT edited together), and then Claude built a skill for me.

I downloaded the skill, then went back to:

Settings -> Capabilities -> Skills -> Your skills,

And uploaded my new skill, then tried it. BTW, I haven't used skills too much. I have my new "Think with Pete" skill enabled, and part of the skill says when to apply it, but I don't know how proactive Claude will be with it. You can always say "use the think with pete skill" though, to invoke it.

Now, imagine the kinds of skills you can create (or find on the web) -- write an agent, draft an email, use this writing style, use that writing style, set up a meeting agenda, help me summarize a transcript with all the tricks, etc., etc. You can just create, upload, and iterate on the ones you want.

Also to remember, this isn't even Claude Code yet!

(P.S. Another way to use the profile about you would be to add it to a project, but I think the above would be generally more useful.)

References to review

"Using Claude’s chat search and memory to build on previous context | Claude Help Center"(https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context)

"Understanding Claude's Personalization Features | Claude Help Center"(https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)

"search for 'skills' in Claude docs"
https://support.claude.com/en/?q=skills