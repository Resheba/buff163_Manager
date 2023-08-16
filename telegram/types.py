from dataclasses import dataclass

from classes.types.item import Item


@dataclass
class MessageInfo:
    item: Item
