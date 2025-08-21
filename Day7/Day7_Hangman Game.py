import random
from Day7_Image import hangman_print, alligator, butterfly, cockroach, stages

print(hangman_print)

word_list = ["alligator", "butterfly", "cockroach"]
ascii_list = [alligator, butterfly, cockroach]

# Random word selection
number = random.randint(0, len(word_list)-1)
chosen_word = word_list[number]

# Word to guess
placeholder = ""
for _ in range(len(chosen_word)):
    placeholder += "()"

print("\nWord to guess : " + placeholder)

lives = 6
correct_letters = []
wrong_letters = []
game = False 

while not game: 
    print(f"\n\n***************** {lives} / 6 LIVES LEFT *****************")
    guess = input("\nGuess a letter : ").lower()

    # Repeated letters 
    if guess in correct_letters or guess in wrong_letters: 
        print("\nYou already typed this letter. Try another a letter.")

    else: 
        display = ""

        # Correct guess 
        for letter in chosen_word: 
            if letter == guess: 
                display += letter
                correct_letters.append(letter)
            elif letter in correct_letters:
                display += letter
            else: 
                display += "()"

        # Wrong guess
        if guess not in correct_letters:
            wrong_letters.append(guess)
            lives -= 1
            print(f"\nYou guessed {guess}, that's not in the word. You lose 1 life.")

            # You lost with 0 lives 
            if lives == 0:
                print("=====================================================")
                print("\nYou lost!")
                game = True

    print(f"\nWord to guess : {display}\n")
    print(stages[lives])

    # You won by guessing the word
    if chosen_word == display: 
        print("=====================================================")
        print("\nYou won!")
        game = True

print(ascii_list[number])
print(f"\nThe answer is {word_list[number]}")