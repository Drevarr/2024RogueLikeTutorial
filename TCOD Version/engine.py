from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console


from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler


class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        """Initialize the engine with a list of entities, an event handler, and a player entity"""
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player

    def handle_events(self, events: Iterable[Any]) -> None:
        """pass the events to it so it can iterate through them, and it uses self.event_handler to handle the events"""
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)

    def render(self, console: Console, context: Context) -> None:
        """This handles drawing our screen. We iterate through the self.entities and print them to their proper locations, then present the context, and clear the console"""
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()