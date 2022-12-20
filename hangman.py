#Step 1 

# from dis import dis
import random
# from re import A
from hangmanart import stages
# TODO add user choice input/word list

# TODO - find bigger word list 

word_list = ["aardvark", "baboon", "camel"]
word_list += input("type your word")

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
display = []

for letter in chosen_word:
    # display.append("_")
    display += "_"
print(display)
lives = 6 
while True:

    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("guess a letter ").lower()

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.hangman.py
    if guess in chosen_word:
        for letter in range(len(chosen_word)):
            if chosen_word[letter] == guess:
                display[letter] = guess
    else:
        lives -= 1
        print(stages[lives])
        if lives <=0:
            print("you lost")
            break
    if "_" in display:
        print(display)
    else: 
        print("game won")
        break
