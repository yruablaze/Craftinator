"""Where Items are made

Items are a subclass of ItemType.

Tags are not used currently, and may need some more thought
"""
import csv
import renpy


class ItemType(object):
    def __init__(self, name, sellable, buyable, base_buy, base_sell, tags):
        self.name = name
        self.sellable = sellable == 'TRUE' or sellable is True
        self.base_buy = int(base_buy)
        self.base_sell = int(base_sell)
        self.tags = tags
        self.buyable = buyable == 'TRUE' or buyable is True


class Item(ItemType):
    # Star value will alter buy and sell price later
    def __init__(self, item_type, quantity=1, star=None):
        ItemType.__init__(self, item_type.name, item_type.sellable,
                          item_type.buyable, item_type.base_buy,
                          item_type.base_sell, item_type.tags)
        self.quantity = quantity
        if star:
            self.star = star
        else:
            self.star = 1

    @property
    def buy_price(self):
        return self.base_buy * self.star

    @property
    def sell_price(self):
        return self.base_sell * self.star


class Seeds(object):
    def __init__(self, name, grow_time, refresh, season_grown, crop):
        self.name = name
        self.grow_time = grow_time
        self.refresh = refresh
        self.season = season_grown
        self.crop = crop


class SeedStar(object):
    def __init__(self, seeds, star=None):
        self.seed = seeds
        self.star = star

    def up_star(self, num):
        self.star = num


# e.g. {'apple': {'name': 'apple', sellable': 'TRUE', 'edible': 'TRUE'...}...}
ITEM = {}
with open(renpy.loader.transfn("items.csv")) as f:
    for row in csv.DictReader(f, skipinitialspace=True):
        _current_items = {}
        for k, v in row.items():
            _current_items[k.lower()] = v
        # change "brown mushroom" to "brown_mushroom" when used as key
        _item_name = _current_items['name'].lower().replace(" ", "_")
        ITEM[_item_name] = ItemType(_current_items['name'], _current_items['sellable'], _current_items['buyable'], _current_items['buyprice'], _current_items['sellprice'], [])


# seeds = Seed("name", grow_time, refresh, ["season_grown"], crop)
onion_seed = Seeds("onion seed", 5, None, ["Summer", "Fall"], ITEM['onion'])
strawberry_seed = Seeds("strawberry seed", 9, 3, ["Summer"], ITEM['strawberry'])
