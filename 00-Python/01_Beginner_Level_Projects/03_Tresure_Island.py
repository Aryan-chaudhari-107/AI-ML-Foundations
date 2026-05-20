
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at cross road. where do you want to go...\n"
                "left or right..?\n").lower()
if choice1 == "left":

    choice2 = input("You're come to the lake. There is island in the middle of the lake.\n"
                    "type 'swim' to swim across or type 'wait' to wait for a boat..?\n").lower()
    if choice2 == "wait":

        choice3 = input("You are arrived at the island unharmed. there is house with 3 doors.\n"
                        "which colour door would you chose? red, blue or yellow..?\n").lower()
        if choice3 == "yellow":
            print("you found the treasure, you win!!")
        elif choice3 == "red":
            print("Burned by fire. Game Over")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game over.")

    else:
        print("Attacked by trout. Game Over.")

else:
    print("Fall into a hole Game Over.")