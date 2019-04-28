"""Time and Time progression

Counts the days, seasons and years
"""


class Season:
    SPRING = 1
    SUMMER = 2
    FALL = 3
    WINTER = 4


## @Singleton
class Time(object):
    def __init__(self, day, season, year):
        self.day = day
        self.season = season
        self.year = year

    def check_clock(self):
        return (str(gameTime.season_friendly()), str(self.day), str(self.year))


    # moves time forward! ^_^
    # M - it might be nice to have something that jumps up for the day changes
    # maybe use events.py for that
    def advance_day(self):
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

        gameTime.check_clock()


    # returns the season to be printed
    def season_friendly(self):
        if self.season == Season.SPRING:
            return "Spring"
        elif self.season == Season.SUMMER:
            return "Summer"
        elif self.season == Season.FALL:
            return "Fall"
        elif self.season == Season.WINTER:
            return "Winter"


gameTime = Time(1, Season.SPRING, 1)
