import random




def hangman_pic(tries_left):
# fix order
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


    while total_lives >= 0:
        word = random_word_from_list(list_of_words)
        user_word_progress = initialize_word_progress(word)

        while tries > 0:
            print("Score:", score)
            print("Total lives:", total_lives)
            print("Tries:", tries)
            hangman_pic(tries)
            print_word_progress(user_word_progress)

            user_guess = input("Enter a letter : ").lower()
            user_guess_positions = find_positions_in_word(user_guess, word)
            if not user_guess_positions:
                tries -= 1
                print("incorrect")

            else:
                update_word_progress(user_guess, user_guess_positions, user_word_progress)

def update_word_progress(user_input, positions, progress_list):
    for position in positions:
        progress_list[position] = user_input



def print_word_progress(user_word_progress):
    print(''.join(user_word_progress))


def find_positions_in_word(user_guess, word):
    user_guess_positions = []
    for pos, char in enumerate(word):
        if char == user_guess:
            user_guess_positions.append(pos)
    return user_guess_positions



def initialize_word_progress(word):
    return list("_" * len(word))


#def replace_blanks(user_input):



def random_word_from_list(list_of_words):
    word_num = random.randint(0, len(list_of_words)-1)
    word = list_of_words[word_num]
    return word


def get_total_lives_from_user():
    total_lives = 0
    while total_lives <= 0:
        user_difficulty = input("Enter a difficulty easy, medium, or hard: ")
        total_lives = get_total_lives(user_difficulty)
    return total_lives

def get_total_lives(user_difficulty):
    if user_difficulty == "easy":
        return 8
    elif user_difficulty == "medium":
        return 4
    elif user_difficulty == "hard":
        return 2
    else:
        return -1




if __name__ == '__main__':
    main()





































































