import random
import os
from hangman_list import word_list
from hangman_stages import stages, logo

def life_stage():
    os.system("cls")
    print(logo)
    print(stages[player_lives])
    print(f"********************************{player_lives}/6 LIVES LEFT********************************")
    if game_over == False:
        print(f"Word to guess: {placeholder}")
        if guess_status == "right":
            print(f"You guessed {user_guess}, that is in the word.")
        elif guess_status == "wrong":
            print(f"You guessed {user_guess}, that's not in the word. You lose a life")
        elif guess_status == "guessed":
            print(f"You have guessed {user_guess} already. Please guess again.")
        if not guess_status == "":
            all_guesses = ""
            for i, guess in enumerate(incorrect_letters):
                all_guesses += guess
                if i != len(incorrect_letters)-1:
                    all_guesses += ","
            print(f"Incorrect attempts : {all_guesses}")

#variable initilization
guess_status = ""
player_lives = 6
gen_word = random.choice(word_list)
placeholder = "_" * len(gen_word)
game_over = False
correct_letters = []
incorrect_letters = []

#main game loop
while not game_over:
    #call header prompt to display information
    life_stage()
    user_guess = input("Guess a letter: ").lower()
    if user_guess in correct_letters or user_guess in incorrect_letters:
        guess_status = "guessed"
        continue
    #loop through and determine if guess was correct. Map this choice to the display word.
    placeholder = ""
    for letter in gen_word:
        if letter == user_guess:
            placeholder += letter
        elif letter in correct_letters:
            placeholder += letter
        else:
            placeholder += "_"
    #determine the guess status for the proper print statements in function to run
    if user_guess not in gen_word:
        player_lives -= 1
        guess_status = "wrong"
        incorrect_letters.append(user_guess)
    else:
        guess_status = "right"
        correct_letters.append(user_guess)
    
    #Determine if win condition is met or if all lives lost
    if "_" not in placeholder:
        game_over = True
        life_stage()
        print(f"***********************************YOU WIN!***********************************")
        print(f"You won! Congrats!!\nThe word was: {gen_word}")
    elif player_lives == 0:
        game_over = True
        life_stage()
        print(f"**********************************YOU LOST!***********************************")
        print(f"You lost all your lives. GAME OVER!\nThe word was: {gen_word}")
    


