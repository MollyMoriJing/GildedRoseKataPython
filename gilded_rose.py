# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemStrategy:
    """Base class for all item strategies"""
    def update_item(self, item):
        pass


class NormalItemStrategy(ItemStrategy):
    def update_item(self, item):
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


class AgedBrieStrategy(ItemStrategy):
    def update_item(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class SulfurasStrategy(ItemStrategy):
    def update_item(self, item):
        # Sulfuras never changes, no need to modify item
        pass


class BackstagePassesStrategy(ItemStrategy):
    def update_item(self, item):
        if item.sell_in > 0:
            if item.sell_in <= 5:
                item.quality = min(item.quality + 3, 50)
            elif item.sell_in <= 10:
                item.quality = min(item.quality + 2, 50)
            else:
                item.quality += 1
        else:
            item.quality = 0
        item.sell_in -= 1


class ConjuredItemStrategy(ItemStrategy):
    def update_item(self, item):
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 2  # Degrade quality twice as fast
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2  # Degrade quality twice as fast after sell-in


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items


    def update_quality(self):
        for item in self.items:
            strategy = self.get_strategy(item)
            strategy.update_item(item)


    def get_strategy(self, item: Item) -> ItemStrategy:
        if item.name == "Aged Brie":
            return AgedBrieStrategy()
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasStrategy()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassesStrategy()
        elif "Conjured" in item.name:
            return ConjuredItemStrategy()
        else:
            return NormalItemStrategy()