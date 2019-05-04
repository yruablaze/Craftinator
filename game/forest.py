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


with open(renpy.loader.transfn("ForestLocations.csv")) as f:
    _locations_list = []
    for row in csv.DictReader(f, skipinitialspace=True):
        _current_line = {}
        for k, v in row.items():
            _current_line[k.lower()] = v
        _location_item = _current_line['item'].lower().replace(" ", "_")
        _chance = int(_current_line['chance'])
        if _current_line['location'] not in _locations_list:
            if _current_line['location'] == "WILD":
                WILD = ForestLocation({ITEM_TYPES[_location_item]: _chance})
            elif _current_line['location'] == "BRIDGE":
                BRIDGE = ForestLocation({ITEM_TYPES[_location_item]: _chance})
            elif _current_line['location'] == "HUT":
                HUT = ForestLocation({ITEM_TYPES[_location_item]: _chance})
            elif _current_line['location'] == "BOG":
                BOG = ForestLocation({ITEM_TYPES[_location_item]: _chance})
            elif _current_line['location'] == "MINE":
                MINE = ForestLocation({ITEM_TYPES[_location_item]: _chance})
            _locations_list.append(_current_line['location'])
        else:
            if _current_line['location'] == "WILD":
                WILD.add_item(_location_item, _chance)
            elif _current_line['location'] == "BRIDGE":
                BRIDGE.add_item(_location_item, _chance)
            elif _current_line['location'] == "HUT":
                HUT.add_item(_location_item, _chance)
            elif _current_line['location'] == "BOG":
                BOG.add_item(_location_item, _chance)
            elif _current_line['location'] == "MINE":
                MINE.add_item(_location_item, _chance)
