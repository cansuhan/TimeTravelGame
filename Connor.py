import sys, time, os    #sys allows printing each individual character, time to delay the characters appearing, os to clear the screen
import random
from os import system, name
#Chapter 4, future/near future setting
future_complete = False
player_name=0

os.system("cls") #clears all previous text

def string_typewrite(string): # Using string_typewrite funtion for strings througout the game for the type writer effect
    global player_name
    for char in string:         # for each character in each line/string
        sys.stdout.write(char)  # print a single character, and keep the cursor there
        sys.stdout.flush()      # flush the buffer 
        time.sleep(0.03)        # wait 0.07 seconds for the type writer effect

def game_over():
    global string_typewrite
    global player_name

    selection = None

    while selection not in (1,2):
        try:
            selection = int(input("Do you want to continue?\n1. YES\n2. NO"))
        except ValueError:
            print("\nPLEASE INPUT YOUR ANSWER BY PRESSING 1 OR 2\n")
            continue
        else:
            if selection == 1:
                string_typewrite ("You have chosen continue\n Good luck\n")
                chapter_4(player_name)
            elif selection == 2:
                string_typewrite ("You have chosen not to continue\n Thanks for playing\n")
                sys.exit()
            else:
                print ("You have made an invalid choice, try again.")

def path_A(): #Path A leads towards path_A_chall or path_A_fail
    global player_name
    global string_typewrite

    string_typewrite ("""
    You travel along the walkway into the megaplex which you're able to enter with relative ease, given the size you would have expected guards but for all you know this could be some sort of future supermarket.
    You notice what looks to be some sort of storage room and decide to have a little poke around. On a wall you notice what seems like a monocle, labelled 'Power Reader'.
    You remove it from the wall and put it up to your eye, you can see readouts of nearby power sources presumably useful for the engineers of the facility.
    After looking around you decide you have 2 options ahead of you.
    \n\n""")

    selection = None
    while selection not in (1,2):
        try:
            selection = int(input("1. Head to the largest power source you can see, so large your new toy has trouble displaying it\n2. Head towards a much closer cluster of smaller power signals\n"))
        except ValueError:
            print("\nPLEASE INPUT YOUR ANSWER BY PRESSING 1 OR 2\n")
            continue
        else:
            if selection == 1:
                string_typewrite ("You begin the journey towards the large power source, deeper into the facility.\n")
                path_A_chall()
            elif selection == 2:
                string_typewrite ("You head off in the direction of the cluster of signals, doing your best to navigate through this labyrinth\n")
                path_A_fail()
            else:
                print ("You have made an invalid choice, try again.")
              
def path_B(): #Path B leads towards path_B_chall or path_B_fail
    global player_name
    global string_typewrite
    
    string_typewrite ("""
    The cargo conveyor belt pulls into what looks like an incredibly large storage room, but strangely no one is removing the cargo, there is no sign of employee's anywhere.
    You wonder how long the cargo has been on this perpetual loop... until you realise you need to jump off the conveyor before it leaves the structure again.\n
    Once inside you wander around looking for anything interesting you can use to help you navigate, a map, a sign... anything at all.
    You find an office with what looks to be tools...or weapons? Who knows. One thing in particular catches your eye though.
    Hung on the wall is a 'Power Reader' presumably used by the engineers to monitor the building, it looks almost like a monocle.
    As you don the power reader you notice that you have a couple of options on where to go
    \n""")

    #Enter via conveyor, leave via option A or B

    selection = None
    while selection not in (1,2):
        try:
            selection = int(input("1. Head to the largest power source you can see, so large your new toy has trouble displaying it.\n2. Head towards a much closer cluster of smaller power signals\n"))
        except ValueError:
            print("\nPLEASE INPUT YOUR ANSWER BY PRESSING 1 OR 2\n")
            continue
        else:
            if selection == 1:
                string_typewrite ("You begin the journey towards the large power source deeper in the facility\n")
                path_B_chall()
            elif selection == 2:
                string_typewrite ("You head off in the direction of the cluster of signals, doing your best to navigate through this labyrinth\n")
                path_B_fail()
            else:
                print ("You have made an invalid choice, try again.")

