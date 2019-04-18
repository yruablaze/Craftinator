# The script of the game goes in this file.

init python:
    import random
    import forest
    from player import currentPlayer
    import items
    import craft
    from shop import Shop
    from clock import gameTime

    def show_time(a, at):
        d= Text("It is %s %s in Year %s." % gameTime.checkClock())
        return d, None

image showingTime = DynamicDisplayable(show_time)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# commented out for now, using narrator instead of Mel
#define m = Character("Mel")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene Crossroads
    show showingTime at left
    show countdown at top

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #M - don't need this yet
    #show eileen happy

    menu:
        "Visit the Forest":
            scene Forest
            narrator "The forest is an excellent spot to find items!"
            jump forest
        "Go to the Field":
            scene Field
            jump field
        "Go to the Barn":
            scene Barn
            jump barn
        "Open a Vendor Stall":
            scene Stall
            jump stall
        "Visit the Market":
            scene Market
            jump market
        "Go to the Crafting Bench":
            scene Crafting
            jump crafting
        "View Stats":
            scene Stats
            jump stats
        "Quit":
            # This ends the game.
            return

label forest:

    menu:
        narrator "Where do you want to look?"

        "In a wild field":
            #example of single line python script (using dollar sign)
            $ item = forest.wild.search()
            jump foundSomething
        "Under the Sunny Brook Bridge":
            $ item = forest.bridge.search()
            jump foundSomething
        "By the Forester's Hut":
            $ item = forest.hut.search()
            jump foundSomething
        "Around Pea Bog":
            $ item = forest.bog.search()
            jump foundSomething
        "By the old mine":
            $ item = forest.mine.search()
            jump foundSomething
        "Go back Home":
            jump start

label foundSomething:
    #example of mult-line python script
    python:
        narrator( "You found a %s!" % item.name )
        currentPlayer.inventory.add(item)
        currentPlayer.addCount(10)
        currentPlayer.expGain(1)
    jump forest

label field:
    narrator "You are in the field"
    jump start

label barn:
    narrator "You are in the barn"
    jump start

label stall:
    narrator "You are at the vendor stall" (interact=False)
    python:
        choice=None
        sellableItems = currentPlayer.inventory.getSellable();
        menu_items = []
        menu_items.append(("Choose an item to sell:", None))
        for item in sellableItems:
            menu_items.append(("Sell one %s for %s gold." % (item.name, item.sellPrice ), item))
        menu_items.append(("Nevermind", "Nevermind"))
        # each tuple in menu_items is (text_displayed_in_menu, object_returned_upon_selection)
        choice = menu(menu_items)
        if (choice == "Nevermind"):
            renpy.jump("start")
        else:
            #todo: add code to actually sell the item
            narrator ("You sold 1 %s for %s gold" % (choice.name, choice.sellPrice))
    jump stall

label market:
    narrator "You are at the market"
    jump start

label crafting:
    narrator "You are at the crafting bench"
    jump start

label stats:
    narrator "You are viewing stats"
    jump start
