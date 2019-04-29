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

    def search(self):
        return Item(random.choice(self.itemTypes))


# randomWeight = rand(1, sumOfWeights)
# for each item in array
#     randomWeight = randomWeight - item.Weight
#     if randomWeight <= 0
#         return item

# this is a bit messy right now, but once these are in a csv, it'll be nicer
WILD = ForestLocation([ITEM['blueberry'], ITEM['blueberry'], ITEM['apple'],
                       ITEM['apple'], ITEM['vine'], ITEM['onion'], ITEM['ginger'],
                       ITEM['strawberry'], ITEM['strawberry'], ITEM['mint'],
                       ITEM['brown_mushroom']])
BRIDGE = ForestLocation([ITEM['stone'], ITEM['shijemi'], ITEM['pebbles'],
                         ITEM['pebbles'], ITEM['pebbles'], ITEM['vine'], ITEM['vine']])
HUT = ForestLocation([ITEM['twig'], ITEM['twig'], ITEM['shijemi'], ITEM['branch'],
                      ITEM['branch'], ITEM['branch'], ITEM['branch'], ITEM['bark'], ITEM['bark']])
BOG = ForestLocation([ITEM['twig'], ITEM['blueberry'], ITEM['vine'],
                     ITEM['vine'], ITEM['twig'], ITEM['dirt']])
MINE = ForestLocation([ITEM['sand'], ITEM['sand'], ITEM['sand'],
                       ITEM['pebbles'], ITEM['pebbles'], ITEM['dirt'],
                       ITEM['stone'], ITEM['stone'], ITEM['stone']])
