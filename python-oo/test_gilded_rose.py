from gilded_rose import (
    AGED_BRIE,
    SULFURAS,
    BACKSTAGE_PASS,
    CONJURED_MANA_CAKE,
    update_quality_single,
)
from item import Item


def test_foo():
    item = Item("foo", 0, 0)
    update_quality_single(item)
    assert "foo" == item.name


def test_past_sell_by_date():
    item = Item("foo", 6, -1)
    update_quality_single(item)
    assert item.quality == 4


def test_quality_never_negative():
    item = Item("foo", 0, 0)
    update_quality_single(item)
    assert item.quality == 0


def test_aged_brie_quality_increase_over_time():
    item = Item(AGED_BRIE, 3, 0)
    update_quality_single(item)
    assert item.quality == 6


def test_max_quality_is_50():
    item = Item(AGED_BRIE, 50, 0)
    update_quality_single(item)
    assert item.quality == 50


def test_sulfuras_doesnt_decrease_in_quality():
    item = Item(SULFURAS, 3, 0)
    update_quality_single(item)
    assert item.quality == 3


def test_backstage_pass_sellin_greater_than_10():
    item = Item(BACKSTAGE_PASS, 3, 11)
    update_quality_single(item)
    assert item.quality == 4


def test_backstage_pass_sellin_less_than_10():
    item = Item(BACKSTAGE_PASS, 3, 10)
    update_quality_single(item)
    assert item.quality == 5


def test_backstage_pass_sellin_less_than_5():
    item = Item(BACKSTAGE_PASS, 3, 5)
    update_quality_single(item)
    assert item.quality == 6


def test_backstage_pass_sellin_less_than_0():
    item = Item(BACKSTAGE_PASS, 3, -1)
    update_quality_single(item)
    assert item.quality == 0


def test_conjured_items_degrade_twice_as_fast_negative_sellin():
    item = Item(CONJURED_MANA_CAKE, 6, -1)
    update_quality_single(item)
    assert item.quality == 2


def test_conjured_items_degrade_twice_as_fast():
    item = Item(CONJURED_MANA_CAKE, 6, 1)
    update_quality_single(item)
    assert item.quality == 4
