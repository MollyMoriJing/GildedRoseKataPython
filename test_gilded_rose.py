# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):

        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6), ]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.items == [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]


    def test_aged_brie_quality_increase(self):
        items = [Item("Aged Brie", 2, 49)]  # "Aged Brie" close to the maximum quality
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 50)  # Should not exceed 50
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 50)  # Failing if it exceeds 50


    def test_sulfuras_quality_and_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 80)  # Quality should not change
        self.assertEqual(gilded_rose.items[0].sell_in, 10)  # Sell-in should not decrease

if __name__ == '__main__':
    unittest.main()
