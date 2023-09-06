from dataclasses import dataclass


@dataclass
class Item:
    name: str
    sell_in: int
    quality: int


@dataclass
class LegendaryItem:
    name: str
    sell_in: int
    quality: int = 80


@dataclass
class AgedItem:
    name: str
    sell_in: int
    quality: int


@dataclass
class PerishableItem:
    name: str
    sell_in: int
    quality: int


@dataclass
class ConjuredItem:
    name: str
    sell_in: int
    quality: int
