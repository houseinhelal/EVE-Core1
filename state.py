from dataclasses import dataclass, field

@dataclass
class SharedState:
    running: bool = False
    events_seen: int = 0
    actions_executed: int = 0
    last_action: str | None = None
    metadata: dict[str, object] = field(default_factory=dict)
