import random
from Day4_2_Image import rock, paper, scissors

game_image = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice < 0 or user_choice >= 3 : 
    print("You typed an invalid number. Try again.")
else : 
    computer_choice = random.randint(0, len(game_image)-1)

    print(f"\nUser choice is\n{game_image[user_choice]}\n")
    print(f"Computer choice is\n{game_image[computer_choice]}")

    if user_choice == computer_choice : 
        print("> It's a draw.\n")
    elif user_choice == 0 and computer_choice == 2 : 
        print("> You win.\n")
    elif user_choice == 2 and computer_choice == 0 : 
        print("> You lose.\n")
    elif user_choice > computer_choice : 
        print("> You win.\n")
    elif user_choice < computer_choice : 
        print("> You lose.\n")
