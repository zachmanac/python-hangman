import os
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    if guess in display:
      print("You've already chosen the letter: " + guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
       
        lives -= 1
        print(f"{guess} is not in the word")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(f"{lives} lives remaining.")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")