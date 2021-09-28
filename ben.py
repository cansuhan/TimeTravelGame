from time import sleep
from os import system, name
import sys  

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



from datetime import datetime
from random import choices, randint
#Jurassic journey
inventory =[]
crush = False
def quick_time_event(ans,time):
  
  t1 = datetime.today()
  given_ans=input().lower()
  t2 = datetime.now()
  dif =t2-t1
  dif=dif.seconds
  if given_ans!=ans or dif>time:
    crushed()
  else:
    return dif


def decision(accepted):
  while True:
    ans=input().lower()
    if ans in accepted:
      return ans
    print("Sorry, that wasn't a valid input")
    sleep(0.5)
    print("Please enter the number of the option you want to choose")
def crushed():
  clear()
  global crush
  crush = True
  typewrite("Oof, looks like you got crushed by a big foot\nWould you like to try again?\n(1.Yes\n2.No)\n")
  if decision(["1","2"])=="1":
    
    brachio_time()
  else:
    game_over()


def inv_check():#might be used later
  if inventory ==[]:
    print("Your inventory is empty")
  else:
    for i in inventory:
      print(i)

def typewrite(words,pause=0.03):
  words+='\n'
  for char in words:
    sleep(pause)
    sys.stdout.write(char)
    sys.stdout.flush()
def brachio_time(): #Wooo dinosaurs
  clear()
  global crush
  crush=False
  print('''
              __       __
             /'_)     /'_)     ###  
      .-^^^-/ /.-^^^-/ /     #####o#   
   __/       //       /       #\|/#
  <__.|_|-|_|  |_|-|_|          |  \n''')
  typewrite("They don't seem to have noticed you yet. They look like herbivores and you're brother always loved dinosaurs, do you:\n1. Approach them\n2. Leave them be and try another place\n")
  ans1= decision(["1","2"])
  if ans1 =="1":
    typewrite("You: 1. Quietly approach \n2. Run at the creatures waving your arms like an insane person")
    ans2 = decision(["1","2"])

    if ans2 == "1":
      typewrite("You head towards the dinosaurs hoping your brother would do the same\nThey look like brontosaurus...or was it diploducus?...apatasaurus?\n\n*Thunk*\nyou look up dazed to see the scaled leg of one of the Brachiosaurus \n(Brachiosaurus that was it!)\nIt doesn't look very impressed. In fact it is rearing a foot up to stomp on you.\nYou should:\n1.Dodge!\n2.ATTACK!")
      ans3 = decision(["1","2"])
      if ans3 =="2":
        crushed()
      else:
        typewrite("You see a mass of scales that probably weighs tonnes coming towards you and attempt to dodge it.\n\n(This will be a test of your reflexes, type the word within the time limit to avoid certain doom.\n(not case sensitive)")
        typewrite("3\n2\n1\nGO",0.8)
        print("Type \"dinosaur\" in less than 10 seconds")
        secs = quick_time_event("dinosaur",10)
      
        typewrite(f"You took {secs} seconds, well done")
        typewrite("You nimbly dodge between the legs of the creature but you aren't out of danger yet.\nSomething catches your attention on the ground next to you")
        sleep(1)
        print("Type the name of the type of dinosaur trying to crush you. You have 7 seconds.")
        secs = quick_time_event("brachiosaurus",7)
        if not crush:
          typewrite(f"You took {secs} seconds, well done")
          sleep(1)
          typewrite("You pick up the small object and manage to slip out\nYou've added a small toy to your inventory")
          sleep(1)
          typewrite("Now you're sure Jon was there at some point and have a better idea of the direction he might have gone")
          inventory.append("dinoclue1")
          sleep(0.5)
        
                
    else:
      crushed()
  else:
    return False

def do_maths():
  sleep(1)
  
  print('''
      /|  
    ?/ |15
    /__|    
     8''')
  ans= input()
  count=1
  while ans!="17" and count<3:
    typewrite(f"Incorrect\nYou have {3-count} more attempts")
    sleep(0.5)
    clear()
    print('''
      /|  
    ?/ |15
    /__|    
     8''')
    
    ans= input()
    count+=1
  if ans =="17":
    return True

