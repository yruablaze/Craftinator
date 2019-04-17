# The script of the game goes in this file.

init python:
    import random
    import forest
    from player import currentPlayer
    import items
    import craft
    from shop import Shop
    import clock as clock

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mel")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene Crossroads

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    menu:
        "Visit the Forest":
            m "The forest is an excellent spot to find items!"
            jump forest
        "Go to the Field":
            jump field
        "Go to the Barn":
            jump barn
        "Open a Vendor Stall":
            jump stall
        "Visit the Market":
            jump market
        "Go to the Crafting Bench":
            jump crafting
        "View Stats":
            jump stats
        "Quit":
            # This ends the game.
            return

label forest:
    m "Where do you want to look?"

    menu:
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
        m( "You found a %s!" % item.name )
        currentPlayer.inventory.add(item)
        currentPlayer.addCount(1)
        currentPlayer.expGain(1)
    jump forest

label field:
    m "You are in the field"
    jump start

label barn:
    m "You are in the barn"
    jump start

label stall:
    m "You are at the vendor stall"
    jump start

label market:
    m "You are at the market"
    jump start

label crafting:
    m "You are at the crafting bench"
    jump start

label stats:
    m "You are viewing stats"
    jump start