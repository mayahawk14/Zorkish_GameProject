#intro
def beach():
  print("You have made it to the beach! To your left and to your right are miles and miles of sand, but in the distance you can see a house infront of you.")

def frontHouse():
  print("You are infront of the house, it looks abandoned but clean. The front door is locked, it appears it needs a key to be opened.")

def mailbox():
  print("There is a mailbox to your left... do you want to open it?")

def openMailbox():
  print("There is a letter... do you want to read it?")

def openLetter():
  print("Dear Betty, \n I really enjoyed my stay here! I lost the main key in the ocean while I was swimming, so I left the spare key under the rock by the back door just in case! Thank you for letting me stay here, and sorry for losing the key! ")

def backHouse():
  print("You are at the back of the house. There appears to be windows, but they are borded, and there is another door that can't be opened.")

def rock():
  print("Laying suspiciously by the door is a rock. Do you want to pick up the rock? ")

def key():
  print("You pick up the rock and you find the key! Go back the way you came from and try opening the front door now!")

def backDoor():
  print("Not this door silly! The front door!")

def frontDoor():
  print("Yay the door is open... do you want to enter the house?")

def frontDoorkey():
  print("You are at the front of the house and you have the key! You can open the door now!")

def kitchen():
  print("You have entered the house and are now in the kitchen. You see a table, a fridge, and some bottled waters. There is a hallway to your right leading to the living room. You also see a staircase leading up to the bedroom.")

def kitchenTwo():
  print("You are in the kitchen again. You see more BOTTLED WATERS making you THIRSTY! There is a hallway to your right leading to the living room. You also see a staircase leading up to the bedroom.\n")
  sleep(1)
  print("You should TAKE SOME WATER!!!")

def livingRoom():
  print("You are now in the living room. You see a couch and a TV playing scary music, you also see a blanket folded nicly on the couch. Do you want to take the blanket?")

def blanket():
  print("This blanket looks nice... now I wanna take a nap! You should head back to the kitchen to go upstairs and take a nap!")

def stairs():
  print("The stairs are dark and scary. There is a light switch next to you do you want to turn the lights on?")

def lightOn():
  print("The lights are on now! You can see the staircase is coverd in pictures of what seem to be the home owners dog. You can now continue going up!")

def lightOff():
  print("Dummy! Now you can't see! Turn the lights back on!")

def bedroom():
  print("You are in a bed room, the walls are painted orange, and you see the sun is about to set, so you decide to take a nap in the bed that’s to your right... do you want to take a nap? yes or no?")

def nap():
  print ("You lay in the bed and fall asleep. You hear an alarm in the distance, and wake up. You realize the entire day was just a dream! ")

def floornap():
  print ("Your body is too tired. You fall on the floor and fall asleep. You hear an alarm in the distance, and wake up. You realize the entire day was just a dream! ")

def ending():
  print("Thank you for playing our game!")
  sleep(1)
  print("Made by... Maya Hawkins... Victoira Johnson... and Jayleen Holden")

from time import sleep


def levelThree():
  while True:
    beach()
    while True:
      direction = input()
      if direction == "N":
        frontHouse()
        print("\n")
        mailbox()
      else:
        if direction == "E":
          print("There is only sand... you can't walk that way. \n")
        if direction == "W":
          print("There is only sand... you can't walk that way. \n")
        if direction == "S":
          print("That way is the ocean... do you really want to go back in? \n")
      if direction == "no":
        print("Are you sure... it's kinda important!")
      if direction == "yes":
        print("Very vague... what do you want to do?")
      if direction == "open":
        openMailbox()
      if direction == "read":
        openLetter()
        sleep(3)
        print(" \n here's a hint... the key you found in the ocean won't open the front door... go to the back of the house!")
        while True:
          direction = input()
          if direction == "N":
            print("Even though you can't walk through a house... \n")
            backHouse()
            rock()
          else:
            if direction == "E":
              print("That way won't get you to the house. \n")
            if direction == "W":
              print("That way is just a void... you physically can't enter. \n")
            if direction == "S":
              print("This is the way back to the beach... you won't win if you go this way! And I won't let you lose.")
          if direction == "no":
              print("Bro... just pick up the rock!")
          if direction == "yes":
            print("Very vague... what do you want to do?")
          if direction == "pick up":
            key()
            while True:
              direction = input()
              if direction == "S":
                frontDoorkey()
              else:
                if direction == "N":
                  print("Going this way will lead to your death... trust me don't take the chance!")
                if direction == "E":
                  print("You can't go this way... sorry.")
                if direction == "W":
                  print("You can't go this way... sorry.")
              
              if direction == "yes":
                print("Very vague... what do you want to do?")
              if direction == "open":
                print("What door do you want to open?")
              if direction == "open back door":
                print("That's unecessary.")
              if direction == "open front door":
                frontDoor()
                while True:
                  direction = input()
                  if direction == "enter":
                    kitchen()
                  if direction == "take":
                    print("Take what?")
                  if direction == "take water":
                    print("You acctually can't sorry.")
                  if direction == "E":
                    livingRoom()
                  else:
                    if direction == "S":
                      print("That goes back outside... you don't want to do that.")
                    if direction == "N":
                      print("That goes no where.")
                    if direction == "W":
                      print("That goes no where.")
                  if direction == "no":
                    print("Come on... you no you want it.")
                  if direction == "take":
                      print("Take what?")
                  if direction == "take blanket":
                    blanket()
                    while True:
                      direction = input()
                      if direction == "W":
                        kitchenTwo()
                      else:
                        if direction == "N":
                          print("That goes no where.")
                        if direction == "E":
                          print("That goes no where.")
                        if direction == "S":
                          print("That goes no where.")
                      if direction == "take":
                        print("Take what?")
                      if direction == "take water":
                        print("You acctually can't sorry.")
                        while True:
                          direction = input()
                          if direction == "N":
                            stairs()
                          else:
                            if direction == "E":
                              print("You don't need to go back into the living room... just go upstairs and take a nap.")
                            if direction == "S":
                              print("That is the front door... please don't leave.")
                            if direction == "W":
                              print("That is a fridge filled with expired food... you can't eat any of it.")
                          if direction == "lights off":
                            lightOff()
                          if direction == "lights on":
                            lightOn()
                            while True:
                              direction = input()
                              if direction == "N":
                                bedroom()
                              else:
                                if direction == "S":
                                  print("The stairs have dissapeared behind you... you can't go back down.")
                                if direction == "E":
                                  print("You're in a staircase... you can't move side to side.")
                                if direction == "W":
                                  print("You're in a staircase... you can't move side to side.")
                              if direction == "no":
                                floornap()
                                sleep(2)
                                ending()
                              if direction == "yes":
                                nap()
                                sleep(2)
                                ending()
                            
                              
