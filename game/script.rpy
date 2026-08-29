# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[povname]")


# The game starts here.

label start:
    
    "Welcome! What's your name?"
    $ povname = renpy.input("Enter here")
    return
