import random
from items import *

"""Searchable locations

Contains lists of items that can be found in different locations

Thinking of reworking this to a number or % based system
Also some locations unlocked by level or season
"""


class ForestLocation(object):
    def __init__(self, itemTypes):
        self.itemTypes = itemTypes

    def search(self):
        # maybe it would be better to change this to a % based thing
        # rather than having a big list of possible items
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
