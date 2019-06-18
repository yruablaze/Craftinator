"""EVENTS

Time passing
Crops growing
Random things happening
Leveling up -> unlocks things
"""


class Events():
    def __init__(self):
        self.dict = {}

    """if statement appends event_handler to list that is
the value of the dictionary. else statement makes new dict entry."""
    def on(self, event_name, event_handler):
        if event_name in self.dict:
            self.dict[event_name].append(event_handler)
        else:
            self.dict[event_name] = [event_handler]

    def trigger(self, event_name):
        if event_name in self.dict:
            for event_handler in self.dict[event_name]:
                event_handler()

# events.on("enter_forest", func)
# events.on("enter_forest", func2)
# events.off("enter_forest", func)
# events.trigger("enter_forest")
# events.on("level_up", check_recipes(player.lvl))

#events --- player level up, items sold count up, items crafted count up
currentEvents = Events()
