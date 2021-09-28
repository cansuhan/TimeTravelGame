#TEAM BLUE GAME - Gameintro & Egypt files
from os import system, name
import sys, time
import random

from ben import dino_level,clear, typewrite
from Connor import chapter_4
from egypt import ancient_egypt
from dave import campfire

dino_complete =False
egypt_complete = False
medival_complete = False
future_complete = False
inventory=[]


print("""\
          __________
         /________ /|
        |   XII , | |
        |     ,'  | |
        |IX  * III| |
        |     `.  | |
        |____VI___| |
        |    |    | |
        |    |    | |
        |   ( )   | |
        |         | | -|- | /` |/  -|- /\ /` |/
        |_TeamBlue__|  |  | \, |\   |  \/ \, |\.\
            \n""")

time.sleep(0.2)
player_name = (input("What is your name adventurer? ").upper().lower().capitalize().strip()) # capitalize and strip unnecessary characters in player name throughout the game
time.sleep(0.7)

clear() #clears all previous text
era_list = [ancient_egypt, dino_level, campfire, chapter_4]
def string_typewrite(string): # Using typewrite function for strings througout the game for the type writer effect
    global player_name
    for char in string:         # for each character in each line/string
        sys.stdout.write(char)  # print a single character, and keep the cursor there
        sys.stdout.flush()      # flush the buffer 
        time.sleep(0.03)        # wait 0.07 seconds for the type writer effect

string_typewrite(f"""\nWelcome to Timeless Adventures {player_name} \n
We hope you are ready to unfold your own adventure in the layers of time...\n""")
""
print("""
   ___               _   _              _    _ 
  / __| ___  ___  __| | | |   _  _  __ | |__| |
 | (_ |/ _ \/ _ \/ _` | | |__| || |/ _|| / /|_|
  \___|\___/\___/\__,_| |____|\_,_|\__||_\_\(_)
                                               
""")

time.sleep(3)

clear() #clears all previous text

string_typewrite(f"""
{player_name}\n
You are taking your brother Jon to visit the \nMuseum of Natural History to see the dinosaurs.\n\n""")

time.sleep(0.5)
print("""        
                 _ _.-'`-._ _
                ;.'________'.;
     _________n.[____________].n_________
    |""_""_""_""||==||==||==||""_""_""_""|
    |  |  |  |  ||==||==||==||  |  |  |  |
    |  |  |  |  ||LI||LI||LI||  |  |  |  |
    |.. .. .. ..||..||..||..||.. .. .. ..|
    |LI LI LI LI||LI||LI||LI||LI LI LI LI|
 ,,;;,;;;,;;;,;;;,;;;,;;;,;;;,;;,;;;,;;;,;;,,
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
""")
time.sleep(0.8)

string_typewrite("""You and Jon take the interactive dinosaur tour at the museum.\n
The roaring T-Rex captivates you, so you turn to Jon to see his reaction.\n
However, you panic as he is nowhere to be seen!\n
You spot a door slightly ajar just to your right, with a sign which reads - """)

print("""
 __      __ _    ___  _  _  ___  _  _   ___  _ 
 \ \    / //_\  | _ \| \| ||_ _|| \| | / __|| |
  \ \/\/ // _ \ |   /| .` | | | | .` || (_ ||_|
   \_/\_//_/ \_\|_|_\|_|\_||___||_|\_| \___|(_)
                                               
    THIS DOOR MUST BE KEPT LOCKED AT ALL TIMES!
   """)

time.sleep(3.5)
clear() #clears all previous text

print("""
-========== .
|  __  __  ||
| |  ||  | ||
| |  ||  | ||
| |__||__| |--
|  __  __()|\ 
| |  ||  | +|
| |  ||  | ||
| |  ||  | ||
| |__||__| ||
|__________|. 
\n""")
time.sleep(0.3)
string_typewrite("You push the door open further to have a better look inside.\n\n")
time.sleep(1)

string_typewrite("""There is no sign of your brother.\n
A tall man with white hair is bent over a computer, which is hooked up to a strange-looking clock.\n
He turns to you and says, “I’m Dr Sands. You must be the volunteer. Are you ready to go through with the experiment?” \n
“What experiment?” you ask. \n
“To travel through time, of course!” he replies. \n
You’ve always been intrigued by time travel! You could just do it!\n
But you need to find your brother!\n\n
""")


def make_choice():
    global player_name 
    string_typewrite(f"Make your choice {player_name}: \n")
    time.sleep(0.5)
    
    while True:
        try:
            selection = int(input("\n1. I’m in Dr Sands, I want to travel time let’s do it!.\n2. I’d better stay and look for my brother.\n\nYour decision: \n"))
        except ValueError:
            invalid_option()
            continue
        else:
            break
    if selection == 1:
        option_1()
    elif selection == 2:
        option_2()
    

