import random

class ItemType(object):
    #edible will affect eating food and cooking later
    def __init__(self, name, sellable, baseBuy, baseSell, tags):
        self.name = name
        self.sellable = sellable
        self.baseBuy = baseBuy
        self.baseSell = baseSell
        self.tags = tags

    def __str__(self):
        return self.name

    def sellCheck(self):
        if self.sellable == True:
            return True
        else:
            return False

    

class Item(object):
    #Star value will alter buy and sell price later
    def __init__(self, itemType, star=None):
        self.type = itemType

        if star:
            self.star = star
        else:
            self.star = random.randint(1,5)

    @property
    def buyPrice(self):
        return self.type.baseBuy * self.star

    @property
    def sellPrice(self):
        return self.type.baseSell * self.star

    @property
    def name(self):
        return self.type.name

    def __str__(self):
        return self.name

    @property
    def sellable(self):
        return self.type.sellable


class Seeds(object):
    def __init__(self, name, growTime, refreshTime, seasonGrown, crop):
        self.name = name
        self.growTime = growTime
        self.refresh = refreshTime
        self.season = seasonGrown
        self.crop = crop


    def getName(self):
        return self.name
    
    def harvestCrop(self):
        return self.crop

    def getGrowTime(self):
        return self.growTime

    def growableCheck(self):
        return self.season


class seedPlot(object):
    def __init__(self, seeds, star=None):
        self.seed = seeds
        self.star = star
        
    def upStar(self, num):
        self.star = num


#later: if there isn't a way to use it it should be sellable
# (self, name, sellable, buy, sell)
#raw food  = ItemType("", True, 4, 2, ["edible"])
blueberry = ItemType("blueberry", True, 3, 2, ["edible", "sweet"])
shijemi = ItemType("shijemi", True, 3, 2, ["edible", "mushroom"])
brown_mushroom = ItemType("brown_mushroom", True, 3, 1, ["edible", "mushroom"])
apple = ItemType("apple", True, 4, 2, ["edible", "crop"])
onion = ItemType("onion", True, 3, 1, ["edible", "crop"])
ginger = ItemType("ginger", True, 2, 1, ["edible"])
strawberry = ItemType("strawberry", True, 3, 2, ["edible", "sweet", "crop"])
mint = ItemType("mint", True, 2, 1, ["edible", "herb", "crop"])

#crafted food = ItemType("", True, 4, 2, [])
fruit_dish = ItemType("fruit_dish", True, 16, 12, ["edible"])

#base  = ItemType("", False, 1, 0, [])
vine = ItemType("vine", False, 3, 0, [])
twig = ItemType("twig", False, 1, 0, [])
branch = ItemType("branch", False, 3, 0, [])
bark = ItemType("bark", False, 1, 0, [])
stone = ItemType("stone", False, 2, 0, [])
pebbles = ItemType("pebbles", False, 1, 0, [])
dirt = ItemType("dirt", False, 1, 0, [])
sand = ItemType("sand", False, 2, 0, [])

#craft = ItemType("", False, 5, 0, [])
string = ItemType("string", False, 5, 0, [])
cloth = ItemType("cloth", True, 15, 11, [])
brick = ItemType("brick", True, 4, 2, [])
pole = ItemType("pole", True, 5, 0, [])
glass = ItemType("glass", True, 3, 0, [])

#seeds = Seed("name", growTime, refreshTime, ["seasonsGrown"])
onion_seed = Seeds("onion_seed", 5, None, ["Summer", "Fall"], onion)
strawberry_seed = Seeds("strawberry_seed", 9, 3, ["Summer"], strawberry)