def dino_level():
  global crush
  clear()
  typewrite("You feel unsteady on your feet and a little nauseous. But after getting your footing you open your eyes to see a wide open field filled with huge creatures grazing\n")
  sleep(1)
  brachio_time()
  if not crush:
    return tyrano_skip()
def found_bro():
  typewrite("You found him well done!")
  sleep(1)
  typewrite("Jon is just wandering the plains, you're surprised that he didn't run into anything\n\nYou activate your time turner and bring the 2 of you home.")
  return True
def tyrano_skip():
  clear()
  typewrite("You wander away from the dinosaurs in search of less lizardy life.\nAfter some walking you find some small footprints, they are definitely in the shape of a shoe\nHowever they disapear quickly as due to the appearance of much larger prints that seem to overlap them")
  sleep(0.5)
  if "dinoclue1" in inventory:
    typewrite("Judging from these few prints and what you found earlier, you think you could figure out exactly where he's gone.\nIt'll just take a little trig\n")
    typewrite("Write the length of the hypotenuse to figure out where your brother has gone.\nYou get 3 attempts")
    if do_maths():
      typewrite("You think you've figured it out, no need to follow the huge prints now, you can head directly to him...Unless\n1.Follow the giant prints anyway\n2.Go find your brother")
      no_trex=decision(["1","2"])
      if no_trex=="1":
        return tyrano_time()
      else:
        return found_bro()
    else:
      return tyrano_time()
  else:
    return tyrano_time()

def eaten():
  global crush
  typewrite("OM NOM NOM\nYou've been eaten by the T-rex\n 1.Try again\n2.Quit")
  crush =True
  if decision(["1","2"]) ==1:
    typewrite("Traveling back to the last safe point")
    sleep(1)
    tyrano_time()
  else:
    game_over()
def game_over():
    print("""
   ___   _   __  __ ___    _____   _____ ___ 
  / __| /_\ |  \/  | __|  / _ \ \ / / __| _ |
 | (_ |/ _ \| |\/| | _|  | (_) \ V /| _||   /
  \___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_`.
                                             
    """)
    sys.exit()
def tyrano_time():
  T2 = '''             .-=-==--==--.
       ..-=="        `.
     ,'       ,'0`)         \\
    :  (       `'"            `.__....____
    :       ,vv.-._   /    /               `---==-._
     \/\/\/VV ^ d88`;'    /                         `.
         ``  ^/d88P!'    /             ,              `._
            ^/    !'   ,.      ,      /                  "-,,__,,--'""""-.
           ^/    !'  ,'  \ . .(      (         _           )  ) ) ) ))_,-.\\
          ^(__ ,!',"'   ;:+.:%:a.     \:.. . ,'          )  )  ) ) ,"'    '
          ',,,'','     /o:::":%:%-.    \:.:.:         .    )  ) _,'
           """'       ;':::'' `+%\%\%\._  \%:%|         ;.). _,-""
                  ,-='_.-'      ``:%::)  )%:|        /:._,"
                 (/(/"           ," ,'_,'%\%\%:       (_,'
                                (  (//(`.___;        \\
                                 \     \    `         |
                                  `.    `.   `.        :
                                    \. . .\    : . . . :
                                     \. . .:    `.. . .:
                                / ,;:%\%\%:        ;:%::
                              //;,--""-.`\  ,=--':%:%:\\'''


  T1='''             .-=-==--==--.
        ..-=="  ,'o`)      `.
      ,'         `"'         \\
      :  (                     `.__....______
      :       ,vv.-._   /    /               `---==-._
      |\/\/\/VV ^    `;'    /                         `.
       \\   ``  ^    !'    /             ,              `.___
        """"""""""""""""\'!\'   ,.      ,      /           """"""""-,,__,,--""""-.
                        \ . .(      (         _                  )  ) ) ) ))_,-.\\
                          ;:+.:%:a.     \:.. . ,'              )  )  ) ) ,"'    '
                          /o:::":%:%-.    \:.:.:         .     )  ) _,'
                        ;':::'' `+%\%\%\._  \%:%|         ;.). _,-""
                    ,-='_.-'      ``:%::)  )%:|        /:._,"
                  (/(/"           ," ,'_,'%\%\%:       (_,'
                                  (  (//(`.___;        \\
                                  \     \    `         `
                                    `.    `.   `.       :
                                      \. . .\    : . . . :
                                      \. . .:     `. . .:
                                    /;:%\%\%:        ;:%::
                                  //;,--""-.`\  ,=--':%:%:\\'''
  Trex =[T1,T2]
  global crush
  crush=False
  typewrite("You follow the large 3 toed footprints since they seemed to be going in the same direction as your brother\nMore or less\nYou hear a large roar in the distance.")
  sleep(1)
  typewrite("\nCresting a nearby hill\n",0.1)
  sleep(0.5)
  typewrite("A huge mouth full of teeth attached to a dinosaur anyone would recognise.\nHopefully the T-rex hasn't seen you though...\n")
  clear()
  for i in range(5):
    clear()
    print(Trex[(i+1)%2])
    sleep(0.5)
  clear()
  typewrite("Do you want to \n1.Run away or \n2.Try to fight?")
  fight = decision(["1","2"])
  if fight==1:
    eaten()
  else:
    typewrite("You turn and run as the T-rex bears down on you.\nIn you can see two possible escape routes \n1.Climb a tree to get out of it's reach\n2.Hide in a cave too short for it to enter",0.01)
    if decision(["1","2"]) =="1":
      return tree_climb()
    else:
      cave()
