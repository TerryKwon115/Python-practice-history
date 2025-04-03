from Day3_3_Image import image

print(image)

print("Welcome to Treasure island.\nYour mission is to find the treasure.")

choice1 = input('You\'re at a fork in the road, where do you want to go?\n'
                '"Left" or "Right". Type "L" or "R".\n').lower()
if choice1 == "l" : 
    choice2 = input('A jungle stretches out before you.\n'
                    'Will you enter the jungle or take a detour?\n'
                    '"Enter" or "Detour". Type "E" or "D".\n').lower()
    if choice2 == "e" : 
        choice3 = input('You encounter a giant water snake. Will you fight it or run away?\n'
                        '"Fight" or "Run". Type "F" or "R".\n').lower()
        if choice3 == "f" : 
            choice4 = input('You discover a large cave behind the dead water snake.\n'
                            'Inside the cave, there are three doors.\n'
                            '"Red", "Blue", or "Yellow". Type "R", "B", or "Y".\n').lower()
            if choice4 == "r" :
                print("You are engulfed in flames. Game over.")
            elif choice4 == "b" :
                print("You fall into the water filled with crocodiles. Game over.")    
            elif choice4 == "y" : 
                choice5 = input('You finally discover a treasure chest.\n'
                                'On the chest, there is an inscription that reads,\n'
                                '"Those who disturb my peace shall never see the light of day."\n'
                                'Will you open the chest?\n'
                                '"Yes" or "No". Type "Y" or "N".\n').lower()
                if choice5 == "y" : 
                    print("The chest is filled with treasure. Congratulations!\n"
                          "However, moments later, you feel your entire body becoming paralyzed.\n"
                          "Game over.")
                elif choice5 == "n" : 
                    print("Congratulations! Your reason has triumphed over your instincts.\n"
                          "You have escaped the curse.\n"
                          "However, moments later, you collapse, struggling to breathe.\n"
                          "Game over.")
                else : 
                    print("You made a choice that is not an option. Game over.")
            else : 
                print("You made a choice that is not an option. Game over.") 
        elif choice3 == "r" : 
            print("The water snake bit you as you tried to escape. Game over.")
        else : 
            print("You made a choice that is not an option. Game over.")
    elif choice2 == "d" : 
        print("You have been captured by cannibals. Game over.")
    else : 
        print("You made a choice that is not an option. Game over.")
elif choice1 == "r" : 
    print("You're trapped. Game over.")
else : 
    print("You made a choice that is not an option. Game over.")