def path_A_chall(): #Find the thing challenge, you can't actually fail this one.... not really a challenge.
    global string_typewrite
    string_typewrite ("As you enter the room you notice what looks to be a robot looking your way")
    print ("""
         ,     ,
        (\____/)
         (_oo_)
           (O)
         __||__    \)
      []/______\[] /
      / \______/ \/
     /    |__|
    (\   /____\ 
    """)
    string_typewrite (f"""
    The robot bids you welcome; 'Greetings fellow human, it's been a long time since I've seen one of our kind in these parts. I am Hugh Man, pleased to meet you'
    'if you're looking to enter deeper into this facility you've come to the right place, unfortunately the door is jammed and I don't have a replacement part to fix it'\n
    \x1B[3mYou look around at the debris of what looks to be several robots of all sorts of shapes and sizes and wonder how he doesn't have the parts to fix the door with all this scrap\x1B[0m\n
    Somewhat nervously you reply back; \x1B[3mHello Hugh Man, I am {player_name}, if I help you find the parts amongst this wreckage can you get this door open?\x1B[0m\n
    Hugh Man looks at you their 'eyes' seem to light up. 'If you find it, I can fix it! find me a spare radial polar flinger and I'll have this cleared in no time'\n
    \x1B[3mRadial polar finger, got it!\x1B[0m - you reply, in a very obvious attempt to pretend you know what you're talking about. \x1B[3mRemind me Hugh, what does one look like again?\x1B[0m\n
    'It's a circular board that slots into the panel on the door, it'll have flashing lights on it if that helps' he replies, your bluff seems to have worked or more like gone unnoticed.\n   
    \x1B[3mYou scan the room looking for where to begin:\x1B[0m
    \n""")

    selection = None
    while selection != (2):
        try:
            selection = int(input("1. Search Hugh Man, he's clearly hiding something\n2. Underneath a rather large and threatening looking robot\n3. Keep checking the same area in the hope it eventually turns up\n4. You see a robotic hand clutching something interesting\n"))
        except ValueError:
            print("\nPLEASE INPUT YOUR ANSWER BY PRESSING 1 TO 4\n")
            continue
        else:
            if selection == 2:
                string_typewrite ("\nYou find an item that looks like it matches the description and pass it over to Hugh Man, he gives you a nod and sets about getting the door open.\n")
                string_typewrite ("\nSeveral minutes of awkward silence later, the door opens revealing an elevator platform, you step on and the floor slowly fades away.")
                string_typewrite ("\nOnce your brain and stomach get over the fact you're stood on a now translucent flooring, you look back to notice Hugh has disappeared\n\n")
                return path_merge()
            else:
                string_typewrite ("You don't find what you're looking for, it must be at one of the other 3 options.\n")
    
