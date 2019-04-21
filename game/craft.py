from items import *


class Recipe(object):
    def __init__(self, product, components):
        self.product = product
        self.components = components

    def craftCheck(self, inventory):
        if inventory.containsType(component, quantity) is True:
            return quantity, component, self.product


recipes = {
    "twig": Recipe(twig, {branch: 1}),
    "bark": Recipe(bark, {branch: 1}),
    "string": Recipe(string, {bark: 2}),
    "pebbles": Recipe(pebbles, {stone: 1}),
    "cloth": Recipe(cloth, {string: 4, twig: 1}),
    "dirt": Recipe(dirt, {pebbles: 5}),
    "brick": Recipe(brick, {stone: 2}),
    "fruit_dish": Recipe(fruit_dish, {blueberry: 3, apple: 1}),
    "glass": Recipe(glass, {sand: 3}),
}
