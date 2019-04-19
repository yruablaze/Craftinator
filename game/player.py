import random
from collections import defaultdict

from items import *
from clock import gameTime



class Player(object):
    def __init__(self, exp, money, actions, actionCount):
        self.exp = exp
        self.lvl = 0
        self.money = money
        self.inventory = Inventory()
        self.actions = actions
        self.actionCount = actionCount

    #for the stats page! not used yet
    def printStats(self):
        return str(self.money), str(self.lvl), str(self.exp)

    #this is doing something, but no way to check right now
    def expGain(self, num=1):
        self.exp += num
        lvlup = 100
        if self.exp >= lvlup:
            self.lvl += 1
            self.exp -= lvlup
            lvlup = lvlup * 1.1
            if (self.lvl % 2 == 0):
                addActions(1)

    #updates the count of actions and
    #checks to see if the day should be advanced
    def addCount(self, num):
        self.actionCount += num
        if self.actionCount >= self.actions:
            gameTime.advanceDay()
            self.actionCount = 0

    #for lvling up, maybe also special foods?
    def addActions(self, num):
        self.actions += num

# A special type of list that stores a player's inventory
# Only store Items here otherwise bad stuff will happen
class Inventory(list):
    def addItem(self, item):
        invItem = self.findType(item)
        if invItem == None:
            self.append(item)
        else:
            invItem.quantity += item.quantity

    # def remove(self, item) comes for free :)
    def removeItem(self, item, num=1):
        invItem = self.findType(item)
        if invItem.quantity == num:
            self.remove(invItem)
        else:
            invItem.quantity -= num

    #??
    def containsType(self, itemType, quantity=1):
        for item in self:
            if item.name == itemType.name and item.quantity >= quantity:
                return True
        return False

    #??
    def findType(self, itemType):
        for item in self:
            if item.name == itemType.name:
                return item
        return None

    #gets a list of sellable items for the vendor
    def getSellable(self):
        return filter( lambda item: item.sellable == True, self )

    # def printSellable(self):
    #     printedItems = []
    #     for item in self:
    #         if item not in printedItems and item.sellable == True:
    #             print "%s (%s g)" % (str(item), str(item.sellPrice()))
    #
    #     print ""

    # def printPretty(self):
    #     itemDict = defaultdict(int)
    #     for item in self:
    #         itemDict[item.name] += 1
    #
    #     for name, quantity in itemDict.iteritems():
    #         print "%s (%s)" % (name, quantity)
    #     print ""



currentPlayer = Player(0, 15, 10, 0)
for i in range(5):
    currentPlayer.inventory.addItem(Item(bark))
currentPlayer.inventory.addItem(Item(blueberry)) # top quality blueberry
currentPlayer.inventory.addItem(Item(blueberry))
currentPlayer.inventory.addItem(Item(blueberry))
currentPlayer.inventory.addItem(Item(apple))
