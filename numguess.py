# Guess a computer generated number
# Limited attempts
# Loops

import random
import time

answer = int(random.randint(1, 10))
attempts = 3
tries = 1
lose = f'You have run out of attempts, the correct answer was {answer}'

while attempts > 0:

    guess1 = input('Guess a number between 1 and 10 --> ')
    guess = int(guess1)
  
    if guess > 10 or guess < 1:
        print('Invalid input, guess a number between 1 and 10')

    if guess == answer:
        lose = f'You guessed right! The answer was {answer}!! It took you {tries} tries'
        break

    elif guess > answer:
        attempts -= 1
        tries += 1
        print(f'Too high, number is less than {guess}!')
        time.sleep(0.5)
        print(f'You have {attempts} attempts left')
        time.sleep(0.5)

    elif guess < answer:
        attempts -= 1
        tries += 1
        print(f'Too low, number is higher than {guess}!')
        time.sleep(0.5)
        print(f'You have {attempts} attempts left')
        time.sleep(0.5)

print(lose)
