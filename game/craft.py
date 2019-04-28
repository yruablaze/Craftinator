"""Recipes!

contains the list of recipes for crafting
a tuple (item, dictionary) but only by choice

used to contain all of crafting
the class doesn't do much
"""
from items import *
import csv
import renpy


class Recipe(object):
    def __init__(self, product, components):
        self.product = product
        self.components = components

    def add_components(self, name, quantity):
        self.components = self.components


# this is a bit messy right now, but once recipes are in a csv, it'll be nicer
recipes = {}

hidden_recipes = {}
# "brick": Recipe(ITEM['brick'], {ITEM['stone']: 2})


def add_to_recipes(key):
    if key in hidden_recipes:
        thing = hidden_recipes[key]
        recipes[key] = thing
        del hidden_recipes[key]


with open(renpy.loader.transfn("recipes.csv")) as f:
    for row in csv.DictReader(f, skipinitialspace=True):
        _current_recipes = {}
        for k, v in row.items():
            if k in recipes:
                _blup = _current_recipes['product'].lower().replace(" ", "_")
                _blup.add_components('component', 'quantity')
                break
            else:
                _current_recipes[k.lower()] = v
        _recipe_name = str(_current_recipes['name'])
        _recipe_product = _current_recipes['product'].lower().replace(" ", "_")
        recipes[_recipe_name] = Recipe(ITEM[_recipe_product], {ITEM[_current_recipes['component']]: _current_recipes['quantity']})
