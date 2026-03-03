import AIRPLANE as biome1
import HOUSE as biome3

def ocean():  
 print("\n You have fallen in the ocean! You are in the middle of the sea with miles of water, but if you look down there is a home of neon coral reefs  at the bottom of the sea.")

def coralreef():
  print("you are in the neon coral reefs, north of you is a old abondoned ship covered in algae.")

def oldship():
 print ("You are in a old abondoned ship at the bottom of the sea, the ship is empty, to the east of you is only a big chained chest")

def smallatlantis():
  print("Behind the chest is small city of atlantis with water bugs. There is nothing else here.")

def deepblackhole():
  print("Far left outside of the ship is deep black hole, if try and expore game will restart")

def oldmonumentstatues():
 print("West of black hole stautes are carved with wording,.... care to read?")

def thetwilightzone():
  print("It got dark, to the far left there is a group of big creatures.... but close to them is a shiny pair of bolt cutters... would you like to pick up?")

def Giantkelp():
  print("Surrouding chest is giant kel. To get through must find sword.. north of you is a dark aisle way with a glowing light underneath a door at the end of the hall.")

def darkaisleinship():
  print("North of aisle is door ... open door? Snside is silver sword. Do you want to pick up?")


def chainedchest():
  print("Surrouned by the giant kelp is the chest northeast of you ....do you want to open? ")



#game def

def levelTwo():
 inventory = "a mysterious thing in your pocket"
 while True:
   ocean()
   while True:
     direction = input()
     if direction == "down":
       coralreef()
       while True:
         direction = input()
         if direction == "E":
           print("you can't go that way... it's just water for miles. \n")
         if direction == "W":
           print("you can't go that way... it's just water for miles. \n ")
         if direction == "S":
           print("you can't go that way... it's just water for miles. \n ")
         if direction == "up":
           print("You can't go that way... do you really think you can fly. \n ")
         if direction == "N":
           oldship()
           while True:
             direction = input()
             if direction == "E":
               print("There is a big chained chest with giant kelp surrounding it.")
               if direction == "W":
                 print("You can't go that way.")
                 continue
             if direction == "N":
               print(" Is a dark aisle way with a glowing light underneath a door at the end of the aisle.")
               while True:
                 direction = input()
                 if direction == "S":
                   print("You probably want to go back.")
                   continue
                 if direction == "N":
                   smallatlantis()
                   continue
                 if direction == "NW":
                   direction = input("There a big deep black hole...would you like to explore?\n")
                   if direction == "yes":
                     biome1.levelOne()
                   else :
                     print("Smart of you. Try somewhere else")
                     continue
                 if direction == "W":
                   oldmonumentstatues()
                   print("There are old large statues carved with wording. Want to read?")
                   if direction == "yes":
                     print("The key to get out is by unordinary creatuers")
                   if direction =="W":
                     thetwilightzone()
                     while True:
                       direction = input()
                       if direction == "E":
                         print("It is pitch dark there are shadows of big creatures in the distance but a shiny object is on the ground.... want to pick up?")
                         direction = input()
                         if direction == "yes":
                           inventory = inventory + "\n Silver Sword"
                           print("Added to your inventory. To see inventory, enter 'i'")
                         if direction == "i":
                           print(inventory)
                           continue
                       if direction == "W":
                         print("you can't go that way.")
                       if direction == "S":
                         Giantkelp()
                         direction = input("In order to get to chest to open find a sword to cut throught kelp.\n")
                         if direction == "E":
                           print("you can't go that way.")
                         if direction == "W":
                           print("you can't go that way.")
                         if direction == "N":
                           darkaisleinship()
                           print("you have reached the end of the hall there is a door.... do you want to open it?")
                           while True:
                             direction = input()
                             if direction == "yes":
                               print("There is a silver sword on shiing bright on a chair.... do you want to pick up?")
                               while True:
                                 direction = input()
                                 if direction == "yes":
                                   inventory = inventory + "\n Silver Sword"
                                   print("Added to your inventory. To see inventory, enter 'i'")
                                 if direction == "i":
                                   print(inventory)
                                   continue
                                 if direction == "NE":
                                   chainedchest()
                                   direction = input("There is a chained chest in front of you.... do you want to open?")
                                   if direction =="yes":
                                     dircetion = input("Do you want to use bolt cutters?\n")
                                     if direction == "yes":
                                       print("You have opened the chest inside way a key to the house now you can leave!")
                                       direction = input("Swim up to the surface. You might find land!\n")
                                       if "swim" in direction:
                                         direction = input("You reach the top of the water... scanning your surroundings, you find shore! Go ahead and swim over!\n")
                                         if "swim" in direction:
                                           biome3.levelThree()
                                   

