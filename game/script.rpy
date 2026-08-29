define p = Character("[povname]", color="#89cbfd")
define s = Character("Star Spirit", color="#f6db78")

label start:
    play music "the_mountain-dreamy-dreamy-music-508007.mp3"
    $ povname = renpy.input("Welcome! What is your name?", length = 32)
    $ povname = povname.strip()
    if not povname:
        $ povname = "You"
    scene bedroom with fade
    play music "atlasaudio-dream-518077.mp3"
    play sound "yawning-6096.mp3" volume 2.5
    p "Hoooaaah! Time to go to sleep..."
    stop music fadeout 2.0
    scene black with fade
    play sound "freesound_community-snoring-long-78149.mp3" fadein 2.0
    p "zzzzz..."
    pause 6.0
    scene ss with fade
    play sound "audiodollar-news-intro-news-background-477317.mp3"
    s "Hello, [povname]! WELCOME to the most exciting game of your life!"
    s "Welcome to... WOULD! YOU! RATHER?!"
    s "Are you ready to make some nearly impossible decisions and plan your perfect day?"
    menu:
            "Yes! Let's do this!":
                s "Great! Let's get started!"
                jump continue

            "Heck no! Who even are you?":
                s "Well I'm your guide. And also you're forced to play so..."
                jump continue
    label continue:
        scene 1 with fade
        s "Would you rather wake up at a beach house..."
        play sound "dragon-studio-ocean-waves-376898.mp3"
        s "... or a cottage in the mountains?"
        play sound "freesound_community-birds-chirping-75156.mp3"
        menu:
            "Beach house":
                s "The sound of the waves are so calming. Excellent choice!"
                jump next
            "Cottage in the mountains":
                s "The view must be stunning! Great chhoice!"
                jump next
    label next:
        scene 2 with fade
        s "Would you rather spend your evening in a city where everyone know your name..."
        play sound "freesound_community-dark-evil-piano-32205.mp3"
        s "... or in a forest where you can hear someone following you?"
        play sound "freesound_community-going-on-a-forest-road-gravel-and-grass-6404.mp3"
        menu:
            "City":
                s "Feels nice to be known huh?"
                jump yo
            "Forest":
                s "Don't worry, no one's here.."
                jump yo

    label yo:
        scene 3 with fade
        s "Would you rather spend your afternoon visiting a new place..."
        s "... or reliving a moment from the past?"
        menu:
            "New place":
                s "Yeah! Somewhere you've been curious about for a while."
                jump hi
            "Past moment":
                s "Some moments just need to be relived!"
                jump hi
    label hi:
        scene 4 with fade
        s "Would you rather spend your morning at a amusement park where everything is free..."
        play sound "freesound_community-amusement-park-attraction-ride-32531.mp3"
        s "... or in a giant version of your favourite video game?"
        play sound "cartoon_music-level-up-retro-video-game-533840.mp3"
        menu:
            "Amusement park":
                s "Great! Amusement parks are the best! The tickets are pretty expensive though."
                jump bro
            "Video game":
                s "That sounds so fun and cool! Basically a VR game!"
                jump bro

    label bro:
        scene 5 with fade
        play music "universfield-horror-background-atmosphere-156462.mp3"
        s "Would you rather wake up and return to the real world where you’ll never get a day like this..."
        s "... or stay here forever and live your perfect day again tomorrow?"
        menu:
            "Wake up":
                jump wake
            "Stay here forever":
                jump stay
    label wake:
        scene black with fade
        s "you'll forget everything once you wake up."
        play music "the_mountain-dreamy-dreamy-music-508007.mp3"
        scene wall with fade
        p "IT'S MORNING! What's that on my wall"
        play sound "freesound_community-gasp-7117.mp3"
        p "OH! It's a STAR SPIRIT!"
        return

    label stay:
        scene black with fade
        s "Now, let’s do it all again."

    return
