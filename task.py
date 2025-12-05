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
game_images = [rock, paper, scissors]
computer_choice = random.choice(game_images)

if user_choice < 0 or user_choice > 2:
    print("❌ That is not a valid option.")
else:
    if user_choice == 0:
        print(rock)
        print(computer_choice)
    elif user_choice == 1:
        print(paper)
        game_images = [rock, paper, scissors]
        comp_choose = random.choice(game_images)
        print(computer_choice)
    elif user_choice == 2:
        print(scissors)
        game_images = [rock, paper, scissors]
        comp_choose = random.choice(game_images)
        print(computer_choice)
    else:
        print("That is not a valid option.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0) or (
            user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("Computer wins. You lose!")s