import random
from items import *

"""What can be bought

Used to run all buying and selling.
Now a list of things that can be bought from market

Maybe later there will be more market stalls
And more lists of things that can be bought
"""


# for the market, tells it what can be bought
buyItemTypes = [string, cloth, fruit_dish]


# for market - gives a list of things to sell from buyItemTypes, one thing per append
def getBuyable():
    buyableList = []
    buyableList.append(Item(random.choice(buyItemTypes)))
    buyableList.append(Item(random.choice(buyItemTypes)))
    buyableList.append(Item(random.choice(buyItemTypes)))
    return buyableList
