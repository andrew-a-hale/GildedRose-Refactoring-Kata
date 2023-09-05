from typing import List, Protocol
from item import Item


def increment_quality(item: Item, n: int = 1, max: int = 50) -> None:
    item.quality = min(item.quality + n, max)


def decrement_quality(item: Item, n: int = 1, min: int = 0) -> None:
    item.quality = max(item.quality - n, min)
    if item.sell_in < 0:
        item.quality = max(item.quality - n, min)


def decrement_sell_in(item: Item, n: int = 1) -> None:
    item.sell_in -= n


class ItemUpdater(Protocol):
    def update_sell_in(item: Item) -> None:
        ...

    def update_quality(item: Item) -> None:
        ...


class DefaultUpdater(ItemUpdater):
    def update_sell_in(item: Item) -> None:
        decrement_sell_in(item)

    def update_quality(item: Item) -> None:
        decrement_quality(item)


class LegendaryUpdater(DefaultUpdater):
    def update_quality(item: Item) -> None:
        pass


class AgedUpdater(DefaultUpdater):
    def update_quality(item: Item) -> None:
        increment_quality(item, 2)


class PerishableUpdater(DefaultUpdater):
    def update_quality(item: Item) -> None:
        increment_quality(item)
        if item.sell_in < 10:
            increment_quality(item)
        if item.sell_in < 5:
            increment_quality(item)
        if item.sell_in < 0:
            item.quality = 0


class ConjuredUpdater(DefaultUpdater):
    def update_quality(item: Item) -> None:
        decrement_quality(item, 2)


AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED_MANA_CAKE = "Conjured Mana Cake"
ITEM_UPDATERS = {
    AGED_BRIE: AgedUpdater,
    BACKSTAGE_PASS: PerishableUpdater,
    SULFURAS: LegendaryUpdater,
    CONJURED_MANA_CAKE: ConjuredUpdater,
}


def update_quality(items: List[Item]):
    for item in items:
        update_quality_single(item)


def update_quality_single(item: Item):
    item_updater = ITEM_UPDATERS.get(item.name, DefaultUpdater)
    item_updater.update_sell_in(item)
    item_updater.update_quality(item)
