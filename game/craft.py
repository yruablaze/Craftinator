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
        self.components[ITEM_TYPES[name]] = quantity


# this is a bit messy right now, but once recipes are in a csv, it'll be nicer
recipes = {}

hidden_recipes = {}
# "brick": Recipe(ITEM_TYPES['brick'], {ITEM_TYPES['stone']: 2})


def find_recipe(key):
    """use when player should find new recipes"""
    if key in hidden_recipes:
        recipes[key] = hidden_recipes[key]
        del hidden_recipes[key]
        return True
    return False


with open(renpy.loader.transfn("recipes.csv")) as f:
    for row in csv.DictReader(f, skipinitialspace=True):
        _current_line = {}
        for k, v in row.items():
            _current_line[k.lower()] = v
        _component = _current_line['component'].lower().replace(" ", "_")
        _quantity = int(_current_line['quantity'])
        if _current_line['name'] in hidden_recipes:
            hidden_recipes[_current_line['name']].add_components(_component, _quantity)
        else:
            _product = _current_line['product'].lower().replace(" ", "_")
            hidden_recipes[_current_line['name']] = Recipe(ITEM_TYPES[_product], {ITEM_TYPES[_component]: _quantity})


with open(renpy.loader.transfn("hidden.csv")) as f:
    for row in csv.DictReader(f, skipinitialspace=True):
        _current_line = {}
        for k, v in row.items():
            _current_line[k.lower()] = v
        if _current_line['hidden'] != 'TRUE':
            _key = _current_line['name']
            recipes[_key] = hidden_recipes[_key]
            del hidden_recipes[_key]
