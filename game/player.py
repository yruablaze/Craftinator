"""The Player

Contains the player class called with currentPlayer
Contains the player inventory a sub class of the player class
Adds items to currentPlayer inventory at page bottom
"""
from collections import defaultdict
from items import *
from clock import gameTime


class Player(object):
    def __init__(self, exp, money, actions, action_count):
        self.exp = exp
        self.lvl = 1
        self.lvl_up = 100
        self.money = money
        self.inventory = Inventory()
        self.actions = actions
        self.action_count = action_count

    # experince UP
    def exp_gain(self, num=1):
        self.exp += num
        if self.exp >= self.lvl_up:
            self.lvl += 1
            self.exp -= self.lvl_up
            self.lvl_up = self.lvl_up * 1.1
            if self.lvl % 2 == 0:
                self.add_actions(1)

    # updates the count of actions and
    # checks to see if the day should be advanced
    def add_action_count(self, num):
        self.action_count += num
        if self.action_count >= self.actions:
            gameTime.advance_day()
            self.action_count -= self.actions

    # for lvling up, maybe also special foods?
    def add_actions(self, num):
        self.actions += num


# A special type of list that stores a player's inventory
# Only store Items here otherwise bad stuff will happen
class Inventory(list):
    def add_item(self, item):
        inv_item = self.find_item(item)
        if inv_item is None:
            self.append(item)
        else:
            inv_item.quantity += item.quantity

    def remove_item(self, item, num=1):
        inv_item = self.find_item(item)
        if inv_item.quantity == num:
            self.remove(inv_item)
        else:
            inv_item.quantity -= num

    # Checks if the item exists in inv and if there is enough of the item
    def contains_item(self, itemType, quantity=1):
        for item in self:
            if item.name == itemType.name and item.quantity >= quantity:
                return True
        return False

    # checks if the item is in the inv and returns the item
    def find_item(self, itemType):
        for item in self:
            if item.name == itemType.name:
                return item
        return None

    # gets a list of sellable items for the vendor
    def get_sellable(self):
        return filter(lambda item: item.sellable is True, self)

    # get whole inventory as a list
    def get_list(self):
        inv_list = []
        for item in self:
            inv_list.append(item)
        return inv_list


# Player(exp, money, actions, action_count)
currentPlayer = Player(0, 15, 10, 0)

for i in range(5):
    currentPlayer.inventory.add_item(Item(bark))
for i in range(3):
    currentPlayer.inventory.add_item(Item(blueberry))
currentPlayer.inventory.add_item(Item(apple))
