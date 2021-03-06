﻿""" The script of the game goes in this file. """
init python:
    import random
    import forest
    from player import currentPlayer
    import items
    import craft
    import shop
    from clock import gameTime

    def display_time(a, at):
        d = Text("It is %s %s in Year %s." % gameTime.check_clock())
        return d, None

    def display_money(a, at):
        d = Text("Gold : %s" % currentPlayer.money)
        return d, None

    time_increase = 10

    """STATS"""
    items_crafted = 0
    items_found = 0
    items_sold = 0
    money_made = 0

    TEXT_COLOR = "#339900"

    # number of recipes to show per page
    SHOW_PER_PAGE = 6

image TIME_DISPLAY = DynamicDisplayable(display_time)
image MONEY_DISPLAY = DynamicDisplayable(display_money)


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

# define m = Character("Mel")

# The game starts here.


label start:
    scene Crossroads
    show TIME_DISPLAY at left

    menu:
        "Visit the Forest":
            scene Forest
            show TIME_DISPLAY at left
            # the narrator line should run once
            # narrator "The forest is an excellent spot to find items!"
            jump forest
        "Go to the Field":
            scene Field
            jump field
        "Go to the Barn":
            scene Barn
            jump barn
        "Open a Vendor Stall":
            scene Stall
            show TIME_DISPLAY at left
            show MONEY_DISPLAY at top
            jump stall
        "Visit the Market":
            scene Market
            show MONEY_DISPLAY at top
            jump market
        "Go to the Crafting Bench":
            scene Crafting
            jump crafting
        "View Stats":
            scene Stats
            show TIME_DISPLAY at left
            jump stats
        "Quit":
            return


label forest:
    menu:
        narrator "Where do you want to look?"
        "In a wild field":
            # example of single line python script (using dollar sign)
            $ item = forest.LOCATIONS["WILD"].search()
            jump foundSomething
        "Under the Sunny Brook Bridge":
            $ item = forest.LOCATIONS["BRIDGE"].search()
            jump foundSomething
        "By the Forester's Hut":
            $ item = forest.LOCATIONS["HUT"].search()
            jump foundSomething
        "Around Pea Bog":
            $ item = forest.LOCATIONS["BOG"].search()
            jump foundSomething
        "By the old mine":
            $ item = forest.LOCATIONS["MINE"].search()
            jump foundSomething
        "Go back Home":
            jump start


label foundSomething:
    python:
        narrator( "You found a %s!" % item.name )
        currentPlayer.inventory.add_item(item)
        currentPlayer.add_action_count(time_increase)
        currentPlayer.exp_gain(1)
        items_found += 1
    jump forest


label field:
    narrator "You are in the field"
    $ craft.find_recipe("glass")
    jump start


label barn:
    narrator "You are in the barn"
    jump start


label stall:
    narrator "You are at the vendor stall" (interact=False)
    python:
        choice=None
        sellable_items = currentPlayer.inventory.get_sellable()
        menu_items = []
        menu_items.append(("Choose an item to sell:", None))
        for item in sellable_items:
            menu_items.append(("Sell %s for %s gold. You have %s." % (item.name, item.sell_price, item.quantity), item))
        menu_items.append(("Nevermind", "Nevermind"))
        # each tuple in menu_items is (text_displayed_in_menu, object_returned_upon_selection)
        choice = menu(menu_items)
        if (choice == "Nevermind"):
            renpy.jump("start")
        else:
            currentPlayer.inventory.remove_item(choice)
            currentPlayer.money += choice.sell_price
            items_sold += 1
            money_made += choice.sell_price 
            narrator ("You sold %s for %s gold" % (choice.name, choice.sell_price))
    jump stall


label market:
    python:
        buyable_items = shop.get_buyable()


label market2:
    narrator "You are at the market" (interact=False)
    python:
        cash = currentPlayer.money
        menu_items = []
        menu_items.append(("Choose an item to buy:", None))
        for item in buyable_items:
            if cash >= item.buy_price:
                menu_items.append(("Buy %s for %s gold." % (item.name, item.buy_price), item))
            else:
                menu_items.append(("Buy %s for %s gold." % (item.name, item.buy_price), None))
        menu_items.append(("Nevermind", "Nevermind"))
        # each tuple in menu_items is (text_displayed_in_menu, object_returned_upon_selection)
        choice = menu(menu_items)
        if (choice == "Nevermind"):
            renpy.jump("start")
        else:
            buyable_items.remove(choice)
            currentPlayer.inventory.add_item(choice)
            currentPlayer.money -= choice.buy_price
            narrator ("You bought %s for %s gold" % (choice.name, choice.buy_price))
    jump market2


