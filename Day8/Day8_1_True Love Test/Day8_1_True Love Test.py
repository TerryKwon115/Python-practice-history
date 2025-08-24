from Day8_1_Image import image

print(image)

# This fun test uses your names to calculate a unique love score.
# It counts how often the letters from the words
# TRUE" and "LOVE" appear in your combined names.

true = ["t","r","u","e"]  
love = ["l","o","v","e"]

def calculate_love_score(first, second):

    total_list = []
    first_num = 0
    second_num = 0

    total_name = (first + second).lower() 

    # Breaks the combined name into individual letters and stores them in total_list
    for letter in total_name: 
        total_list.append(letter) 
            
    # Counts how many times each letter from "TRUE" appears in the name
    for letter_true in true: 
        first_num += total_list.count(letter_true)
                
    # Counts how many times each letter from "LOVE" appears in the name
    for letter_love in love:
        second_num += total_list.count(letter_love)    
        
    score = int(str(first_num) + str(second_num))
        
    print(f"\n\n# Your True Love score : {score}\n")

    if score < 20:
        print("# Test Result : Are you sure about this relationship?\n")
        
    elif score < 40:
        print("# Test Result : This screams friendship zone.\n") 
        
    elif score < 60:
        print("# Test Result : Something's really missing.\n")    
        
    elif score < 80:
        print("# Test Result : This is the best match?\n")    
        
    elif score < 100:
        print("# Test Result : Stop kidding me.\n")      
        
    elif score < 1010:
        print("# Test Result : I can't stand liars.\n")
        
    else: 
        print("Test Result : This is lame.\n")

game = True
while game:
    
    first_name = input("\nPlease enter the first name : ")
    second_name = input("\nPlease enter the second name : ")

    calculate_love_score(first = first_name, second = second_name)
    
    question = input("\n* Would you like to play again? Yes or No : ").lower()
    
    if question == "yes":
        print("\n======================================================")
        
    elif question == "no":
        print("\n< Thanks for using the True Love Test! Next time, surprise me with a new date! >")
        game = False
        
    else:
        print("\n< Incorrect input. Please try again. >")
        game = False
