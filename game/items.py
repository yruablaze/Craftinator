"""Where Items are made

Items are initialized as ItemType Class
then are turned into the Item Class

We were talking about reworking how these work
And initializing items from a CSV sheet
Tags are not used currently, and may need some more thought
"""
import csv
import renpy


class ItemType(object):
    def __init__(self, name, sellable, buyable, base_buy, base_sell, tags):
        self.name = name
        self.sellable = sellable == 'TRUE'
        self.base_buy = int(base_buy)
        self.base_sell = int(base_sell)
        self.tags = tags
        self.buyable = buyable == 'TRUE'


class Item(object):
    # Star value will alter buy and sell price later
    def __init__(self, itemType, quantity=1, star=None):
        self.type = itemType
        self.quantity = quantity
        if star:
            self.star = star
        else:
            self.star = 1

    @property
    def buy_price(self):
        return self.type.base_buy * self.star

    @property
    def sell_price(self):
        return self.type.base_sell * self.star

    @property
    def name(self):
        return self.type.name

    @property
    def sellable(self):
        return self.type.sellable


class Seeds(object):
    def __init__(self, name, grow_time, refresh, season_grown, crop):
        self.name = name
        self.grow_time = grow_time
        self.refresh = refresh
        self.season = season_grown
        self.crop = crop

    def get_name(self):
        return self.name

    def harvest_crop(self):
        return self.crop

    def get_grow_time(self):
        return self.grow_time

    def growable_check(self):
        return self.season


class SeedStar(object):
    def __init__(self, seeds, star=None):
        self.seed = seeds
        self.star = star

    def up_star(self, num):
        self.star = num


# constant that's a dictionary of dictionaries, oh my!
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
