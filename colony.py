from __future__ import annotations
from collections.abc import Iterable
from .events import Event
from .neural_bus import NeuralBus
from .state import SharedState

class Colony:
    def __init__(self, bus: NeuralBus, state: SharedState, zooids: Iterable[object]) -> None:
        self.bus = bus
        self.state = state
        self.zooids = list(zooids)
        self.bus.subscribe_all(self._count_event)

    def _count_event(self, event: Event) -> None:
        self.state.events_seen += 1

    def start(self) -> None:
        self.state.running = True
        self.bus.publish(Event("colony.started", "colony"))

    def stop(self) -> None:
        self.bus.publish(Event("colony.stopped", "colony"))
        self.state.running = False
