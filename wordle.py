import random
from words import words
import string

print('===WORD GUESS===')

# Find and produce the word


def get_valid_word(words):
    # randomly chooses something from the list
    word = random.choice(words)
    return word.upper()

# Gameplay


def word_guess():
    word = get_valid_word(words)
    letters = set(word)  # Letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters guessed by player

    lives = 5

    while len(letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ',
              ' '.join(used_letters))

        word_fill = [
                letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_fill))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in letters:
                letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in used_letters:
            print('You have already used that letter')

        else:
            print('Invalid character')


# Gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('Game over! Word was', word)
    else:
        print('You guessed the word:', word, '!!')


word_guess()
