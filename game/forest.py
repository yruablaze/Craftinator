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
        self.itemTypes[ITEM[item]] = chance

    def search(self):
        sum_chance = 0
        for num in [self.itemTypes]:
            sum_chance += num
        random_weight = random.randint(1, sum_chance)
        for chance in [self.itemTypes]:
            random_weight = random_weight - chance
            if random_weight <= 0:
                return self.itemTypes


with open(renpy.loader.transfn("ForestLocations.csv")) as f:
    _locations_list = []
    for row in csv.DictReader(f, skipinitialspace=True):
        _current_line = {}
        for k, v in row.items():
            _current_line[k.lower()] = v
        _location_item = _current_line['item'].lower().replace(" ", "_")
        _chance = int(_current_line['chance'])
        _location = _current_line['location'].upper().replace(" ", "_")
        if _location in _locations_list:
            _location.add_item(_location_item, _chance)
        else:
            _locations_list.append(_location)
            _location = ForestLocation({ITEM[_location_item]: _chance})
# string object can't do add_item
