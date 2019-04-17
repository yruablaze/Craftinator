# The script of the game goes in this file.

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
    # todo: port the runForestMenu code over to here from py.FarmGame
    m "You are in the forest"
    
    # just trying some simple python code to see how it works (dollar sign means python code)
    $ things = [ "blueberry", "blueberry", "apple", "apple", "vine", "onion", "ginger", "strawberry", "mint", "brown mushroom"]
    $ found = renpy.random.choice(things)
    $ firstChar = found[0] # get the first character of the found thing
    $ aOrAn = 'a'
    $ vowels = ['a', 'e', 'i', 'o', 'u'] #sometimes not y
    
    if ( firstChar in vowels ): # indefinite articles are harder than this, but let's pretend it's based on the letter and not the sound...
        $ aOrAn = 'an' 
    
    # displays some dialog using python
    $ m( "You found %s %s!" % (aOrAn, found) ) 
    
    jump start
    
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