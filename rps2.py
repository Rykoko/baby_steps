import random
import time

rounds = 0
AI = 0
Player = 0

while rounds < 3:

    options = ['Rock', 'Paper', 'Scissors']

    loses_to = {
        'paper': 'rock',
        'rock': 'scissors',
        'scissors': 'paper',
    }

    player_choice = input('Pick an option [Rock, Paper, Scissors]: ').lower()
    comp_choice = random.choice(options).lower()

    for option in options:
        print(option)
        time.sleep(0.4)

    def play(player_choice, comp_choice):
        global AI
        global Player
        if player_choice == loses_to[comp_choice]:
            print (f'\nComputer wins! {comp_choice} beats {player_choice}')
            AI += 1
        elif comp_choice == loses_to[player_choice]:
            print (f'\nYou win! {player_choice} beats {comp_choice}')
            Player += 1
        else:
            print ('\nDraw!')
            Player += 1
            AI += 1

    rounds += 1

    play(player_choice, comp_choice)

    print(f'Rounds:  {rounds}\nComputer: {AI}\nPlayer: {Player}\n')

    if rounds == 3:
        if AI > Player:
            print(f'Computer wins {AI} - {Player}!!\n')
        elif Player > AI:
            print(f'Player wins {Player} - {AI}!!\n')
        else:
            print(f'Draw {Player} - {AI}\n')

        ask = input('\nDo you want to play again [y/n]? ')
        if ask == 'y':
            rounds = 0
            Player = 0
            AI = 0
            print('Loading new game...')
            time.sleep(1.0)
        else:
            quit()
