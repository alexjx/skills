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

This repository uses the layout expected by the `skills` CLI:

```
skills/<name>/SKILL.md
```

List the available skills with:

```bash
npx skills add https://github.com/alexjx/skills/tree/main/skills --list
```

Install all skills with:

```bash
npx skills add https://github.com/alexjx/skills/tree/main/skills --skill '*' -y
```

Install one skill with:

```bash
npx skills add https://github.com/alexjx/skills/tree/main/skills --skill commit -y
```

Use a skill without installing it:

```bash
npx skills use https://github.com/alexjx/skills/tree/main/skills --skill commit
```

The bundled installer wraps the same local source path:

```bash
./install.sh
```

Pass any `skills add` options after the script name, for example:

```bash
./install.sh --agent codex --skill commit -y
```

For local development, use `./skills` in place of the HTTPS URL so generated
agent state under `.agents/` or `.claude/` is not rediscovered as source content.

#### Available Skills

- **agent-harness** - Orchestrate multi-session work with persistent state tracking
- **commit** - Create atomic commits with conventional commit formatting
- **execute-plan** - Execute a written implementation plan with dependency analysis and verification
- **handover** - Consolidate multi-step context into an executable handover document for coding agents, external tool agents, or human operators

### Agents

Agent configurations for specialized task handling.
