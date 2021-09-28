#TEAM BLUE GAME
from os import system, name
import sys, time
import random

def string_typewrite(string): 
    for char in string:         # for each character in each line/string
        sys.stdout.write(char)  # print a single character, and keep the cursor there
        sys.stdout.flush()      # flush the buffer 
        time.sleep(0.03)        # wait 0.07 seconds for the type writer effect

def invalid_option():
    time.sleep(0.5)
    print(f"\nThis is not a valid option. \nPlease make your choice by entering digits 1 or 2\n")
    time.sleep(1.5)

def game_over():
    print("""
   ___   _   __  __ ___    _____   _____ ___ 
  / __| /_\ |  \/  | __|  / _ \ \ / / __| _ |
 | (_ |/ _ \| |\/| | _|  | (_) \ V /| _||   /
  \___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_`.
                                             
    """)
    string_typewrite("You have failed.\n\n")
    time.sleep(3)
    string_typewrite("\nLuckily your time-turner will get you back to your previous checkpoint.\n")
    time.sleep(3)

egypt_complete = False

def fight_flight():
    while True:
        try:
            soldier_duel = int(input("\n1. Face the soldier. \n2. Make a run for it and jump into the river on your left.\n\nYour decision: \n"))
        except ValueError:
            invalid_option()
            continue
        else:
            break
    if soldier_duel == 1:
        fight_soldier()
    elif soldier_duel == 2:
        make_run()
    else:
        invalid_option()
        return fight_flight()

def make_run():
        string_typewrite("""\nYou decide to jump into the river.\n\nHowever, you are not alone, two crocodiles emerge from the water.\n\n""")
        time.sleep(1)
        game_over()
        # time.sleep(2)
        # string_typewrite("\nLuckily your time-turner will get you back to your previous checkpoint.")
        # time.sleep(2)
        return fight_flight()

def fight_soldier():
        string_typewrite("""\n
You decide to face the soldier.\n
“No one enters the Pharoah’s temple unless they can meet the challenge!” he shouts.\n
“What challenge?” you ask.\n
“You must fight me!” he exclaims.\n
“The loser will become food for the Pharoah’s crocodiles in the river.” he adds.\n
The soldier pulls two weapons from his saddle.\n
        """)

#fight_flight()

def choose_weapon():
    while True:
        try:
            select_weapon = int(input("\n1. Sword \n2. Wooden Staff \n\nYour decision: \n"))
        except ValueError:
            invalid_option()
            continue
        else:
            break
    if select_weapon == 1:
        weapon_1()
    elif select_weapon == 2:
        weapon_2()
    else:
        invalid_option()
        return choose_weapon()

def weapon_1():
    print("""
       ^
      |.|
      |||
      |||
      |||
      |||
      |||
    __|||_
    `-----'
      | |  ))
      | | ,)
     |___|.
""")
    string_typewrite("""
The soldier strikes you with his spear, you dodge and manage to block him with your sword.\n
He stumbles and falls into the river.\n
You defeated the soldier!\n
You proceed towards the temple.\n
 """)
    time.sleep(1)
    string_typewrite("""
You enter a winding, narrow corridor. Colourful art line the walls.\n
The corridor turns and twists but doesn’t seem to lead anywhere.\n
From somewhere up ahead you hear a human scream.\n
Maybe you should get out of here right now.\n
But what if it was Jon?\n\n""")
    time.sleep(2)
    return

def weapon_2():
    string_typewrite("""\nYou strike with your wooden staff.\n
However, the spear hits your staff and it breaks in half.\n
You chose the wrong weapon.\n
    """)
    game_over()
    # time.sleep(2)
    # string_typewrite("\Your time-turner will get you back to your previous checkpoint in a moment.")
    time.sleep(2)
    return choose_weapon()

#choose_weapon()

def choose_now():
    time.sleep(0.5)
    while True:
        try:
            select_weapon = int(input("\n1. Follow the Sound \n2. Go Back \n\nYour decision: \n"))
        except ValueError:
            invalid_option()
            continue
        else:
            break
    if select_weapon == 1:
        go_ahead()
    elif select_weapon == 2:
        run_back()
    else:
        invalid_option()
        return choose_now()

def run_back():
    string_typewrite("""
You decide to run back.\n
You fall onto the angry soldier's path again.\n
He lifts you up and throws you into the river.\n
You try the button on the time-turner.\n
You find yourself back in the lab with Dr. Sands.\n
"You made it back!" Dr. Sands greets you. "How did it go?"\n
You’re about to answer when you remember Jon.\n
Oh, no! You left your brother in the past!
\n\n""")
    time.sleep(1)
    game_over()
    time.sleep(1)
    return choose_now()

