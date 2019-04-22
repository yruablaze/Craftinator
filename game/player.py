import random
from collections import defaultdict
from items import *
from clock import gameTime

"""The Player

Contains the player class called with currentPlayer
Contains the player inventory a sub class of the player class
Adds items to currentPlayer inventory at page bottom
"""


class Player(object):
    def __init__(self, exp, money, actions, actionCount):
        self.exp = exp
        self.lvl = 1
        self.lvlUp = 100
        self.money = money
        self.inventory = Inventory()
        self.actions = actions
        self.actionCount = actionCount

    # experince UP
    def expGain(self, num=1):
        self.exp += num
        if self.exp >= self.lvlUp:
            self.lvl += 1
            self.exp -= self.lvlUp
            self.lvlUp = self.lvlUp * 1.1
            if (self.lvl % 2 == 0):
                self.addActions(1)

    # updates the count of actions and
    # checks to see if the day should be advanced
    def addCount(self, num):
        self.actionCount += num
        if self.actionCount >= self.actions:
            gameTime.advanceDay()
            self.actionCount -= self.actions

    # for lvling up, maybe also special foods?
    def addActions(self, num):
        self.actions += num


# A special type of list that stores a player's inventory
# Only store Items here otherwise bad stuff will happen
class Inventory(list):
    def addItem(self, item):
        invItem = self.findType(item)
        if invItem is None:
            self.append(item)
        else:
            invItem.quantity += item.quantity

    def removeItem(self, item, num=1):
        invItem = self.findType(item)
        if invItem.quantity == num:
            self.remove(invItem)
        else:
            invItem.quantity -= num

    # Checks if the item exists in inv and if there is enough of the item
    def containsType(self, itemType, quantity=1):
        for item in self:
            if item.name == itemType.name and item.quantity >= quantity:
                return True
        return False

    # checks if the item is in the inv and returns the item
    def findType(self, itemType):
        for item in self:
            if item.name == itemType.name:
                return item
        return None

    # gets a list of sellable items for the vendor
    def getSellable(self):
        return filter( lambda item: item.sellable is True, self )

    # get whole inventory as a list
    def getList(self):
        invList = []
        for item in self:
            invList.append(item)
        return invList


# Player(exp, money, actions, actionCount)
currentPlayer = Player(0, 15, 10, 0)

for i in range(5):
    currentPlayer.inventory.addItem(Item(bark))
currentPlayer.inventory.addItem(Item(blueberry))
currentPlayer.inventory.addItem(Item(blueberry))
currentPlayer.inventory.addItem(Item(blueberry))
currentPlayer.inventory.addItem(Item(apple))
