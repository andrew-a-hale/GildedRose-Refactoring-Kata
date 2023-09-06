from typing import List
import items

Item = (
    items.LegendaryItem
    | items.AgedItem
    | items.ConjuredItem
    | items.PerishableItem
    | items.Item
)


def increment_quality(item: Item, n: int = 1, max: int = 50) -> None:
    item.quality = min(max, item.quality + n)


def decrement_quality(item: Item, n: int = 1, min: int = 0) -> None:
    item.quality = max(min, item.quality - n)
    if item.sell_in < 0:
        item.quality = max(min, item.quality - n)


def decrement_sell_in(item: Item, n: int = 1):
    item.sell_in -= n


def legendary_item_updater(item: Item):
    pass


def aged_item_updater(item: Item):
    decrement_sell_in(item)
    increment_quality(item)
    if item.sell_in < 10:
        increment_quality(item)
    if item.sell_in < 5:
        increment_quality(item)


def perishable_item_updater(item: Item):
    decrement_sell_in(item)
    increment_quality(item)
    if item.sell_in < 10:
        increment_quality(item)
    if item.sell_in < 5:
        increment_quality(item)
    if item.sell_in < 0:
        item.quality = 0


def conjured_item_updater(item: Item):
    decrement_sell_in(item)
    decrement_quality(item, 2)


def default_item_updater(item: Item):
    decrement_sell_in(item)
    decrement_quality(item)


def update_quality_single(item: Item) -> None:
    match type(item):
        case items.LegendaryItem:
            legendary_item_updater(item)
        case items.AgedItem:
            aged_item_updater(item)
        case items.PerishableItem:
            perishable_item_updater(item)
        case items.ConjuredItem:
            conjured_item_updater(item)
        case _:
            default_item_updater(item)


def update_quality(items: List[Item]):
    match items:
        case []:
            return
        case [item]:
            update_quality_single(item)
        case [item, *rest]:
            update_quality_single(item)
            update_quality(rest)
