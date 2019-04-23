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


recipes = {
    "string": Recipe(string, {bark: 2}),
    "cloth": Recipe(cloth, {string: 4, twig: 1}),
    "brick": Recipe(brick, {stone: 2}),
    "fruit_dish": Recipe(fruit_dish, {blueberry: 3, apple: 1}),
}

hidden_recipes = {
    "glass": Recipe(glass, {sand: 3}),
    "dirt": Recipe(dirt, {pebbles: 5}),
    "pebbles": Recipe(pebbles, {stone: 1}),
    "twig": Recipe(twig, {branch: 1}),
    "bark": Recipe(bark, {branch: 1}),
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
