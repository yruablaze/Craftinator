"""Searchable locations

Contains lists of items that can be found in different locations

Thinking of reworking this to a number or % based system
Also some locations unlocked by level or season
"""
import random
from items import *


class ForestLocation(object):
    def __init__(self, itemTypes):
        self.itemTypes = itemTypes

    def add_item(self, item, chance):
        self.itemTypes[ITEM_TYPES[item]] = chance

# TypeError: unsupported operand type(s) for +=: 'int' and 'ItemType' on line 22
    def search(self):
        _sum_chance = 0
        for v in self.itemTypes.itervalues():
            _sum_chance += v
        random_weight = random.randint(1, _sum_chance)
        for item, num in self.itemTypes.iteritems():
            random_weight = random_weight - num
            if random_weight <= 0:
                return Item(item)


LOCATIONS = {}


with open(renpy.loader.transfn("ForestLocations.csv")) as f:
    _locations_list = []
    for row in csv.DictReader(f, skipinitialspace=True):
        _current_line = {}
        for k, v in row.items():
            _current_line[k.lower()] = v
        _item = _current_line['item'].lower().replace(" ", "_")
        _chance = int(_current_line['chance'])
        _location = _current_line['location']
        if _location not in LOCATIONS:
            LOCATIONS[_location] = ForestLocation({ITEM_TYPES[_item]: _chance})
        else:
            LOCATIONS[_location].add_item(_item, _chance)
