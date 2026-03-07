# Coding Buddy

A terminal-based AI coding agent. Pair program from the command line with an LLM that can read files, run commands, and edit your code.

## Features

- Interactive REPL or single-prompt mode
- File reading, editing, and shell command execution
- Streaming responses with syntax-highlighted output
- Per-session memory and context management
- AGENTS.md support for per-project instructions
- Works with any OpenAI-compatible API (OpenRouter by default)

## Installation

```bash
git clone https://github.com/Yussefayman/coding-buddy
cd coding-buddy
pip install .
```

Set your API key:

```bash
cp .env.example .env
# add your API_KEY and BASE_URL to .env
```

## Usage

```bash
# Interactive mode
coding-buddy

# Single prompt
coding-buddy "explain this codebase"
```

## Architecture

![Coding Buddy Architecture](artifacts/Coding%20Buddy%20Archtecture.png)

## Dependencies

| Package | Purpose |
|---|---|
| `click` | CLI interface |
| `rich` | Terminal UI rendering |
| `openai` | LLM API client |
| `pydantic` | Tool schema validation |
| `tiktoken` | Token counting |
| `httpx` | Async HTTP |
