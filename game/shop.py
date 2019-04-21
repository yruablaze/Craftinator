import random
from items import *
# import clock as clock

# for the market, tells it what can be bought
buyItemTypes = [string, cloth, fruit_dish]

# every item
allItemTypes = {
    "blueberry": blueberry,
    "strawberry": strawberry,
    "apple": apple,
    "shijemi": shijemi,
    "onion": onion,
    "ginger": ginger,
    "mint": mint,
    "branch": branch,
    "twig": twig,
    "bark": bark,
    "stone": stone,
    "pebbles": pebbles,
    "sand": sand,
    "vine": vine,
    "string": string,
    "cloth": cloth,
    "dirt": dirt,
    "brick": brick,
    "pole": pole,
    "glass": glass,
    "fruit_dish": fruit_dish
}


# for market - gives a list of things to sell from buyItemTypes, one thing per append
def getBuyable():
    buyableList = []
    buyableList.append(Item(random.choice(buyItemTypes)))
    buyableList.append(Item(random.choice(buyItemTypes)))
    buyableList.append(Item(random.choice(buyItemTypes)))
    return buyableList
