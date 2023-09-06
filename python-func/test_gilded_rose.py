from gilded_rose import update_quality_single, update_quality
from items import Item, LegendaryItem, AgedItem, PerishableItem, ConjuredItem


def test_foo():
    item = Item("foo", 0, 0)
    update_quality_single(item)
    assert "foo" == item.name


def test_past_sell_by_date():
    item = Item("foo", -1, 6)
    update_quality_single(item)
    assert item.quality == 4


def test_quality_never_negative():
    item = Item("foo", 0, 0)
    update_quality_single(item)
    assert item.quality == 0


def test_aged_brie_quality_increase_over_time():
    item = AgedItem("Aged Brie", 0, 3)
    update_quality_single(item)
    assert item.quality == 6


def test_max_quality_is_50():
    item = AgedItem("Aged Brie", 0, 50)
    update_quality_single(item)
    assert item.quality == 50


def test_sulfuras_doesnt_decrease_in_quality():
    item = LegendaryItem("Sulfuras", 0, 3)
    update_quality_single(item)
    assert item.quality == 3


def test_backstage_pass_sellin_greater_than_10():
    item = PerishableItem("Pass", 11, 3)
    update_quality_single(item)
    assert item.quality == 4


def test_backstage_pass_sellin_less_than_10():
    item = PerishableItem("Pass", 10, 3)
    update_quality_single(item)
    assert item.quality == 5


def test_backstage_pass_sellin_less_than_5():
    item = PerishableItem("Pass", 5, 3)
    update_quality_single(item)
    assert item.quality == 6


def test_backstage_pass_sellin_less_than_0():
    item = PerishableItem("Pass", -1, 3)
    update_quality_single(item)
    assert item.quality == 0

def test_conjured_item_past_sell_in():
    item = ConjuredItem("Conjured Pie", 0, 6)
    update_quality_single(item)
    assert item.quality == 2

def test_conjured_item_past_sell_in():
    item = ConjuredItem("Conjured Pie", 1, 6)
    update_quality_single(item)
    assert item.quality == 4

def test_update_items():
    items = [
        ConjuredItem("Conjured Pie", 1, 6),
        ConjuredItem("Conjured Pie", 0, 6),
    ]
    update_quality(items)
    items[0].quality == 2
    items[1].quality == 4