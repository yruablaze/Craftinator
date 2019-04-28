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
        self.components[ITEM[name]] = quantity


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
        _current_recipe_line = {}
        for k, v in row.items():
            _current_recipe_line[k.lower()] = v
        _recipe_component = _current_recipe_line['component'].lower().replace(" ", "_")
        if _current_recipe_line['name'] in recipes:
            recipes[_current_recipe_line['name']].add_components(_recipe_component, _current_recipe_line['quantity'])
        else:
            _recipe_product = _current_recipe_line['product'].lower().replace(" ", "_")
            recipes[_current_recipe_line['name']] = Recipe(ITEM[_recipe_product], {ITEM[_recipe_component]: _current_recipe_line['quantity']})
