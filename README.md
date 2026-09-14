# EVE-Core

**EVE-Core v0.1 — Minimal Colony**

EVE is an experimental persistent digital colony inspired by the siphonophore: specialized **Zooids** coordinate through a typed Neural Bus, shared state, memory, goals, criticism, and governed action.

> **No module is EVE. EVE is the governed interaction of the colony over time.**

EVE does not claim consciousness, sentience, or human emotion. Internal states are engineering mechanisms and must have measurable causal effects on behavior.

## v0.1 goals
- Small, understandable colony.
- Typed event communication.
- Persistent event memory with SQLite.
- Explicit Critic gate before action.
- Replayable/observable behavior.
- No self-modification or uncontrolled external action.

## Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python -m eve.main
pytest
```

## Structure
```text
eve/core/       colony, event model, neural bus, shared state
eve/zooids/     perception, memory, reasoning, critic, action
docs/           architecture, principles, safety
tests/          baseline tests
data/           runtime SQLite database (ignored)
```

Next milestone: **v0.2 — richer environment + measurable adaptive internal state**.
