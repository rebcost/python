stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


from random import choice, gammavariate

word_list = ["aardvark", "baboon", "camel"]
chosen_word = choice(word_list)

# Creating a display

display = []
for _ in range(len(chosen_word)):
    display += "_"
#print(display) 

lives = 6
game_over = False

while not game_over:

    guess = input('Guess a letter: ')

    # Show the letter chosen on display

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

        if guess not in chosen_word:
            lives -= 1  
            if lives == 0:
                game_over = True
                print('You Lose')

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Condition of stop for the loop
    if "_" not in display:
        game_over = True
        print('You Win')

    print(stages[lives])
