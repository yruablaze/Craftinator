# The script of the game goes in this file.

init python:
    import random
    import forest
    from player import currentPlayer
    import items
    import craft
    from shop import shop
    from clock import gameTime

    def showTime(a, at):
        d= Text("It is %s %s in Year %s." % gameTime.checkClock())
        return d, None

    def showMoney(a, at):
        d= Text("Gold : %s" % currentPlayer.money)
        return d, None

    timeIncrease = 10

image showingTime = DynamicDisplayable(showTime)
image showingMoney = DynamicDisplayable(showMoney)

# Photo by Holly Mandarich on Unsplash
image Crossroads = "Crossroads.jpg"
# Photo by Imat Bagja Gumilar on Unsplash
image Forest = "Forest.jpg"
# Photo by Benjamin Davies on Unsplash
image Field = "Field.jpg"
# Photo by Pedro Lastra on Unsplash
image Barn = "Barn.jpg"
# Photo by Sid Verma on Unsplash
image Stall = "Stall.jpg"
# Photo by William J Simpson on Unsplash
image Market = "Market.jpg"
# Photo by NeONBRAND on Unsplash
image Crafting = "Crafting.jpg"
# Photo by Kiwihug on Unsplash
image Stats = "Stats.jpg"


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

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #M - don't need this yet
    #show eileen happy

    menu:
        "Visit the Forest":
            scene Forest
            show showingTime at left
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
            show showingTime at left
            show showingMoney at top
            jump stall
        "Visit the Market":
            scene Market
            show showingMoney at top
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
        currentPlayer.inventory.addItem(item)
        currentPlayer.addCount(timeIncrease)
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
        sellableItems = currentPlayer.inventory.getSellable()
        menu_items = []
        menu_items.append(("Choose an item to sell:", None))
        for item in sellableItems:
            menu_items.append(("Sell one %s for %s gold. You have %s." % (item.name, item.sellPrice, item.quantity), item))
        menu_items.append(("Nevermind", "Nevermind"))
        # each tuple in menu_items is (text_displayed_in_menu, object_returned_upon_selection)
        choice = menu(menu_items)
        if (choice == "Nevermind"):
            renpy.jump("start")
        else:
            currentPlayer.inventory.removeItem(choice)
            currentPlayer.money += choice.sellPrice
            narrator ("You sold 1 %s for %s gold" % (choice.name, choice.sellPrice))
    jump stall

label market:
    python:
        buyableItems = shop.getBuyable()
label market2:
    narrator "You are at the market" (interact=False)
    python:
        cash = currentPlayer.money
        menu_items = []
        menu_items.append(("Choose an item to buy:", None))
        for item in buyableItems:
            if cash >= item.buyPrice:
                menu_items.append(("Buy a %s for %s gold." % (item.name, item.buyPrice), item))
            else:
                menu_items.append(("Buy a %s for %s gold." % (item.name, item.buyPrice), None))
        menu_items.append(("Nevermind", "Nevermind"))
        # each tuple in menu_items is (text_displayed_in_menu, object_returned_upon_selection)
        choice = menu(menu_items)
        if (choice == "Nevermind"):
            renpy.jump("start")
        else:
            buyableItems.remove(choice)
            currentPlayer.inventory.addItem(choice)
            currentPlayer.money -= choice.buyPrice
            narrator ("You bought 1 %s for %s gold" % (choice.name, choice.buyPrice))
    jump market2

label crafting:
    narrator "You are at the crafting bench" (interact=False)
    python:
        menu_items = []
        menu_items.append(("Choose an item to craft:", None))
        for recipe in craft.recipes.values():
            componentsFound = True
            componentsText = ""
            for component, quantity in recipe.components.iteritems():
                componentsText += ("%s %s, " % (quantity, component))
                if currentPlayer.inventory.containsType(component, quantity) == False:
                    componentsFound = False
            if componentsFound == True:
                menu_items.append(("Make a %s with: %s" % (recipe.product, componentsText[0:-2]), recipe))
        menu_items.append(("View all recipes", "View all"))
        menu_items.append(("Nevermind", "Nevermind"))
        # each tuple in menu_items is (text_displayed_in_menu, object_returned_upon_selection)
        choice = menu(menu_items)
        if (choice == "Nevermind"):
            renpy.jump("start")
        elif(choice == "View all"):
            renpy.jump("recipeList")
        else:
            currentPlayer.inventory.addItem(items.Item(choice.product))
            for component, quantity in choice.components.iteritems():
                currentPlayer.inventory.removeItem(items.Item(component), quantity)
            currentPlayer.expGain(4)
            currentPlayer.addCount(timeIncrease)
            narrator ("You made a %s!" % (choice.product.name))
    jump crafting

