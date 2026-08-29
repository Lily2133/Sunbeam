define p = Character("[povname]", color="#89cbfd")

label start:
    play music "the_mountain-dreamy-dreamy-music-508007.mp3"
    $ povname = renpy.input("Welcome! What is your name?", length = 32)
    $ povname = povname.strip()
    if not povname:
        $ povname = "You"
    p "Hi, I'm [povname]!"
    return