#prompt user to say yes 
def option_2():
    print(f"\nThis is an adventure game {player_name}!")
    string_typewrite("""
You really want to pass on this once in a lifetime opportunity to travel time?\n
Please take a second to think it over and make the rigt choice!
\n""")
    time.sleep(2.2)
    return make_choice()

#Invalid input prompt to use in the game throughout
def invalid_option():
    time.sleep(0.5)
    print(f"\nThis is not a valid option {player_name}. \nPlease make your choice by entering the correct digits\n")
    time.sleep(1.5)

#The choice to start the game
def option_1():
    string_typewrite("""
Before you can even reply to Dr Sands, you hear pounding footsteps.\n
You turn to see your brother racing toward the time portal.\n
“JON!” you cry out. “You can’t go in there!” \n
“You’re not the boss of me!” Jon exclaims as he jumps into the time portal.\n
Dr Sands shouts “He went before I made the final settings! If you don’t bring him back, he’ll disappear into timelessness forever!”\n
“But what time period did he jump into? you ask.\n
“Your guess is as good as mine. Here, take the time-turner to get back to the present" Dr Sands replies.\n
He hands you a device that looks like a pocket watch.\n
You need to decide which era you are going to!
\n\n""")
    choose_era()


def choose_era():
    global future_complete, dino_complete, egypt_complete, medival_complete, era_list 
    
    string_typewrite(f"Where are you travelling in time?\n\nMake your choice {player_name}: \n")
    
    while True:
        try:
            select_era = int(input("""\n1. Ancient Egypt\n2. Prehistory Cretaceous Period\n3. The Medival Period\n4. The Distant Future\n5. Let the game decide for you\n\nYour decision: \n"""))
        except ValueError:
            invalid_option()
            continue
        else:
            break
    
    if select_era == 1:
        if ancient_egypt in era_list:
            ancient_egypt()
            egypt_complete=True
            era_list.remove(ancient_egypt)
        else:
            typewrite("You've already been here")
            choose_era()

    elif select_era == 2:
        if dino_level in era_list:
            dino_level()
            dino_complete =True
            era_list.remove(dino_level)
        else:
            typewrite("You've already been here")
            choose_era()
    elif select_era == 3:
        if campfire in era_list:
            campfire()
            medival_complete =True
            era_list.remove(campfire)
        else:
            typewrite("You've already been here")
            choose_era()

    elif select_era == 4:
        if chapter_4 in era_list:
            chapter_4(player_name)
            future_complete=True
            era_list.remove(chapter_4)
            typewrite("As you return hoping that your brother wasn't in that part of time\nYour brother? appears next to you.\nYou're not sure how he managed to get back alone but he always was good with gadgets")
        else:
            typewrite("You've already been here")
            choose_era()
    elif select_era == 5:    #make a random selection for the player
        
        era = random.choice(era_list)
        era_list.remove(era)
        if era==chapter_4:
            era(player_name)
        else:
            era()
    else:
        invalid_option()
        choose_era()
    if era_list!=[]:
        typewrite(f"You've returned from your journey with your brother, Dr Sands is waiting for you.\nHmm he says, my readings say there is still \n{len(era_list)} of your brother still out there in various times.\n")
        typewrite("Will you go and find them?\n1.Yes\n2.No")
        again=input()
        while True:
            
            if again not in("1","2") :
                typewrite("please enter 1 or 2")
                again=input()
            elif again=="1":
                choose_era()
                break
            else:
                
                typewrite(f"You've decided {4-len(era_list)} of your brother is enough, time to go home.")
                break


    else:
        typewrite(f"You've found them all {player_name}! Now you have 4 of your brother Jon!...\nYou think you may regret this decision.")
        print('''                                                                    
 _____ _           _          ___                _         _         
|_   _| |_ ___ ___| |_ ___   |  _|___ ___    ___| |___ _ _|_|___ ___ 
  | | |   | .'|   | '_|_ -|  |  _| . |  _|  | . | | .'| | | |   | . |
  |_| |_|_|__,|_|_|_,_|___|  |_| |___|_|    |  _|_|__,|_  |_|_|_|_  |
                                            |_|       |___|     |___|''')
        time.sleep(2)
        exit()
        
make_choice()

print('''                                                                    
 _____ _           _          ___                _         _         
|_   _| |_ ___ ___| |_ ___   |  _|___ ___    ___| |___ _ _|_|___ ___ 
  | | |   | .'|   | '_|_ -|  |  _| . |  _|  | . | | .'| | | |   | . |
  |_| |_|_|__,|_|_|_,_|___|  |_| |___|_|    |  _|_|__,|_  |_|_|_|_  |
                                            |_|       |___|     |___|''')
time.sleep(2)

# print (future_complete)
# print (dino_complete)
# print (egypt_complete)
