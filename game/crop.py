"""The field for growing

Crop.py is not used yet, for V0.6
"""

from clock import gameTime
from player import currentPlayer
from items import Seeds


class Plot(object):
    def __init__(self, soil_lvl, seed):
        self.soil_lvl = soil_lvl
        self.seed = seed
        self.time_passed = 0

    def __str__(self):
        return str(self.seed) + " - " + str(self.soil_lvl)


class Field(object):
    def __init__(self):
        self.plot_list = []
        for i in range(1, 7):
            self.plot_list.append(Plot(1, None))

    def add_seed(self, seed):
        seed_added = False
        for plot in self.plot_list:
            if plot.seed is None:
                plot.seed = seed
                seed_added = True
                plot.time_passed = 0
                currentPlayer.inventory.remove_item(seed)
                break
        if not seed_added:
            print("No room in this field for your crop!")

    def __str__(self):
        outStr = ""
        for plot in self.plot_list:
            outStr += str(plot) + "\n"
        return outStr


"""This won't work proper, will look at later
    def check_day(self):
        for plot in self.plot_list:
            if plot.seed is not None:
                days = Seeds.get_grow_time(plot.seed)
"""


field_one = Field()