label crafting:
    narrator "You are at the crafting bench" (interact=False)
    python:
        menu_items = []
        menu_items.append(("{color=%s}Choose an item to craft:{/color}" % (TEXT_COLOR), None))
        for recipe in craft.recipes.values():
            components_found = True
            components_text = ""
            for component, quantity in recipe.components.iteritems():
                components_text += ("%s %s, " % (quantity, component.name))
                if currentPlayer.inventory.contains_item(component, quantity) is False:
                    components_found = False
            if components_found is True:
                menu_items.append(("Make a %s with: %s" % (recipe.product.name, components_text[0:-2]), recipe))
        menu_items.append(("View all recipes", "View all"))
        menu_items.append(("Nevermind", "Nevermind"))
        # each tuple in menu_items is (text_displayed_in_menu, object_returned_upon_selection)
        choice = menu(menu_items)
        if (choice == "Nevermind"):
            renpy.jump("start")
        elif(choice == "View all"):
            renpy.jump("recipeList")
        else:
            currentPlayer.inventory.add_item(items.Item(choice.product))
            for component, quantity in choice.components.iteritems():
                currentPlayer.inventory.remove_item(items.Item(component), quantity)
            currentPlayer.exp_gain(4)
            currentPlayer.add_action_count(time_increase)
            items_crafted += 1
            narrator ("You made a %s!" % (choice.product.name))
    jump crafting


label recipeList:
    python:
        current_page = 0
        recipes_list = craft.recipes.values()


label recipeSubList:
    python:
        menu_items = []
        start_sub_list = current_page*SHOW_PER_PAGE
        end_sub_list = (current_page+1)*SHOW_PER_PAGE
        # only add the current page of recipes to the menu
        recipesSubList = recipes_list[start_sub_list:end_sub_list]
        for recipe in recipesSubList:
            components_text = ""
            for component, quantity in recipe.components.iteritems():
                components_text += ("%s %s, " % (quantity, component.name))
            menu_items.append((" %s needs: %s" % (recipe.product.name, components_text[0:-2]), None))
        # Show prev button on pages after the first page
        if (current_page > 0):
            menu_items.append(("< Prev", "prev"))
        # Show next button on pages before the last page
        if ( end_sub_list < len(recipes_list) ):
            menu_items.append(("Next >", "next"))
        menu_items.append(("Done", "Nevermind"))
        # each tuple in menu_items is (text_displayed_in_menu, object_returned_upon_selection)
        choice = menu(menu_items)
        if (choice == "Nevermind"):
            renpy.jump("crafting")
        elif (choice == "prev"):
            current_page -= 1
            renpy.jump("recipeSubList")
        elif (choice == "next"):
            current_page += 1
            renpy.jump("recipeSubList")


label stats:
    narrator "Here is the status page"  (interact = False)
    python:
        menu_items = []
        menu_items.append(("{color=%s}Level %s with %s exp{/color}" % (TEXT_COLOR, currentPlayer.lvl, currentPlayer.exp), None))
        menu_items.append(("{color=%s}%s exp required to level up{/color}" % (TEXT_COLOR, currentPlayer.lvl_up), None))
        menu_items.append(("{color=%s}%s actions per day, %s used today{/color}" % (TEXT_COLOR, currentPlayer.actions, currentPlayer.action_count), None))
        menu_items.append(("{color=%s}%s Gold{/color}" % (TEXT_COLOR, currentPlayer.money), None))
        menu_items.append(("View Inventory", "View all"))
        menu_items.append(("Nevermind", "Nevermind"))
        # each tuple in menu_items is (text_displayed_in_menu, object_returned_upon_selection)
        choice = menu(menu_items)
        if (choice == "Nevermind"):
            renpy.jump("start")
        elif(choice == "View all"):
            renpy.jump("statsInvDisplay")


label statsInvDisplay:
    python:
        current_page = 0
        inv_list = currentPlayer.inventory.get_list()


label subStatsInvDisplay:
    python:
        menu_items = []
        start_sub_list = current_page*SHOW_PER_PAGE
        end_sub_list = (current_page+1)*SHOW_PER_PAGE
        # only add the current page of recipes to the menu
        invSubList = inv_list[start_sub_list:end_sub_list]
        for item in invSubList:
            menu_items.append(("{color=%s}%s : %s{/color}" % (TEXT_COLOR, item.name, item.quantity), None))
        # Show prev button on pages after the first page
        if (current_page > 0):
            menu_items.append(("< Prev", "prev"))
        # Show next button on pages before the last page
        if (end_sub_list < len(inv_list)):
            menu_items.append(("Next >", "next"))
        menu_items.append(("Done", "Nevermind"))
        # each tuple in menu_items is (text_displayed_in_menu, object_returned_upon_selection)
        choice = menu(menu_items)
        if (choice == "Nevermind"):
            renpy.jump("stats")
        elif (choice == "prev"):
            current_page -= 1
            renpy.jump("subStatsInvDisplay")
        elif (choice == "next"):
            current_page += 1
            renpy.jump("subStatsInvDisplay")