def cave():
  print("Not done yet")
def tree_climb():
  typewrite("The Tyranosaurus is bearing down on you as you begin to try and climb the tree\nEnter'l's and'r's in the same order that you see branches on the \\left\\ or /right/ on the tree looking up from the bottom.\nWe'll do an example.")
  print('''      
       |     ___/
       |    |
       |    |
  \\____|    |
       |    |''')
  typewrite("In this example, you'd want to enter 'lr'")
  if input().lower()!="lr":
    while True:
      a = 0.2
      typewrite("Not sure how or why you'd get that wrong...\nTry typing 'l' 'r'.\nNo spaces or anything\nI believe in you",a)
      typed = input()
      if typed=='lr':
        break
      a*=2
      if a>1:
        typewrite("You've brought this on yourself, it'll only grow slower") 
  typewrite("Well done")
  typewrite("If there are no branches to grab, you'll have to just press Enter with no input\nTo launch yourself higher and try and grab onto something.\nDo your best to not be eaten!")
  sleep(0.5)
  typewrite("Here we go then",0.2)
  for k in range(3):
    tree= rand_tree()
    ans=branch_writer(tree)
    if input()!=ans:
      eaten()
      break 
    elif k ==1:
      typewrite("You're making your way up the tree but still aren't safe yet")
    elif k==2:
      typewrite("You've managed to scramble to the top of the tree!\nYou're out of the reach of the T-rex's jaws but it was closer than you'd have liked\nThe Tyranosaurus tries to reach you for a few minutes, then tries to push the tree to no avail.\nAfter a short while it simply looks dejected and leaves\nDeciding that it can probably find an easier meal.")
      sleep(0.5)
      typewrite("After a few more minutes you see a familiar figure from your high vantage point.")
      return found_bro()
    
def branch_writer(tree):
  ans=''
  if tree[0]==1:
    ans+='l'
  if tree[2]== 1:
    ans+='r'
  if tree[1]==1:
    ans+="l"
  if tree[3]==1:
    ans+='r'
  return ans
def rand_tree():
  branch_l={0:"     |",1:"_\\____"}
  branch_r={0:"|    ",1:"___/_"}
  branches=[randint(0,1),randint(0,1),randint(0,1),randint(0,1)]
  print(f"     |    {branch_r[branches[3]]}")
  print(f"{branch_l[branches[1]]}    |")
  print(f"     |   ={branch_r[branches[2]]}")
  print(f"{branch_l[branches[0]]}    |")
  return branches

def cave():
  typewrite("You see a cave with an entrance too small for the T-rex\n It doesn't go very deep but you think it'll be safer than climbing a tree.")
  typewrite("You rush inside and try to stay low, the trex slams it's body against the entrance and you can feel the walls shaking")
  typewrite("Maybe you should have climbed that tree...",0.2)
  typewrite("The cave collapses on you")
  
  typewrite("Let's go back a step")
  sleep(1)  
  clear()
  tyrano_time()

