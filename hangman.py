import random
'''''
Jan 20,2022
Jayden Mendoza

This is a hangman game where the user enters one letter to try and solve the word.
the user will be given an amount of lives of their choosing (how many times they can get a word wrong)
They will earn score based on how long the word is.

'''''
# prints the rules
def rules():
    print("These are the rules for hangman:\n1. If the user enters a number or special character it will be taken as a guess\n2. You will choose a mode easy,medium,or,hard. Each mode will depend on how many lives you have\n3. Your score will be determined by the length of the word that you solve ")
    print('\n')

# pictures of hangmen
def hangman_pic(tries_left):
    hangman = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
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
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    hangman.reverse()
    print(hangman[tries_left])


def main():

    # gets the word file and turns it into a list
    word_file = open("hangman_words.txt", "r")
    list_of_words = []
    for line in word_file:
        stripped_lines = line.strip()
        list_of_words.append(stripped_lines)

    wrong_guessed_letters = []
    right_guessed_letters = []
    tries = 6
    score = 0
    total_lives = get_total_lives_from_user()


# updates word progress i.e. fills in the blanks
def update_word_progress(user_input, positions, progress_list):
    for position in positions:
        progress_list[position] = user_input


# prints the word progress
def print_word_progress(user_word_progress):
    print(''.join(user_word_progress))
# takes all items in an iterable and joins them into one string
# iterable is anything that you can loop over using a for loop in Python

# finds the index of the position of the user guess and adds it to a list
def find_positions_in_word(user_guess, word):
    user_guess_positions = []
    for pos, char in enumerate(word):
        if char == user_guess:
            user_guess_positions.append(pos)
    return user_guess_positions

# starts the amount of blanks
def initialize_word_progress(word):
    return list("_" * len(word))

# generates a random word form list
def random_word_from_list(list_of_words):
    word_num = random.randint(0, len(list_of_words)-1)
    word = list_of_words[word_num]
    return word

# ges the user to choose a mode
def get_total_lives_from_user():
    total_lives = 0
    while total_lives <= 0:
        user_difficulty = input("Enter a difficulty 'easy' = 8 lives, 'medium' = 4 lives, or 'hard' = 2 lives: ").strip().lower()
        total_lives = get_total_lives(user_difficulty)
    return total_lives

# sets the number of lives
def get_total_lives(user_difficulty):
    if user_difficulty == "easy":
        return 8
    elif user_difficulty == "medium":
        return 4
    elif user_difficulty == "hard":
        return 2
    else:
        return -1
# returns -1 if it is anything but the 3 answers and loops back

# this checks the user input
def attempt_word(list_of_words, score, total_lives):
    guessed_letters = set()
    tries = 6
    word = random_word_from_list(list_of_words)
    user_word_progress = initialize_word_progress(word)
    print('\n')
    print(word)
    attempting_word = True

    while attempting_word:
        # prints the main interface images
        print("Tries: ", tries, " Lives: ", total_lives, " Score:", score)
        print("Incorrectly guessed letters:", guessed_letters or '')
        hangman_pic(tries)
        print("Word:")
        print_word_progress(user_word_progress)

# gets user input strips of white spaces then makes it lowercase
        user_guess = input("Enter a letter : ").strip().lower()
        print('\n')

# if the letter has already been guessed it loops back
        if user_guess in guessed_letters:
            print(">>>You already guessed that<<<")
            print("\n")
            continue

# if the input is greater than 1 it loops back
        if len(user_guess) != 1:
            print("\n>>> Enter exactly 1 letter <<<\n")
            continue

# tries to find the user guess index in the word,records the index, and replaces a white space with the user's input
        user_guess_positions = find_positions_in_word(user_guess, word)

# if it can't find it is incorrect
        if not user_guess_positions:
            tries -= 1
            guessed_letters.add(user_guess)
            print(">>>Incorrect<<<")
            print('\n')

# updates missing spaces and adds the user input to guessed words
        else:
            update_word_progress(user_guess, user_guess_positions, user_word_progress)
            guessed_letters.add(user_guess)

# checks for a complete word
        if "_" not in user_word_progress:
            score = score + len(word)
            print(">>>Well Done! Word solved!<<<")
            attempting_word = False

# checks for a failed word
        if tries == 0:
            hangman_pic(tries)
            print("-----HANGED-----")
            print("The word was:", word)
            print('\n')
            total_lives -= 1
            attempting_word = False
    return score, total_lives




def main():

# gets the word file and turns it into a list
    word_file = open("hangman_words.txt", "r")
    list_of_words = []
    for line in word_file:
        stripped_lines = line.strip()
        list_of_words.append(stripped_lines)
    print(">>>>>WELCOME TO HANGMAN<<<<<")
    rules()
    score = 0
    total_lives = get_total_lives_from_user()
# loops until total_lives are 0
    while total_lives > 0:
        score, total_lives = attempt_word(list_of_words, score, total_lives)
# asks the user to play again
    while input("Play again? (Y/N):").upper() == "Y":
        word_file = open("hangman_words.txt", "r")
        list_of_words = []
        for line in word_file:
            stripped_lines = line.strip()
            list_of_words.append(stripped_lines)
        print(">>>>>WELCOME TO HANGMAN<<<<<")
        rules()
        score = 0
        total_lives = get_total_lives_from_user()
        while total_lives > 0:

            score, total_lives = attempt_word(list_of_words, score, total_lives)


# is used to execute some code only if the file was run directly, and not imported
if __name__ == '__main__':
    main()





