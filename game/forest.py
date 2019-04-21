import random

from items import *

class ForestLocation(object):
    def __init__(self, itemTypes):
        self.itemTypes = itemTypes

    def search(self):
        #maybe it would be better to change this to a % based thing
        #rather than having a big list of possible items
        return Item(random.choice(self.itemTypes))

wild = ForestLocation([blueberry, blueberry, apple, \
                       apple, vine, onion, ginger, strawberry, strawberry, mint, \
                       brown_mushroom])
bridge = ForestLocation([stone, shijemi, pebbles, \
                         pebbles, pebbles, vine, vine])
hut = ForestLocation([twig, twig, shijemi, branch, \
                      branch, branch, branch, bark, bark])
bog = ForestLocation([twig, blueberry, vine, vine, twig, dirt])
mine = ForestLocation([sand, sand, sand, pebbles, \
                       pebbles, dirt, stone, stone, stone])