def path_B_chall(): #Enter the correct password challenge, 3 guesses then you die
    
    string_typewrite("""
    On your way towards the large energy reading you notice you're barred from entry by a barrier of red light
    the light seems to intermittently go out and luckily seems to follow a predictable pattern, but first you decide you should test it.\n

    \x1B[3mYou throw something from your pocket deliberately at the barrier while it's active\x1B[0m \n

    the object vaporises instantly, the stakes just got a lot higher... but without power there's no getting home.

    You brave the jump as the barrier goes down! Success!... you think for a second.
    The room is lit up by red lights, the barrier holds steady... You're trapped. 2 large weapon systems drop from the ceiling.

    You notice a terminal blinking, you move towards it. 4 buttons display heavily corrupted text.
    1. MY@?#@L$
    2. C0$$0&
    3. A#T#V#T#
    4. DE@£?|^ATE
    """)

    #you trigger some sort of security system upon arrival, you need to input the correct value to survive the challenge. 
    retry = 3
    selection = None
    while retry > 0:
        try:
            selection = int (input("\nWhich button do you press?\n"))
        except ValueError:
            print ("\nPLEASE INPUT YOUR ANSWER BY PRESSING 1 TO 4\n")
            continue
        else:
            if selection == 4:
                print ("\nYou have chosen correct\n")
                string_typewrite ("The red lights turn off, the barriers go down and finally, you can breathe.\n")
                string_typewrite ("A large door opens up, revealing an elevator platform, you step in and hope this is where you need to be. \n")
                return path_merge()
        
            elif retry == 1 and selection != 4:
                retry-=1
                string_typewrite(f"\nThe screen flashes red, you chose the wrong one it seems, you have {retry} number of attempts left")
                string_typewrite(f"\nAs you press the last button.... and the last thing you hear is the mechanical whir of the weapons systems starting up")
                game_over()

            else: 
                retry -=1
                string_typewrite(f"\nThe screen flashes red, you chose the wrong one it seems, you have {retry} number of attempts left")

def path_A_fail(): #Path_A_fail leads to death or loops back into path_A_chall  
    global player_name
    global string_typewrite
    
    string_typewrite("""
    You arrive in what appears to be some sort of armoury, there's body suits displayed along the walls with an accompanying assortment of weapons.\n  
    \x1B[3mWhere is everybody? Surely this stuff wouldn't be just left unguarded\x1B[0m - you can't help but mutter to yourself\n
    It get's even stranger when upon closer inspection you realise the layers of dust over everything, this armoury hasn't been used in a very long time.\n
    \x1B[3mBEEP BEEP BEEP\x1B[0m\n
    Thankfully the beeps of the power reader get you back on track and draw your eyes to a container under the display, inside the container are 6 metallic orbs.\n
    \x1B[3mWell these are definitely what I'm looking for, funky looking batteries they have in the future though\x1B[0m\n
    As you pick up one of the orbs you hear the whir of it coming to life followed by it emitting a blue glow, the glow is getting stronger and stronger
    You have a gut feeling something bad is about to happen, you clearly activated this device to do something and you need to make a snap decision.
    \n\n""")

    selection = None
    while selection not in (1,2):
        try:
            selection = int(input("1. Hold on to it and hope for the best\n2. Throw the orb as far away from you as you are able and take cover.\n"))
        except ValueError:
            print("\nPLEASE INPUT YOUR ANSWER BY PRESSING 1 OR 2\n")
            continue
        else:
            if selection == 1:
                string_typewrite ("You hold on to the orb as it becomes increasingly bright in your hands, \x1B[3mI think I regret this....\x1B[0m \n")
                game_over()
            elif selection == 2:
                string_typewrite ("From your cover point you hear what sounds like a pop and then a vaguely eletrical crack. You aren't sure what would have happened if you held it but you're glad you didn't. You continue onwards, from now on wary to touch metallic orbs.\n")
                path_A_chall()
            else:
                print ("You have made an invalid choice, try again.")

