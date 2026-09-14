from .core.colony import Colony
from .core.neural_bus import NeuralBus
from .core.state import SharedState
from .zooids.action import ActionZooid
from .zooids.critic import CriticZooid
from .zooids.memory import MemoryZooid
from .zooids.perception import PerceptionZooid
from .zooids.reasoning import ReasoningZooid

def build_colony(db_path: str = "data/eve.db"):
    bus = NeuralBus()
    state = SharedState()
    memory = MemoryZooid(bus, db_path)
    perception = PerceptionZooid(bus)
    reasoning = ReasoningZooid(bus)
    critic = CriticZooid(bus)
    action = ActionZooid(bus, state)
    colony = Colony(bus, state, [memory, perception, reasoning, critic, action])
    return colony, perception, memory

def main() -> None:
    colony, perception, memory = build_colony()
    colony.start()
    print("EVE-Core v0.1 | type 'exit' to stop")
    try:
        while True:
            text = input("> ")
            if text.strip().lower() in {"exit", "quit"}:
                break
            perception.observe(text)
            print(f"EVE baseline action: {colony.state.last_action}")
    finally:
        colony.stop()
        memory.close()

if __name__ == "__main__":
    main()
