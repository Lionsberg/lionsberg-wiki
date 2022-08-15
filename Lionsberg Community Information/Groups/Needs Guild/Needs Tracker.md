# Needs Tracker
### why needs?

Most of us do not know what need is driving our emotions. This makes it all too easy for us to react to our emotional state with strategies that don't fulfill our needs. The need remains unfilled, the emotions remain, mysterious, haunting, implacable.

The idea here, though, is to get really good at identifiying needs, personal needs, project needs, community needs. How? At first, by looking for them deep below unpleasant emotions. One method involves studying [a typical needs list](https://www.cnvc.org/training/resource/needs-inventory) and finding those that best describe you in the moment. Then you think of a strategy for fulfilling that need. Imagine that eventually all of us get really good at identifying needs and at satisfying them.

As a project team or as a community, describing and fulfilling needs is what the following is about.

### project lifetime

Throughout the lifetime of building anything, needs arise and are fulfilled. A need is something missing. It has a description and a condition of satisfaction. By amassing all the needs of a project, anyone can quickly come to understand its thrust and status.

### owner

A need has two owners: the **spokesperson** and the **fulfillment team**. Anyone or any team can select a need, promising to fulfill it. A need can be worked on in a variety of ways. It can be assessed for (and committed according to) time and broken down into sub-needs, resources, and milestones. Progress, designs, decisions, and other activities can be reported within a need. Each of these will be date stamped, including duration.  

### tasks

The team signs a promise to fulfill the need. The team works out the actions and work details which fulfill the need. Agile tasks are included.

### maturity

When a need is fulfilled, it becomes part of the current state of play. The need is then displayed as a completed component, with a description of how it is to be used. This allows the project to retain an audit trail from initial needs to final documentation. The tags and dependencies created along the way are retained, and can be expanded to account for ongoing improvements, and newly emerging needs.  

### search

Search strings let users locate needs by matching them against description. **Tags** (aka categories) can be added to needs, as many as are deemed appropriate. These tags are used by the search facility to shrink the number of matches shown and presented for this purpose in a multiple-choice list. Tags are managed separately, made available when creating a need, and can be easily expanded with a need-new-tag function. The importance (payoff, urgency or priority) of each need is another searchable facet. It’s a rough estimate of how much value will accrue from fulfilling the need. Other search parameters can be easily added as we desire. Some **tags** that come to mind:  

- infrastructure
- prototype
- research
- resource
- medium
- trouble
- design
- small
- test
- big  

### dependencies

Dependencies between needs can be presented as a graph, like a mind map. Owned needs will also show a duration and due date, which will be summed over owned sub-needs.

Another approach to dependencies is an outline view where subordinate needs can be optionally made invisible. Any single need can be viewed in isolation (containing needs can be optionally made invisible). Needs can be reordered or moved about or edited. Completed needs can be optionally made invisible.

### accountability

The fulfiller of a need promises to satisfy the conditions expressed by the stakeholder, specifying a timeframe. Agile philosophy allows surprises to arise and be dealt with, mitigating surprises and avoiding catastrophes. Stakeholders should to be informed about and involved in dealing with these surprises. This ripples out into and through all dependent needs.  

The usual harsh judgement which accompanies surprises is not as useful as analyzing the causes of those surprises. Unclear conditions of satisfaction, inadequate planning or communication, mismatch of owner’s skillset. Careful integration of such analysis back into the process of needs management will help us grow our overall team strength.  

Ranking the performance of the fulfiller in terms of quality, timeliness, communication, and perhaps other things can help the owner improve and help future stakeholders of other needs decline or accept an offer. However, we want to avoid blacklisting and to promote second chances. Perhaps when an owner receives a low ranking, they can cite it and add a declaration of intent to improve, indicating awareness and desire.

### stakeholder

The person who authors a need is its stakeholder and recipient. Alternatively, the author can submit the need on behalf of someone else, and that other person is the stakeholder. Any negotiations, requests for information, assessment of completion and of the owner’s accountability are to be directed to / performed by the stakeholder.

Let’s say that the effort of meeting the conditions of satisfaction are discovered to be impractical. The stakeholder can choose to cancel the need or restate its conditions of satisfaction.

Doing this kind of back and forth with care and vigor allows us to be agile without sacrificing reliability and accountability. Perhaps the mechanism is a combination of email and chat room, both of which are recorded in the need.

### creating a new need

The minimum requirement for a new need is title and stakeholder. I personally prefer to add new needs directly into the dependency graph. Why? For one, this eliminates the high friction of filling out an unfamiliar and potentially lengthy form.

The rest can be filled in or updated at any time in a form or a separate view. The stakeholder is usually the person creating the need, so that is the default and can be changed at any time.

### database

Four tables (and their schemas) come to mind:

- needs (id, description, conditions of satisfaction, date created, stakeholder, fulfillment team, rough delivery date, subordinate need ids, tag ids)
- users (id, name, email, phone number, rating/reliability/accountability)
- reports (id, need id, description, type, reporter id, date, duration)
- tags (id, description, title)    

### examples

Some (obvious?) first needs:  

- needs tracker website
- state of play (synopsis) board
- simple onboarding content and presentation
- assessment of current technologies
- road map
- knowledge base (tutorials, documentation, how to guides)

### user interface

At minimum, six views will give us a lot, perhaps delivered in the following order:

1. chat room for stakeholder and fulfillment team
2. create a new need (a plus button above the list of needs)
3. dependency graph / outline
4. search (filter) and view existing needs
5. state of play (synopsis) board
6. road map (time graph)

As for item 1 ... Autogenerate needs on the fly during chat. We could incorporate a way to add needs from a chat. (:need: as a keyword to auto create a new need with a title and stakeholder) into a holding area from which they can be cherry picked

As for item 2 ... The minimum requirement for a new need is title and stakeholder. I personally prefer to add new needs directly into the dependency graph. Why? For one, this eliminates the high friction of filling out an unfamiliar and potentially lengthy form. The rest can be filled in or updated at any time in a form or a separate view. The stakeholder is usually the person creating the need, so that is the default and can be changed at any time.

### needs clearinghouse

All of us working together to operationalize the [[Meta Project]] are gradually meeting people and learning from them, collaborating with them. Some of us, however have ideas that have stalled for lack of something (guidance, funding, knowledge, skill). For such folks, would it make sense to provide a repository of personal needs?

The synopsis board can present has been recently accomplished across all the actively pursued needs?

### possible existing tools

- [Nolt](https://nolt.io/) 
	- I hate the name. minimum $25 / month. It deals with dependencies very poorly and consequently no hierarchy graph. I cannot recommend it!
	- <a data-nolt="button" href="https://meta-project.nolt.io">Click here to try a Meta Project Nolt entry form</a><script async src="https://cdn.nolt.io/widgets.js"></script>

[[Current meta work on needs]]  