def path_B_fail(): #Path_B_fail leads to death or loops back into path_B_chall
    global player_name
    global string_typewrite

    string_typewrite ("You follow the power reader directions and find a room guarded by a robot!")
    print(""")   
                 ___
                |_|_|
                |_|_|             _____
                |_|_|    ____    |*_*_*|
      _______   _\__\___/ __ \____|_|_   _______
     / ____  |=|      \  <_+>  /      |=|  ____ |
     ~|    |\|=|======\\______//======|=|/|    |~
      |_   |    \      |      |      /    |    |
       \==-|     \     |  2D  |     /     |----|~~/
       |   |      |    |      |    |      |____/~/
       |   |       \____\____/____/      /    / /
       |   |         {----------}       /____/ /
       |___|        /~~~~~~~~~~~~\     |_/~|_|/
        \_/        |/~~~~~||~~~~~\|     /__|z
        | |         |    ||||    |     (/|| \)
        | |        /     |  |     \       \\
        |_|        |     |  |     |
                   |_____|  |_____|
                   (_____)  (_____)
                   |     |  |     |
                   |     |  |     |
                   |/~~~\|  |/~~~\|
                   /|___|\  /|___||
                  <_______><_______>""")

    string_typewrite("""              
    'HALT MEATBAG, ONLY AUTHORISED PERSONNEL BEYOND THIS POINT!'\n
    \x1B[3mYou notice a sign saying Restricted Access, engineers only.\x1B[0m\n
    \x1B[3mI'm new here and haven't been given security clearance yet, I was told to meet my superior through here\x1B[0m - You attempt a pretty obvious bluff but hope robots aren't the brightest\n
    'I'VE HEARD OF NO NEW HIRES, VERY WELL I'LL LET YOU PASS....IF YOU ANSWER THIS SIMPLE QUESTION.'
    'WHEN WOULD YOU USE AN ION FRAGMENTOR'
    \n\n""")

    #B's fail state room.

    selection = None
    while selection not in (1,2):
        try:
            selection = int(input("1. erm, that's, erm....\x1B[3mYou attempt to make a run for it\x1B[0m\n2. Well obviously when you wanna fragment some Ions.\n"))
        except ValueError:
            print("\nPLEASE INPUT YOUR ANSWER BY PRESSING 1 OR 2\n")
            continue
        else:
            if selection == 2:
                string_typewrite ("'THAT ONE IS ON ME FOR SETTING THE BAR SO LOW, VERY WELL YOU MAY PASS BUT I'LL BE WATCHING YOU MEATBAG'\n")
                string_typewrite ("You decide to proceed towards the large energy reading, over staying your welcome here seems unwise.\n")
                path_B_chall()
            elif selection == 1:
                string_typewrite ("A truly unwise option when you think about, I mean look at the guy, he's got all sorts of weapons. The robot opens fire without hesitation.\n")
                game_over()
            else:
                print ("You have made an invalid choice, try again.")

def path_merge(): #Path_merge is the connecting point for A and B, leads towards merge_fail or path_end.
    global player_name
    global string_typewrite
 
    string_typewrite ("""
    After the elevator platform comes to a stop you look around to view a room on such a scale you struggle to believe you're actually still indoors, the chamber is connected by a spiderweb of walkways over a seemingly endless drop below.
    Ahead of you is a main walkway flanked by large pillars of light stretching up from the depths, the large power source you've been following looks to be down that route.
    While taking in the room you also notice a terminal that could shed some light on your current location.
    \n""")

    #This path collects path A and B, then sends you towards death or the end.

    selection = None
    while selection not in (1,2):
        try:
            selection = int(input("1. Do you want to continue straight ahead towards the large power source?\n2. Do you want to investigate the terminal?\n"))
        except ValueError:
            print("\nPLEASE INPUT YOUR ANSWER BY PRESSING 1 OR 2\n")
            continue
        else:
            if selection == 1:
                string_typewrite ("You follow the main walkway, taking in the spectacle around you and hoping no surprises await you.\n")
                path_end()
            elif selection == 2:
                string_typewrite ("You walk over to the terminal.\n")
                merge_fail()
            else:
                print ("You have made an invalid choice, try again.")

