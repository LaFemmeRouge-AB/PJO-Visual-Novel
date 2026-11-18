# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lauren")
define a = Character("Addy")
define ad = Character("Adrien")
define e = Character("Ellie")
define g = Character("Grace")
define m = Character("Moriah")
define o = Character("Oli")
define s = Character("Sandy")
define j = Character("Jasper")
define c = Character("Chiron")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene front camp

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Chiron

    # These display lines of dialogue.

    c "Hello! Welcome to Camp Halfblood."

    c "I'm sure your satyr has told you all about us. I recommend going to the Hermes cabin. Our Hermes head counselor can help you there."

    hide Chiron

    scene Hermes Beds

    m "Uh is there a head counselor here?"

    # Animation here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    a "Ow..."

    m "Hello?"

    a "Hey."

    menu welcome:
        "What to say?"
        "Are you the head counselor?":
            show Addy disheveled
            a "Yeah, sorry. Normally I'm a bit more... up. New camper?"
            menu:
                "What to say?"
                "Yeah? Chiron told me to come up":
                    show Addy Excited
                    a "Oh okay cool. Well, welcome to Camp Halfblood!"
                "Yeah...":
                    show Addy Excited
                    a "Great! Welcome to Camp Halfblood. Your home for the summer... or... more."
                        
        "Am I in the wrong place?":
            show Addy disheveled
            a "Well if you're looking for Hermes Cabin, you're right."
            menu:
                "What to say?"
                "Oh then yeah... are you the head counselor?":
                    show Addy Excited
                    a "Indeed I am. Welcome to Camp Halfblood!"
                "Yes, sorry, I'm new here.":
                    show Addy Excited
                    a "Oh then welcome! I'm the head counselor here, and probably your guide."



    a "If Chiron sent you here, I'm probably your guide!"

    a "You're in luck. I'm the best one. Don't tell anyone I said that..."
    
    show Addy Neutral

    a "My name is Addy. A daughter of Hermes. I stay here all year."

    #Add new person notif

    m "I'm Moriah!"
    menu:
        "What to say?"
        "How do I know what child of a god I am?":
            a "Well, a symbol or some sign from your parent will appear eventually."
            a "The gods used to never claim us, but a kid named Percy Jackson changed all that. You'll probably hear about him."
            a "Well, which parent do you have?"
            m "I live with my mom?"
            a "Then you can limit your choices to the dads."
            a "Mostly.... It's rare but I've seen some with two biological dads. Mostly Apollo."
            a "Do you have any hints for your cabin? Like powers?"
            menu: 
                "What to say?"
                "Not as far as I can tell":
                    a "Then you'll find who later."
                "My like senses and abilities are better than most peoples?":
                    a "That's most gods. Don't worry, he'll claim you eventually."          
            a "I learned mine when I challenged the old head counselor to a race and won."

        "Do I have to stay all year?":
            a "No, it's your choice. Most kids stay for the summer, it really depends on how monsters are attracted to you, or if you actually just want to stay."

        "Where do I stay?":
            a "Until you find your cabin, all unclaimed campers stay in Hermes!"
            a "There's not many, Percy Jackson made a deal with the gods, so most kids get claimed pretty quick."

        "Nothing":
            a "Good to meet you."

    a "If you follow me along here, I can show you the camp."

    scene Pavillion Front

    show Addy Guide

    a "This is the dining pavillion, each cabin has their table."

    scene Big House

    show Addy Guide
    
    a "This is where Chiron and our camp director lives, Dionysus."

    a "It's also the infirmary and war room."

    scene Combat Area

    show Addy Guide

    a "This is where our arena, climbing wall, and archery range area."

    scene Forest

    show Addy Guide

    a "Of course this is the forest. We have canoe lake and a beach a little past here."

    scene Stables

    show Addy Guide

    a "And here's the stables."

    scene Main Camp

    show Addy Guide

    a "And that's the end of our tour."

    a "We also have a forge, volleyball courts, armory, showers, ampitheater, and strawberry fields. Pretty much everything you can think of."

    a "Any questions?"

    menu:
        "Any questions?"
        "None":
            a "Awesome! I'll see you later then, you can go do whatever. Maybe look through the cabins?"

            a "We have a schedule everyday depending on your cabin. You can find the Hermes one on the board in our cabin."

        "What do we do everyday?":
            a "We have a schedule everyday depending on your cabin. You can find the Hermes one on the board in our cabin."

        "How can I get claimed as soon as possible?":
            a "Eager, okay! You just have to wait, do some activities or something. Go talk to other cabins."
    
    a "Au revoir mon ami. I'll catch you for dinner tonight? I gotta head to the wall."

    #Add the these choices will have consequences

    menu:
        "Go with her to the wall?":
            m "Can I come with?"
            a "For sure!"
            scene Wall
            #Add minigame.


        "Go to Apollo Cabin?":
            hide Addy
            scene Apollo Cabin


        "Explore the camp?":
            hide Addy


    # This ends the game.

    return
