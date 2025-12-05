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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))
game_image = [rock, paper, scissors]
computer_choice_index = random.randint(0,2)
computer_choice = game_image[computer_choice_index]

if user_choice < 0 or user_choice > 2:
    print("❌ That is not a valid option.")
else:
    if user_choice == 0:
        print(rock)
        print(computer_choice)
    elif user_choice == 1:
        print(paper)
        print(computer_choice)
    elif user_choice == 2:
        print(scissors)
        print(computer_choice)
    else:
        print("That is not a valid option.")

    if user_choice == computer_choice_index:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice_index == 1) or (user_choice == 1 and computer_choice_index == 0) or (
            user_choice == 2 and computer_choice_index == 1):
        print("You win!")
    else:
        print("Computer wins. You lose!")