def merge_fail(): #merge_fail brances off path_merge you either die or move on to the finale, by this point i was utterly done with coming up with creative ways to move the player about as you can see.
    global player_name
    global string_typewrite
    
    string_typewrite ("""
    You arrive at the terminal and unfortunately, you can't read the symbols the screen is displaying. One thing catches your eye though.
    A big, shiny, tantalising red button. You know you shouldn't press it, you know all the things around it that clearly look like warnings must actually be warnings
    But you can't stop thinking about it, what if this is actually the answer to all of lifes questions?...

    Do you press the Red Button?
    \n""")

    #1 last choice, by this point I was done writing story so it's a stupid choice.

    selection = None
    while selection not in (1,2):
        try:
            selection = int(input("1. Yes\n2. No\n"))
        except ValueError:
            print("\nPLEASE INPUT YOUR ANSWER BY PRESSING 1 OR 2\n")
            continue
        else:
            if selection == 2:
                string_typewrite ("You made the obviously correct choice, feeling vindicated with your clearly superior intelligence you proceed down the main walkway.\n")
                path_end()
            elif selection == 1:
                string_typewrite ("In the least surprising thing to possibly ever happen, that red button labelled with warnings was not in fact a good button\n")
                string_typewrite ("A countdown appears on the terminal, you activated the self destruct. You have 10 seconds to get your affairs in order...\n")
                game_over()
            else:
                print ("You have made an invalid choice, try again.\n")

def path_end(): #Final part of the story
    global player_name
    global string_typewrite
    global future_complete
    
    #End Point
    
    string_typewrite ("""
    You reach the end of the walkway, a large ciruclar platform surrounded by pillars of light, sitting in the centre is a terminal. 
    Above the terminal is a crystal seemingly suspended in midair, as you approach you relaise you've seen this crystal before.
    It was part of the time machine Dr. Sands was calibrating back before this adventure began.

    \x1B[3mI better get this crystal back to Dr. Sands, then we can find Jon\x1B[0m \n
    You remove the crystal and the giant beams of light suddenly dim, you feel rumbling beneath your feet, you hear loud bangs and explosions in the distance.
    It's as if you removed the heart of the structure and now it's dying, the rumbling gets more intense until suddenly... the floor gives way.
    As you fall into what feels like endless dark, you're desperately trying to use your time-turner to escape the grizzly end that awaits.
    In your panic you forgot the battery was drained, you hold the time-turner up to the crystal and feel the surge of power transferring between the objects.
    Just as you hear the bangs of debris hitting the floor you are sucked away, to where isn't important right now, anywhere but the next 10 seconds is the best place to be.
    \n\n""")
    
    #I know this story is bad but it was the best I could come up with in a few hours

    future_complete = True

def chapter_4(name): #The chapter start's here
    global time
    global player_name
    global string_typewrite
    player_name=name
    # time.sleep(0.5)
    # player_name = str(input("What is your name adventurer? ").strip(" ").capitalize()) # capitalize and strip unnecessary characters in player name throughout the game
    # time.sleep(0.5)

    string_typewrite(f"""
    You arrive on the other side of the portal amidst a sprawling metropolis of neon and steel, teeming with life or perhaps more approriately what seems like life.
    You knew you would encounter many strange and wonderful sights, given the ability to jump through time but you weren't expecting quite this strange.

    \x1B[3mYou look at your time-turner, "No juice" you mutter to yourself...just another problem for you to solve.\x1B[0m

    'Well {player_name} you've really got yourself into it this time, I need a power source and to look for any signs of Jon' you exclaim, resigned to face what's to come. Ahead you notice a fork in path.
    \n""") 

    #test to sec playername function

    selection = None
    while selection not in (1,2):
        try:
            selection = int(input("1. In front of you is large megaplex, it looks like you can clamber up on to a walk way that leads towards it. \n2. You also notice what seems to be a conveyor running under your location leading in to the complex that you could use \n"))
        except ValueError:
            print("\nPLEASE INPUT YOUR ANSWER BY PRESSING 1 OR 2\n")
            continue
        else:
            if selection == 1:
                string_typewrite ("You set off on the walkway towards the megaplex, taking in the vastness of the structure\n")
                path_A()
            elif selection == 2:
                string_typewrite ("You lower yourself onto the conveyor belt taking great care to avoid the various bits of cargo and not to fall off, as you're slowly whisked off towards your destination you can't help but wonder if you'll regret your choice.\n")
                path_B()
            else:
                print ("You have made an invalid choice, try again.")

# chapter_4()
# print (future_complete)
