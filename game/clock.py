## from Singleton import Singleton
#having lots of problems with singleton class
#can't use functions that should work.. gives attributeErrors saying
#singleton instance has no attribute ____

#going to use a regular class instead



class Season:
    SPRING = 1
    SUMMER = 2
    FALL = 3
    WINTER = 4


##@Singleton
class Time(object):
    def __init__(self, day, season, year):
        self.day = day
        self.season = season
        self.year = year

    def checkClock(self):
        return (str(gameTime.seasonFriendly()), str(self.day), str(self.year))


    #moves time forward! ^_^
    def advanceDay(self):
        self.count = 0
        if self.day < 30:
            self.day += 1
        elif self.season < Season.WINTER:
            self.day = 1
            self.season += 1
        else:
            self.day = 1
            self.season = 1
            self.year += 1
            
        print ""
        print "It's a new day!"
        gameTime.checkClock()
        
        

    #returns the season to be printed
    def seasonFriendly(self):
        if self.season == Season.SPRING:
            return "Spring"
        elif self.season == Season.SUMMER:
            return "Summer"
        elif self.season == Season.FALL:
            return "Fall"
        elif self.season == Season.WINTER:
            return "Winter"

gameTime = Time(1, Season.SPRING, 1)