def go_ahead():
    string_typewrite("""
You decide to follow the sound.\n
It leads to an opening, you see an enormous gate beyond it.\n
You walk towards it.\n
\n""")
    time.sleep(1)
    print("""
                              .sSSSSSs.
                              sSS=""^^^"s
                  /\       /  / \_\_\/_/_)
                 /';;     /| |/\/.-. .-.|
                / \;|    /. \,S'  -   - |
               / -.;|    | '.SS     _|  ;
              ; '-.;\,   |'-.SS\   __  /S
              | _  ';\.   |' SSS\_____/SS
              |  '- ';.\  \_SSS[_____]SS
              \ '--.-';;\. __SSS/\    SSS
               \  .--' ';;'.=SSS` \_\_SSS
                `._ .-'` _';;..=.=.=.\.=.|
                   ;-._-'  _.;\.=.=.=.|.=|
         ,     _.-'    `"=._  ;\=.=__/__/
         )\ .'`   __        ".;|.=.=.=./
         (_\   .-`  '.   |    \/=.=.=/`
          / \         \-,|     |.--'|
         /  \`,       //  \    | |  |
         ( (__) )  _.-'--,  \   | |  '--,
         ;----' -'--,__)))  \  '--, __)))
         \_________)))       \___)))
""")
    string_typewrite("""
A Sphinx appears right in front of the gate! \n
"Hold there mortal! Are you worthy enough to pass the trial of the gods?" She says.\n
"Answer me this and I shall open the temple gate for you..."\n
""")
    time.sleep(1)
    return riddle()

def riddle():
    string_typewrite("\nAt night they come without being fetched, and by day they are lost without being stolen.\n\n")

    while True:
        try:
            riddle_answer = input ("Please think carefully before you enter your answer here: \n").lower().strip()
        except ValueError:
            invalid_option()
            continue
        else:
            break
    if riddle_answer == "stars" or riddle_answer == "star" or riddle_answer == "the stars":
        time.sleep(2)
        string_typewrite("\nThe Sphinx just disappears into thin air.")
        #as one of its feathers fall onto the sand, it writes -\n\nObtain Pharaoh's ankh from the throne room,  then you shall find your brother.\n")
        time.sleep(1)
        string_typewrite("\nThe gate suddendly opens and you enter.\n")
        return throne_room()
    else:
        string_typewrite("""\nThe Sphinx laughs at your answer!\n
Suddenly a hole appears under you and you fall.\n
You try to get the time-turner on your neck.\n
It breaks and slips from your hand!\n
    """)
    game_over()
    time.sleep(2)
    return riddle()

def throne_room():
    print("""
      __.-=-.            .-=-.__
      --<(_)>            <(_)>--
    *.__.'|                |'.__.* 
""")
    string_typewrite("""You find yourself in a long throne room.\n
There are two thrones in the distance, one is smaller.\n
That’s when you notice who’s sitting on the small throne next to the Pharaoh.\n\n
JON!\n\n
“I’ve been looking all over for you!” you run to him. “We’ve got to get back you can’t stay —”\n
“Silence!” the Pharaoh bellows.\n
“No one speaks to my son without permission!”\n
The Pharaoh orders the soldier at your side to throw you out.\n
“Oh great Pharaoh I come bearing gifts for your son, our future king” you say.\n
You take the time-turner off and hold it out.\n
You both have to be touching the device to go back to present. This has to be done quick.\n
As you pass the device to Jon, you press the button.\n\n""")
    time.sleep(2)
    string_typewrite("""You are back in Dr Sand's lab!\n
You saved you brother Time Traveller!
    """)

egypt_complete = True

def ancient_egypt():
    global egypt_complete
    time.sleep(1)
    print("""
                              \^/
           L L               /   \               L L
        __/|/|_             /  .  \             _|\|\__
        _| [_[_\           /     .-\           /_]_] |_
       __\  __`-\_____    /    .    \    _____/-`__  /__
      ___] /=@>  _   {>  /-.         \  <}   _  <@=\ [___
     ____/     /` `--/  /      .      \  \--` `\     \____
    ____/  \____/`-._> /               \ <_.-`\____/  \____
   ____/    /__/      /-._     .   _.-  \      \__\    \____
  ____/    /__/      /         .         \      \__\    \____
  ___/_  _/__/      /          .          \      \__\_  _\____
 \__/_ ``_|_/      /      -._  .        _.-\      \_|_`` _\___/
   /__`-`__\      <_         `-;           _>      /__`-`__
      `-`           `-._       ;       _.-`           `-`
                        `-._   ;   _.-`
                            `-._.-`
    """)
    time.sleep(1)
    string_typewrite("An enormous stone monument stretches towards the sky.\n\n")
    time.sleep(2)
    string_typewrite("The sound of thundering hooves breaks the silence.\n\nA soldier charges towards you in a chariot with a spear in his hand.\n")
    string_typewrite("\nAre you going to fight or flight?\n\nMake your choice: \n")
    fight_flight()
    string_typewrite("""\nChoose your weapon: \n""")
    choose_weapon()
    string_typewrite("""\nMake your choice: \n""")
    choose_now()

