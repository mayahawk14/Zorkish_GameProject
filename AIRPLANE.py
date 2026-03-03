

#defines
from time import sleep
import OCEAN as biome2

import sys
import time

#for printing slow 
def slowprintt(text):
   for x in text:
     print(x, end='')
     sys.stdout.flush()
     sleep(0.5)
#for printing slow, quickly
def slowprint(text):
   for x in text:
     print(x, end='')
     sys.stdout.flush()
     sleep(0.05)
#for printing slow, with line skips after every letter
def slowprintfall(text):
   for x in text:
     print(x, end='\n')
     sys.stdout.flush()
     sleep(0.05)


#text for the seat
def seat():
  print("Congratulations!! You just won a trip to the Bahamas! A one-way ticket to the land of calm and serenity. No catch, free of charge.")
  sleep(3)
  print("You’re an hour into your plane ride to the vacation of your dreams. You can’t see anybody around. To your left is a window overlooking a view of the vast ocean, and to your right is the plane aisle. \n")

#text for entering the aisle
def aisle():
  print("Aisle \n You move into the aisle.")
  sleep(.8)
  print("From here, behind you, you can see all of the seats-- they're all empty. In front of you is a door with a sign that reads 'Plane Staff Only'. It's unlocked. A faint hum, like white noise, surrounds the room. \n")

#text for entering the cockpit
def cockpit():
  print("Cockpit \n You open the door.")
  sleep(.5)
  print("The cockpit is empty. It consists of two big seats and a long console of buttons. One button is bigger than the others, and glows a bright red. 'Autopilot'. \n")

#text for exiting the cockpit
def leavingCockpit():
  print("You exit the cockpit.")
  sleep(.5)
  print("Aisle \n You move into the aisle.")
  sleep(.8)
  print("From here, behind you, you can see all of the seats-- they're all empty. In front of you is a door with a sign that reads 'Plane Staff Only'. It's unlocked. A faint hum, like white noise, surrounds the room. \n")

#for moving down the aisle
def aisle2():
  print("You move down the aisle.")
  sleep(.8)
  print("The plane seats are scattered with people's belongings. A half-full baby bottle; a blanket; a tangled string of wired headphones... They were once here. I wonder where they went. \n")#from here, can only move forward and backward. i probably shouldn't be making it so creepy 
 # oo we should let them try to take the objects, dont let them or do idk
 #for moving down the aisle more
def aisle3():
  print("You move further down the aisle.")
  sleep(.8)
  print("A faint hum, like white noise, surrounds the room. \n")

#for entering the bathroom/snack zone
def bathroomSnack():
  print("You've reached the end of the aisle.")
  sleep(.8)
  print("To your left is what seems to be a small closet space, covered by one thin sheet of blue curtain. To your left is a door with a bathroom sign, the lock reads 'Occupied', but it's cracked open an inch. Directly in front of you is another curtain leading elsewhere; red, billowing. \n")

#for entering bathroom
def bathRoom():
  print("Bathroom \n You enter the bathroom.")
  sleep(.8)
  print("A small sink there. A toilet there. A vent by the cabinet with screws that might be a little loose. There is nothing special about the bathroom. \n")

def ventWay():
  slowprint("It's... a little dusty in here, but doable. If you can...")
  sleep(2)
  slowprint("... wriggle your way through- yeah, just like that. It's leading you SOMEWHERE, that's for sure.\n")
  sleep(3)
  slowprint("Ah, there's the light. We're nearing closer. \n\n")
  sleep(2)
  
def leaveBathroom():
  print("You exit the bathroom. \n")

#for entering snack room
def snackRoom():
  print("Snack Room \n You move the curtain.")
  sleep(.8)
  print("You pull open the curtain and reveal a small snack cart jostling against a cabinet. The cabinet has no doors, and displays an assortment of packaged nuts. \n") #no better snacks??

def leaveSnackroom():
  print("You exit the snack room.")
  sleep(.8)

#for entering first class
def firstClass():
  print("First Class \n You open the door that leads past the bathroom and the Snack room and enter the First Class section of the plane.")
  sleep(0.8)
  print("The room is much spacier than the last, with cushioned chairs that sit far apart from each other and a small table for each one. It seems unlikely that such a flight would take off without people in it... Other than you, of course. \n")
  sleep(0.8)
  print("A darkened hallway looms in the very back of the area. 'Exit' reads atop it, along with an arrow pointing down.")

#for entering staircase room
def stairCase():
  print("Staircase \n You move to the back of First class and follow the staircase.")
  sleep(.8)
  slowprint("It's dark in here. You can make out the steps of the spiral staircase- steep, that lead down... down... down...\n")

