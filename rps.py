# rock beats scissors
# scissors beats paper
# paper beats rock
# best 2 of 3
# print r, p, s, Go!
# you vs comp

import random
import time

# options

rps = ['Rock', 'Paper', 'Scissors']

# number of rounds (best 2 of 3)

# rounds = 3

# scorekeeping

# comp = 0
# you = 0

# player choice

# choice = input('What is your play [Rock, paper, scissors]? ')

# com choice

# comchoice = random.choice(rps)

# Gameplay


def game():

    # counts

    rounds = 3
    comp = 0
    you = 0

    while rounds > 0:

        choice = input('What is your play [Rock, Paper, Scissors]? ').lower()
        comchoice = random.choice(rps).lower()

        # if both play the same option

        if choice == comchoice:
            rounds -= 1
            comp += 1
            you += 1
            for i in rps:
                print(i)
                time.sleep(0.5)
            print('\n', '--->', choice, comchoice, '<---', '\n')
            print('DRAW!')
            print('Score: ', you, comp)

        # if you play rock - outcomes

        elif choice == 'Rock'.lower():
            if comchoice == 'Scissors'.lower():
                you += 1
                rounds -= 1
                for i in rps:
                    print(i)
                    time.sleep(0.5)
                print('\n', '--->', choice, comchoice, '<---', '\n')
                print('YOU WIN!')
                print('Score: ', you, comp)
            else:
                comp += 1
                rounds -= 1
                for i in rps:
                    print(i)
                    time.sleep(0.5)
                print('\n', '--->', choice, comchoice, '<---', '\n')
                print('YOU LOSE!')
                print('Score: ', you, comp)

        # if you play paper - outcomes

        elif choice == 'Paper'.lower():
            if comchoice == 'Rock'.lower():
                you += 1
                rounds -= 1
                for i in rps:
                    print(i)
                    time.sleep(0.5)
                print('\n', '--->', choice, comchoice, '<---', '\n')
                print('YOU WIN!')
                print('Score: ', you, comp)
            else:
                comp += 1
                rounds -= 1
                for i in rps:
                    print(i)
                    time.sleep(0.5)
                print('\n', '--->', choice, comchoice, '<---', '\n')
                print('YOU LOSE!')
                print('Score: ', you, comp)

            # if you play scissors - outcomes

        elif choice == 'Scissors'.lower():
            if comchoice == 'Paper'.lower():
                you += 1
                rounds -= 1
                for i in rps:
                    print(i)
                    time.sleep(0.5)
                print('\n', '--->', choice, comchoice, '<---', '\n')
                print('YOU WIN!')
                print('Score: ', you, comp)
            else:
                comp += 1
                rounds -= 1
                for i in rps:
                    print(i)
                    time.sleep(0.5)
                print('\n', '--->', choice, comchoice, '<---', '\n')
                print('YOU LOSE!')
                print('Score: ', you, comp)

    # printing the final scores

    if you > comp:
        print(f'You win!! The score is: {you} - {comp}')
    elif you < comp:
        print(f'You lose! The score is: {you} - {comp}')
    else:
        print(f'DRAW! The score is: {you} - {comp}')

    again = input('Play again (Y/N)? ')
    if again == 'Y'.lower():
        game()
    else:
        quit()


game()
