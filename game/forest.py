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
        # over - to find recipes and seeds this can't do Item here
        return Item(random.choice(self.itemTypes))


WILD = ForestLocation([blueberry, blueberry, apple, \
                       apple, vine, onion, ginger, strawberry, strawberry, mint, \
                       brown_mushroom])
BRIDGE = ForestLocation([stone, shijemi, pebbles, \
                         pebbles, pebbles, vine, vine])
HUT = ForestLocation([twig, twig, shijemi, branch, \
                      branch, branch, branch, bark, bark])
BOG = ForestLocation([twig, blueberry, vine, vine, twig, dirt])
MINE = ForestLocation([sand, sand, sand, pebbles, \
                       pebbles, dirt, stone, stone, stone])
