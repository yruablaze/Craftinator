import random
from clock import gameTime
from player import currentPlayer
from items import seedPlot

class Plot(object):
    def __init__ (self, soilLvl, seed):
        self.soilLvl = soilLvl
        self.seed = seed
        self.timePassed = 0

    def __str__ (self):
        return str(self.seed) + " - " + str(self.soilLvl)


class Field(object):
    def __init__(self):
        self.plotList = []
    
        for i in range(1, 7):
            self.plotList.append( Plot(1, None) )

    def addSeed(self, seed):
        seedAdded = False
        for plot in self.plotList:
            if plot.seed == None:
                plot.seed = seed
                seedAdded = True
                plot.timePassed = 0
                inventory.removeType(seed)
                break
        if not seedAdded:
            print "No room in this field for your crop!"

    def __str__ (self):
        outStr=""
        for plot in self.plotList:
            outStr += str(plot) + "\n"
        return outStr

    def checkDay(self):
        for plot in self.plotList:
            if plot.seed not == None:
                days = Seeds.getGrowTime(plot.seed)
                
        
    
fieldOne = Field()