label recipeList:
    python:
        # number of recipes to show per page
        showPerPage = 6
        currentPage = 0
        recipesList = craft.recipes.values()

label recipeSubList:
    python:
        menu_items = []
        startSubList = currentPage*showPerPage
        endSubList = (currentPage+1)*showPerPage

        # only add the current page of recipes to the menu
        recipesSubList = recipesList[startSubList:endSubList]
        for recipe in recipesSubList:
            componentsText = ""
            for component, quantity in recipe.components.iteritems():
                componentsText += ("%s %s, " % (quantity, component))
            menu_items.append((" %s needs: %s" % (recipe.product, componentsText[0:-2]), None))

        #Show prev button on pages after the first page
        if (currentPage > 0):
            menu_items.append(("< Prev", "prev"))

        #Show next button on pages before the last page
        if ( endSubList < len(recipesList) ):
            menu_items.append(("Next >", "next"))

        menu_items.append(("Done", "Nevermind"))

        # each tuple in menu_items is (text_displayed_in_menu, object_returned_upon_selection)
        choice = menu(menu_items)

        if (choice == "Nevermind"):
            renpy.jump("crafting")
        elif (choice == "prev"):
            currentPage -= 1
            renpy.jump("recipeSubList")
        elif (choice == "next"):
            currentPage += 1
            renpy.jump("recipeSubList")

label stats:
    #$ narrator ("You bought 1 %s for %s gold" % ("placeholder", "10,000"))
    narrator "Here is the status page"  (interact=False)
    python:
        menu_items = []
        menu_items.append(("Level %s with %s exp" % (currentPlayer.lvl, currentPlayer.exp), None))
        menu_items.append(("%s exp required to level up" % (currentPlayer.lvlUp), None))
        menu_items.append(("%s actions per day, %s used today" % (currentPlayer.actions, currentPlayer.actionCount), None))
        menu_items.append(("%s Gold" % (currentPlayer.money), None))

        menu_items.append(("View Inventory", "View all"))
        menu_items.append(("Nevermind", "Nevermind"))

        # each tuple in menu_items is (text_displayed_in_menu, object_returned_upon_selection)
        choice = menu(menu_items)
        if (choice == "Nevermind"):
            renpy.jump("start")
        elif(choice == "View all"):
            renpy.jump("statsInvDisplay")
    jump start

label statsInvDisplay:
    python:
        # number of recipes to show per page
        showPerPage = 6
        currentPage = 0
        inventoryList = currentPlayer.inventory.getList()

label subStatsInvDisplay:
    python:
        menu_items = []
        startSubList = currentPage*showPerPage
        endSubList = (currentPage+1)*showPerPage

        # only add the current page of recipes to the menu
        invSubList = inventoryList[startSubList:endSubList]
        for item in inventoryList:
            menu_items.append(("%s : %s" % (item.name, item.quantity), None))

        #Show prev button on pages after the first page
        if (currentPage > 0):
            menu_items.append(("< Prev", "prev"))

        #Show next button on pages before the last page
        if ( endSubList < len(inventoryList) ):
            menu_items.append(("Next >", "next"))

        menu_items.append(("Done", "Nevermind"))

        # each tuple in menu_items is (text_displayed_in_menu, object_returned_upon_selection)
        choice = menu(menu_items)

        if (choice == "Nevermind"):
            renpy.jump("stats")
        elif (choice == "prev"):
            currentPage -= 1
            renpy.jump("invSubList")
        elif (choice == "next"):
            currentPage += 1
            renpy.jump("invSubList")
