import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

user_input = int(input("what do you choose? 0 for rock, 1 for paper, 2 for scissor\nyour choose: "))
if user_input >=0 and user_input <=2:
    print(game_image[user_input])

else:
    print("You typed an invalid number. You lose!")


computer_choice = random.randint(0,2)
print(f"computer chose: {computer_choice}")
print(game_image[computer_choice])

if user_input == 0 and computer_choice == 1:
    print("computer win!")

elif user_input == 1 and computer_choice == 2:
    print("computer win!")

elif user_input == 2 and computer_choice == 0:
    print("computer win!")

elif user_input == computer_choice:
    print("It's draw.")

elif user_input == 1 and computer_choice == 0:
    print("you win!")

elif user_input == 2 and computer_choice == 1:
    print("you win!")

elif user_input == 0 and computer_choice == 2:
    print("you win!")

else:
    print("computer win!")