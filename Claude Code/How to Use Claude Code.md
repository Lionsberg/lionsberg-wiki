# How to Use Claude Code
_AI generated in dialogue with humans. Not fully reviewed._
## Core Philosophy

**Have Claude Code do everything except provide the instructions.** You provide the vision and direction; Claude Code executes the work.

Treat Claude Code as an intelligent co-worker, not a tool to micromanage. Tell it what you want accomplished, have it explain how it would approach it, review together, and then let it implement.

## Documentation is Everything

**Document absolutely everything** - this creates project legibility and ensures continuity:

- What you're currently working on
- What you're thinking about working on next
- Your plans and strategies
- How plans have changed and why
- How the work process went
- Decisions made and reasoning
- Work logs and progress updates

This documentation should live in your workspace as markdown files, not in Claude's private space. These files become the project memory and allow you (and Claude) to maintain context across sessions.

## Working with Claude Code in Terminal Mode

### Basic Workflow

1. **Give clear instructions** about what you want accomplished
2. **Ask Claude to explain** how it would approach the task
3. **Have Claude write a plan document** in your workspace
4. **Review the plan together** - make edits in Obsidian or give feedback
5. **Iterate until satisfied** - "here's what you got wrong, update it and let's review again"
6. **Authorize implementation** - "implement this, and make sure you keep a work log"

### Key Commands and Features

- **@ symbol** - Brings up the file picker to reference specific files
- **Accept Edits** - Generally leave "Accept Edits On" for smoother workflow
- **Git integration** - Claude can use git to commit and push work snapshots

### Plan Mode vs. Direct Work

**Plan Mode**: Claude can think and talk but cannot do any work. It's a "bolt" that prevents execution while allowing planning and discussion.

**Direct Work Mode**: Claude can both plan and execute.

**Note**: Some experienced users (like Pete) never use plan mode - they prefer to just have Claude work directly while documenting plans as it goes.

## Project Management Best Practices

### Maintain Project Legibility

- Keep all plans, decisions, and work logs as files in your workspace
- Use clear naming conventions for documentation files
- Create a project journal or log that tracks daily/weekly progress
- Document "why" decisions were made, not just "what" was done

### Effective Collaboration Patterns

**Instead of**: "Change line 42 to use a different variable name"
**Do this**: "The variable naming in this function isn't clear. Review it and propose better names that follow our conventions."

**Instead of**: "Add error handling here, here, and here"
**Do this**: "This module needs better error handling. Analyze where errors could occur and implement comprehensive error handling with our standard patterns."

### Iteration Cycle

1. **Request** - Describe what you want
2. **Proposal** - Claude writes a plan/approach document
3. **Review** - You review in Obsidian, make notes
4. **Refine** - Give feedback, Claude updates the plan
5. **Implement** - Once aligned, Claude executes with work log
6. **Document** - Capture outcomes, learnings, next steps

## Integration with This Wiki

When working in the Lionsberg Wiki specifically:

- Respect the three content modes (Individual Voice, Formal System, Community)
- Follow the wiki editing conventions (first line = filename, double-bracket links, etc.)
- Use git frequently to maintain snapshots
- Document your work process in a dedicated workspace or journal
- Reference the CLAUDE.md file for repository-specific guidance

## Tips for Success

1. **Start conversations with context** - Reference relevant files with @
2. **Be explicit about what you want documented** - "Create a work log as you go"
3. **Save important context in files** - Don't rely on conversation memory alone
4. **Use git commits strategically** - Commit after completing logical chunks of work
5. **Review Claude's work** - You're the architect, Claude is the builder
6. **Iterate freely** - It's easy to refine and improve; don't aim for perfection on first pass
7. **Keep a project journal** - Track what you're learning and how the project is evolving

## Common Patterns

### Starting a New Feature
```
"I want to add [feature description]. First, create a plan document called
'[feature-name]-plan.md' that outlines how you would approach this.
Include considerations for [specific concerns]. Don't implement yet."
```

### Reviewing and Refining
```
"I've reviewed the plan in Obsidian and added comments. Read the updated
file and let's discuss the changes before moving forward."
```

### Implementation
```
"The plan looks good. Implement it and maintain a work log in
'[feature-name]-worklog.md' as you go. Commit to git after each
major step."
```

### Reflection and Documentation
```
"Now that [feature] is complete, create a summary document that captures:
- What we built and why
- Key decisions and tradeoffs
- What we learned
- Next steps or future considerations"
```

## Terminal Mode Specific Notes

Since you're using Claude Code in terminal mode (CLI):

- All file edits will be shown with diffs for you to review
- You can accept/reject edits interactively
- Git operations happen through the terminal commands
- The @ file picker helps navigate your repository quickly
- You can background long-running operations
- Claude maintains session context but files preserve it across sessions

## Know Your Model

**Keep track of which Claude model you're using.** Different models have different capabilities, speeds, and costs.

### The Models

- **Sonnet** - Balanced performance and speed. Good for most tasks.
- **Opus** - Most capable and intelligent. Best for complex reasoning and difficult tasks.
- **Haiku** - Fastest and most cost-effective. Good for simple, straightforward tasks.

### Why This Matters

**Cost management**: Opus costs significantly more than Sonnet, which costs more than Haiku. Using Opus for simple tasks wastes money.

**Quality expectations**: If you're getting unexpectedly simple responses, you might be on Haiku. If you need deeper reasoning, switch to Sonnet or Opus.

**Work documentation**: Note which model you used for different tasks. This helps you understand which model works best for which types of work.

### Checking Your Model

Claude Code will typically tell you which model is active. You can also ask: "What model are you?"

### Best Practices

- **Use Haiku for**: Simple edits, straightforward documentation, basic refactoring
- **Use Sonnet for**: Most coding tasks, planning, complex edits, general work
- **Use Opus for**: Architectural decisions, complex problem-solving, difficult debugging

**Document which model you're using** in your work logs, especially when comparing results or troubleshooting quality issues.

## Getting Started Checklist

- [ ] Read the CLAUDE.md in this repository for project-specific guidance
- [ ] Set up a workspace folder for plans, logs, and working documents
- [ ] Establish a naming convention for your documentation files
- [ ] Create an initial project journal or work log
- [ ] Practice the request → proposal → review → implement cycle
- [ ] Commit frequently to git to maintain snapshots
- [ ] Keep "Accept Edits On" unless you need fine-grained control
- [ ] Check which model you're using and choose appropriately for the task
