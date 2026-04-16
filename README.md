# Claude Code Extensions

Custom skills, commands, and agents for Claude Code.

## Structure

```
.claude/
  commands/       # Slash commands (*.md files)
agents/           # Agent configurations
skills/           # Custom skills
```

## Usage

### Commands

Place `.md` files in `.claude/commands/`. Each file becomes a slash command.

Example: `.claude/commands/review.md` creates the `/review` command.

### Skills

Skills extend Claude's capabilities with specialized knowledge and workflows.

To install skills, symlink the `skills/` directory:

```bash
ln -s /path/to/this/repo/skills ~/.claude/skills
```

#### Available Skills

- **crawl4ai** - Web crawler that converts URLs to clean markdown for LLM consumption
- **execute-plan** - Execute a written implementation plan with dependency analysis and verification
- **handover** - Consolidate multi-step context into an executable handover document for coding agents, external tool agents, or human operators

### Agents

Agent configurations for specialized task handling.
