from enum import Enum

class ItemType(Enum):
    default = 0
    legendary = 1
    aged = 2
    perishable = 3
    conjured = 4

class Item:
    def __init__(self, name: str, type: ItemType, sell_in: int, quality: int):
        self.name = name
        self.type = type
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s, %s" % (self.name, self.type, self.sell_in, self.quality)