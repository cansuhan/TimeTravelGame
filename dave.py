import sys, time, os    #sys allows printing each individual character, time to delay the characters appearing, os to clear the screen
import random
player_name=0
medieval_complete = False

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
                dragon()
            elif selection == 2:
                string_typewrite ("You have chosen not to continue\n Thanks for playing\n")
                sys.exit()
            else:
                print ("You have made an invalid choice, try again.")

def campfire(): 
    global player_name
    global string_typewrite

    string_typewrite ("You enter the mountains it's so dark, you look around and can't see a thing in front of you")
    print (""" 
                 .-.    .  _   *     _   .
              *          /   \     ((       _/ \       *    .
            _    .   .--'\/\_ \     `      /    \  *    ___
        *  / \_    _/ ^      \/\'__        /\/\  /\  __/   \ *
          /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .
     .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _
        /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ |
       /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^ |
      /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `. 
    @&8jgs@@ @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%
    @88:::&(&8&&8:::::%&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::
    `::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8:::::'
     `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.
    """)

    selection = None

    while selection not in (1,2):
        try:
            
            selection = int(input("Do you want to build a campire?\n1. Yes\n2. No\n"))
        except ValueError:
            print("\nPLEASE INPUT YOUR ANSWER BY PRESSING 1 OR 2\n")
            continue
        else:
            if selection == 1:
                print ("""
                                &&.
            )                .,.&&
           (  (              \=__/
               )             ,'-'.
         (    (  ,,      _.__|/ /|
          ) /\ -((------((_|___/ |
        (  // | (`'      ((  `'--|
      _ -.;_/ \\--._      \\ \-._/.
     (_;-// | \ \-'.\    <_,\_\`--'|
     ( `.__ _  ___,')      <_,-'__,'
      `'(_ )_)(_)_)'  )'''""")
                string_typewrite ("You light a fire, a brief reprieve from the bitter cold.\n")
                dragon()
            elif selection == 2:
                string_typewrite ("You choose to freeze death, not a great choice but it's one you made\n")
                game_over()
            else:
                print ("You have made an invalid choice, try again.")

def dragon():
    global player_name
    global string_typewrite

    string_typewrite ("A gigantic dragon appears!")
    print ("""
        '''   (  )   /\   _                 (     
        \ |  (  \ ( \.(               )                      _____
     \  \ \  `  `   ) \             (  ___                 / _   |
    (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
    - .-               \+  ;          (  O                           \____
                            )        \_____________  `              \  /
    (__                +- .( -'.- <. - _  VVVVVVV VV V\                 \/
    (_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
    .    /./.+-  . .- /  +--  - .     \______________//_              \_______
    (__ ' /x  / x _/ (                                  \___'          \     /
    , x / ( '  . / .  /                                      |           \   /
        /  /  _/ /    +                                      /              \/
    '  (__/                                             /                  \ """)

    selection = None

    while selection not in (1,2):
        try:
            
            selection = int(input("Do you want to fight the dragon?\n1. Yes\n2. No\n"))
        except ValueError:
            print("\nPLEASE INPUT YOUR ANSWER BY PRESSING 1 OR 2\n")
            continue
        else:
            if selection == 1:
                string_typewrite ("You fight the dragon\n")
                tower()
            elif selection == 2:
                string_typewrite ("The dragon fights you\n")
                game_over()
            else:
                print ("You have made an invalid choice, try again.")

def tower():
    global player_name
    global string_typewrite

    string_typewrite ("you carry walking deeper in to the mountains, you come across a tower!")
    print("""
    '''                                             |>>>
                                                |
                                            _  _|_  _
                                           |;|_|;|_|;|
                                           \\.    .  /
                                            \\:  .  /
                                             ||:   |
                                             ||:.  |
                                             ||:  .|
                                             ||:   |       \,/
                                             ||: , |            
                                             ||:   |
                                             ||: . |
              __                            _||_   |
     ____--`~    '--~~__            __ ----~    ~`---,              ___
    -~--~                   ~---__ ,--~'                  ~~----_____-~'   `~----~~ '''
    """)
    selection = None

    while selection not in (1,2):
        try:
            
            selection = int(input("You hear cries from the top would you like to save your brother jon and fight the ogre?\n1. Yes\n2. No\n"))
        except ValueError:
            print("\nPLEASE INPUT YOUR ANSWER BY PRESSING 1 OR 2\n")
            continue
        else:
            if selection == 1:
                string_typewrite ("Congratulations you saved your brother jon move on to the next chapter\n")
                medieval_complete = True
                #Join up with the rest of the code
            elif selection == 2:
                string_typewrite ("You dont fight and you dont save your brother and dont retrive the time crystal\n")
                game_over()
            else:
                print ("You have made an invalid choice, try again.")