#for entering basement room
def startBasement():
  print("Basement \n You reach the end of the stairs and are met with a terribly dark hallway. It's the baggage area. Stacks and stacks of suitcases and bags line either side of the room, creating a narrow aisle. At the end of the aisle glows a reddish brightness. Where is it coming from? \n")

def midbasement():
  print("Basement \n You walk further down the basement hall. Suitcases surround you, held together by large nets. The red light gets brighter; closer. \n")

def basementExit():
  print("Basement Exit \n You've reached the exit of the baggage room. The gleaming red light is revealed to be an exit sign, with an arrow pointing to the door just below it. \n")



"""


# CONTINUE TEST

while True:
  dos = input("How do you like your eggs?: \n")
  if dos == "Scrambled":
    print("Yay that's right!!")
    break
  if dos == "Boiled":
    print("You're insane.")
    continue
  else :
    print("Dude what.")
    break


"""



print("Would you like to start the game?: \n")
choose = input()

def levelOne():
 inventory = "a mysterious thing in your pocket"
 while True:
   seat()
   while True:
     direction = input("You can move: N)  S)  E)  W)\n")
     if direction == "W":
       aisle()
       while True:
         direction = input()
         #first aisle options
         if direction == "N":
           cockpit()
           direction = input()
           #cockpit options
           if "leave" in direction:
              leavingCockpit()
              continue
           if "button" in direction:
              print("Well. You just died. \n")
              sleep(2.3)
              levelOne()
           else :
             print("You can't do that.")
             continue
         if direction == "open door":
           cockpit()
           direction = input()
           #cockpit options
           if "leave" in direction:
              leavingCockpit()
              continue
           if "button" in direction:
              print("Well. You just died. \n")
              sleep(2.3)
              levelOne()
           else :
              print("You can't do that")
              continue
              
         if direction == "S":
           aisle2()
           #has objects around
           while True:
             direction = input()
             #aisle 2 options
             if direction == "S":
               aisle3()
               while True:
                 direction = input()
                 #aisle 3 options
                 if direction == "S":
                   while True:
                     bathroomSnack()
                     direction = input()
                     #bathroom/snack hall options
                     if "door" in direction:
                       bathRoom()
                       sleep(.5)
                       direction = input("You should probably just leave... \n")
                       #bathroom options
                       if "leave" in direction:
                         leaveBathroom()
                         continue
                       if "vent" in direction:
                         print("Hmm... interesting choice. But proceed.")
                         sleep(1.7)
                         ventWay()
                         midbasement()
                         while True:
                           direction = input()
                           #further down basement options
                           if direction == "N":
                             basementExit()
                             while True:
                               direction = input("What will you do?: \n")
                               #further further down basement options
                               if "open" in direction:
                                 def fallingAIRPLANE():
                                   print("The force of the air pressure releasing from the plane sucks you out of the exit and, before you know it, you're flying!")
                                   sleep(3.5)
                                   slowprint("Well...\n\n")
                                   sleep(1)
                                   slowprintfall("falling...\n")
                                   sleep(2)
                                   slowprintt('...\n')
                                   sleep(2)
                                   slowprint("Falling for a while.\n")
                                   sleep(2)
                                   slowprint("This seems dangerous, especially without a parachute.\n\n")
                                   sleep(1.7)
                                   slowprint("Wouldn't it be great if we had some sort of large cloth to substitute as a parachute to ease our fall?\n\n")
                                   sleep(1.8)
                                   slowprint("Hmm...\n")
                                   sleep(1.8)
                                   did = input("Hey, did you pick up that blanket from the aisle earlier?\n")
                                   if did == "no":
                                     print("What!? Oh noo!! This landing is going to be a bit of a rocky one!\n\n")
                                   if did == "yes":
                                     save = input("Amazing! We can totally use that to land safely! Go ahead!:\n\n")
                                     if save == "use blanket":
                                       print("Good thinking! You pull out the blanket, wrap the corners around your hands, and use it as a parachute.\n")
                                       sleep(1.8)
                                       slowprint("It spreads out and catches in the air; your descent slows and...\n\n")
                                 fallingAIRPLANE()
                                 biome2.levelTwo()
                               else :
                                 print("\n It's too late.")
                                 continue
                           else :
                             print("You can't do that.")
                             continue
                       else :
                         print("I don't know that.")
                         continue
                     if "blue" in direction:
                       snackRoom()
                       direction = input()
                       # snack room options
                       if "leave" in direction:
                         #when i ask to leave the snackroom (specifically after picking up peanuts), it says I can't go there, then takes me to the end of the aisle
                          leaveSnackroom()
                          continue
                       if "nuts" or "peanuts" in direction:
                          print("Cool. A snack for your travels.")
                          inventory = inventory + "\n Pack of peanuts"
                          sleep(1)
                          print("Added to your inventory. To see inventory, enter 'i'")
                         
                          
                       if direction == "i":
                         print(inventory)
                          #^^ when I ask for inventory, it gives it to me, then says i cant go there, then takes me to the end of the aisle??
                       else :
                         print("I don't know that command.")
                         continue
                     if "red" in direction:
                       while True:
                         firstClass()
                         direction = input()
                         #first class options
                         if direction == "S":
                           while True:
                             stairCase()
                             direction = input()
                             #staircase options
                             if "down" in direction:
                               startBasement()
                               while True:
                                 direction = input()
                                 #basement options
                                 if direction == "N":
                                   midBasement()
                                   while True:
                                     direction = input()
                                     #further down basement options
                                     if direction == "N":
                                       basementExit()
                                       while True:
                                         direction = input()
                                         #further further down basement options
                                         if "open" in direction:
                                           def fallingAIRPLANE():
                                             print("The force of the air pressure releasing from the plane sucks you out of the exit and, before you know it, you're flying!")
                                             sleep(3.5)
                                             slowprint("Well...\n\n")
                                             sleep(1)
                                             slowprintfall("falling...\n")
                                             sleep(2)
                                             slowprintt('...\n')
                                             sleep(2)
                                             slowprint("Falling for a while.\n")
                                             sleep(2)
                                             slowprint("This seems dangerous, especially without a parachute.\n\n")
                                             sleep(1.7)
                                             slowprint("Wouldn't it be great if we had some sort of large cloth to substitute as a parachute to ease our fall?\n\n")
                                             sleep(1.8)
                                             slowprint("Hmm...\n")
                                             sleep(1.8)
                                             did = input("Hey, did you pick up that blanket from the aisle earlier?\n")
                                             if did == "no":
                                               print("What!? Oh noo!! This landing is going to be a bit of a rocky one!\n\n")
                                             if did == "yes":
                                               save = input("Amazing! We can totally use that to land safely! Go ahead!:\n\n")
                                               if save == "use blanket":
                                                 print("Good thinking! You pull out the blanket, wrap the corners around your hands, and use it as a parachute.\n")
                                                 sleep(1.8)
                                                 slowprint("It spreads out and catches in the air; your descent slows and...\n\n")
                                           fallingAIRPLANE()
                                           biome2.levelTwo()
                                         else :
                                           print("\n It's too late. Just do it.")
                                           continue
                                     else :
                                       print("\n You can't go there.")
                                       continue
                                 else :
                                   print("\n You can't do that. \n")
                                   continue
                             if direction == "N":
                               continue
                             else :
                               print("\n You can't do that. \n")
                               continue
                         if direction == "N":
                           continue
                         else :
                           print("\n You can't go there. \n")
                           continue
                     else :
                       print("\n You can't go there. \n")
                       continue
                 if direction == "N":
                   print("You can't go back. \n")
                   sleep(1.4)
                   continue
                 else :
                   print("\n You can't go there. \n")
                   continue
             #TAKE HEADPHONES??
             if "headphones" in direction:
               print("\n Oookay... they won't be of any use, but it's your choice.")
               inventory = inventory + "\n Headphones"
               sleep(1)
               print("Added to your inventory. To see inventory, enter 'i'")
               continue
             if direction == "i":
               print(inventory)
               continue

             #TAKE BABY BOTTLE?? no
             if "baby bottle" in direction:
               print("\n I don't think this kid's mom would like that very much.")
               continue
             #TAKE BLANKET?
             if "blanket" in direction:
               print("\n Sure, I guess if you want it. It's not like anyone's here to claim it.")
               inventory = inventory + "\n Wool blanket"
               sleep(1)
               print("Added to your inventory. To see inventory, enter 'i'")
               continue
             if direction == "i":
               print(inventory)
               continue

             if direction == "N":
               print("You can't go back")
               continue
             else :
               print("\n You can't do that. \n")
               continue
         if direction == "E":
           levelOne()
         else :
           print("\n You can't go there. \n")
           continue
     if direction == "E":
       print("That's a window. You can't go there.")
       continue
     if direction == "N":
       print("That's a wall. You can't go there.")
       continue
     else :
       print("\n You can't go there. \n")
       continue
