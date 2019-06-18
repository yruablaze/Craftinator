"""What can be bought

List of things that can be bought from market

Notes:
Maybe later there will be more market stalls
And more lists of things that can be bought
    ie: seed seller sells seeds, traveling merchent sells rare things
"""
import random
from items import *


# add buyable items to the BUY_ITEMS_LIST
# make it a constant, since it only needs to be done once
BUY_ITEMS_LIST = []
for k, v in ITEM_TYPES.items():
    if v.buyable:
        BUY_ITEMS_LIST.append(v)


# for market - makes a random list from buy_items_list, one thing per line
def get_buyable(avail_items=3):
    buyable_list = []
    for i in range(avail_items):
        buyable_list.append(Item(random.choice(BUY_ITEMS_LIST)))
    return buyable_list

special_recipes_path = {}

with open(renpy.loader.transfn("data/specialRecipeKeys.csv")) as f:
    for row in csv.DictReader(f, skipinitialspace=True):
        _current_line = {}
        for k, v in row.items():
            _current_line[k.lower()] = v
        _key = _current_line['name'].lower().replace(" ", "_")
        _name = _current_line['name']
        _stat = _current_line['stat']
        _count = int(_current_line['count'])
        special_recipes_path[_key] = {"name": _name, "stat": _stat, "count": _count}
