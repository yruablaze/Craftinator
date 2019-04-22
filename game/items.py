"""Where Items are made

Items are initialized as ItemType Class
then are turned into the Item Class

We were talking about reworking how these work
And initializing items from a CSV sheet
Tags are not used currently, and may need some more thought
"""


class ItemType(object):
    def __init__(self, name, sellable, base_buy, base_sell, tags):
        self.name = name
        self.sellable = sellable
        self.base_buy = base_buy
        self.base_sell = base_sell
        self.tags = tags


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
    def __init__(self, name, growTime, refreshTime, seasonGrown, crop):
        self.name = name
        self.grow_time = growTime
        self.refresh = refreshTime
        self.season = seasonGrown
        self.crop = crop

    def get_name(self):
        return self.name

    def harvest_crop(self):
        return self.crop

    def get_grow_time(self):
        return self.growTime

    def growable_check(self):
        return self.season


class SeedStar(object):
    def __init__(self, seeds, star=None):
        self.seed = seeds
        self.star = star

    def up_star(self, num):
        self.star = num


# (self, name, sellable, buy, sell, tags)
# raw food  = ItemType("", True, 4, 2, ["edible"])
blueberry = ItemType("blueberry", True, 3, 2, ["edible", "sweet"])
shijemi = ItemType("shijemi", True, 3, 2, ["edible", "mushroom"])
brown_mushroom = ItemType("brown mushroom", True, 3, 1, ["edible", "mushroom"])
apple = ItemType("apple", True, 4, 2, ["edible", "crop"])
onion = ItemType("onion", True, 3, 1, ["edible", "crop"])
ginger = ItemType("ginger", True, 2, 1, ["edible"])
strawberry = ItemType("strawberry", True, 3, 2, ["edible", "sweet", "crop"])
mint = ItemType("mint", True, 2, 1, ["edible", "herb", "crop"])

# crafted food = ItemType("", True, 4, 2, [])
fruit_dish = ItemType("fruit dish", True, 16, 12, ["edible"])

# base  = ItemType("", False, 1, 0, [])
vine = ItemType("vine", False, 3, 0, [])
twig = ItemType("twig", False, 1, 0, [])
branch = ItemType("branch", False, 3, 0, [])
bark = ItemType("bark", False, 1, 0, [])
stone = ItemType("stone", False, 2, 0, [])
pebbles = ItemType("pebbles", False, 1, 0, [])
dirt = ItemType("dirt", False, 1, 0, [])
sand = ItemType("sand", False, 2, 0, [])

# craft = ItemType("", False, 5, 0, [])
string = ItemType("string", False, 5, 0, [])
cloth = ItemType("cloth", True, 15, 11, [])
brick = ItemType("brick", True, 4, 2, [])
pole = ItemType("pole", True, 5, 0, [])
glass = ItemType("glass", True, 3, 0, [])

# seeds = Seed("name", growTime, refreshTime, ["seasonsGrown"])
onion_seed = Seeds("onion seed", 5, None, ["Summer", "Fall"], onion)
strawberry_seed = Seeds("strawberry seed", 9, 3, ["Summer"], strawberry)
