from gilded_rose import update_quality_single, update_quality
from item import Item, ItemType


def test_foo():
    item = Item("foo", ItemType.default, 0, 0)
    update_quality_single(item)
    assert "foo" == item.name


def test_past_sell_by_date():
    item = Item("foo", ItemType.default, -1, 6)
    update_quality_single(item)
    assert item.quality == 4


def test_quality_never_negative():
    item = Item("foo", ItemType.default, 0, 0)
    update_quality_single(item)
    assert item.quality == 0


def test_aged_brie_quality_increase_over_time():
    item = Item("Aged Brie", ItemType.aged, 0, 3)
    update_quality_single(item)
    assert item.quality == 6


def test_max_quality_is_50():
    item = Item("Aged Brie", ItemType.aged, 0, 50)
    update_quality_single(item)
    assert item.quality == 50


def test_sulfuras_doesnt_decrease_in_quality():
    item = Item("Sulfuras", ItemType.legendary, 0, 3)
    update_quality_single(item)
    assert item.quality == 3


def test_backstage_pass_sellin_greater_than_10():
    item = Item("Pass", ItemType.perishable, 11, 3)
    update_quality_single(item)
    assert item.quality == 4


def test_backstage_pass_sellin_less_than_10():
    item = Item("Pass", ItemType.perishable, 10, 3)
    update_quality_single(item)
    assert item.quality == 5


def test_backstage_pass_sellin_less_than_5():
    item = Item("Pass", ItemType.perishable, 5, 3)
    update_quality_single(item)
    assert item.quality == 6


def test_backstage_pass_sellin_less_than_0():
    item = Item("Pass", ItemType.perishable, -1, 3)
    update_quality_single(item)
    assert item.quality == 0

def test_conjured_item_past_sell_in():
    item = Item("Conjured Pie", ItemType.conjured, 0, 6)
    update_quality_single(item)
    assert item.quality == 2

def test_conjured_item_past_sell_in():
    item = Item("Conjured Pie", ItemType.conjured, 1, 6)
    update_quality_single(item)
    assert item.quality == 4

def test_update_items():
    items = [
        Item("Conjured Pie", ItemType.conjured, 1, 6),
        Item("Conjured Pie", ItemType.conjured, 0, 6),
    ]
    update_quality(items)
    items[0].quality == 2
    items[1].quality == 4