import random




def hangman_pic(lives_left):
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
    if lives_left == 0:
        print(hangman[1])
    elif lives_left == 1:
        print(hangman[2])
    elif lives_left == 2:
        print(hangman[3])
    elif lives_left == 3:
        print(hangman[4])
    elif lives_left == 4:
        print(hangman[5])
    elif lives_left == 5:
        print(hangman[6])
    elif lives_left == 6:
        print(hangman[7])


def main():

    # gets the word file and turns it into a list
    word_file = open("hangman_words.txt", "r")
    list_of_words = []
    for line in word_file:
        stripped_lines = line.strip()
        list_of_words.append(stripped_lines)

    guessed_words = []
    guessed_letters = []
    tries = 6
    score = 0
    total_lives = 0
    user_yes = True

    bad_input = True


    while bad_input:
        user_difficulty = input("Enter a difficulty easy, medium, or hard: ")
        if user_difficulty == "easy":
            total_lives += 8
            bad_input = False
        elif user_difficulty == "medium":
            total_lives += 4
            bad_input = False
        elif user_difficulty == "hard":
            total_lives += 2
            bad_input = False
        else:
            print("Enter easy, medium, or hard")
            continue

    while total_lives >= 0:
        word_num = random.randint(0, len(list_of_words))
        word = list_of_words[word_num]
        word_char_list = list(word)
        blank_spaces = []
        for i in range(len(word)):
            blank_spaces.append("_")
        print("Score:", score)
        print("Total lives:", total_lives)
        print("Tries:", tries)
        hangman_pic(total_lives)


        while tries >= -1:
            user_guess = input("Enter a letter or type the word to solve: ")
            if not user_guess.isalpha:
                print("It has to be a lower case letter")
                continue
            elif 1 < len(user_guess) < len(word_char_list):
                print("That's incorrect")
                tries -= 1
                continue












main()




































































