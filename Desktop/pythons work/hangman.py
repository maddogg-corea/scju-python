import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for word in range(word_length):
    display += "_"
print(display)

end_of_game = False
chances = len(chosen_word)  # Number of chances based on the length of the chosen word

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if len(guess) > 1 or len(guess) < 1:
        print("Please enter a single letter.")
    elif len(guess) == 1:
        if guess not in chosen_word:
            chances -= 1
            print(f"{guess} is not in the word. You have {chances} chances left.")
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        print(display)

        if "_" not in display:
            end_of_game = True
            print("You win.")
        elif chances == 0:
            end_of_game = True
            print("You lose.")
        else:
            print("Keep playing.")