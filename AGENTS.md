## Preferred Way of Working

### Incremental and Focused

* Use the `tldr` MCP server to understand code structure
* Make small, well-scoped changes
* One concern per change set
* Avoid cascading refactors without agreement

### Code-First Reasoning

* Inspect files before discussing them
* Do not assume abstractions or intent

### Pragmatic Testing

* Tests should defend correctness, not chase coverage
* Avoid brittle, over-specified tests

### Communication Style

* Concise, technical, professional
* Minimal narration
* Challenge assumptions and ideas - constructive dialog and pushback is expected

### Briefs

When following project briefs, any questions or additional context should be captured as instructions in the `## Approach` section once answered.

Always provide a summary of actions in an `## Output` section at the end of the brief so that the brief, the summary and the code changes can be captured in the same commit.

Always provide the output from `/cost` in a `## Cost` section at the end of the brief using the following template format

```markdown
## Cost

| Metric | Details |
| :--- | :--- |
| Total Cost | **$1.00** |
| Total Duration (API) | **2m 00s** |
| Total Code Changes | **100 lines added, 100 lines removed** |

### Usage by Model 

**claude-sonnet-4-6:**

| Type | Tokens |
| :--- | :--- |
| Input | 3.0k |
| Output | 10.0k |
| Cache Read | 1.2m |
| Cache Write | 51.9k |
```
