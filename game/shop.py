import random
from items import *

"""What can be bought

Used to run all buying and selling.
Now a list of things that can be bought from market

Maybe later there will be more market stalls
And more lists of things that can be bought
"""


# for the market, tells it what can be bought
buy_items_list = [string, cloth, fruit_dish]
# for later when more items might be available
avail_items = 3


# for market - makes a random list from buy_items_list, one thing per line
def get_buyable():
    buyable_list = []
    for i in range(avail_items):
        buyable_list.append(Item(random.choice(buy_items_list)))
    return buyable_list
