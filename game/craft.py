"""Recipes!

contains the list of recipes for crafting
a tuple (item, dictionary) but only by choice

used to contain all of crafting
the class doesn't do much
"""
from items import *


class Recipe(object):
    def __init__(self, product, components):
        self.product = product
        self.components = components


# this is a bit messy right now, but once recipes are in a csv, it'll be nicer
recipes = {
    "string": Recipe(ITEM['string'], {ITEM['bark']: 2}),
    "cloth": Recipe(ITEM['cloth'], {ITEM['string']: 4, ITEM['twig']: 1}),
    "brick": Recipe(ITEM['brick'], {ITEM['stone']: 2}),
    "fruit_dish": Recipe(ITEM['fruit_dish'], {ITEM['blueberry']: 3, ITEM['apple']: 1}),
}

hidden_recipes = {
    "glass": Recipe(ITEM['glass'], {ITEM['sand']: 3}),
    "dirt": Recipe(ITEM['dirt'], {ITEM['pebbles']: 5}),
    "pebbles": Recipe(ITEM['pebbles'], {ITEM['stone']: 1}),
    "twig": Recipe(ITEM['twig'], {ITEM['branch']: 1}),
    "bark": Recipe(ITEM['bark'], {ITEM['branch']: 1}),
}

"""tested(gives error) and unused

def add_to_recipes(key):
    if key in hidden_recipes:
        thing = get(key[])
        recipes[key] = thing
        del hidden_recipes.key

"fruit_dish": Recipe((fruit_dish, {blueberry: 3, apple: 1}), \
(fruit_dish, {apple: 2, strawberry: 2})),
"""
