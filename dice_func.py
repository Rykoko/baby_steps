import random
import time

# function for double rolls


def roll():
    time.sleep(0.5)
    dice1 = int(random.randint(1, 6))
    dice2 = int(random.randint(1, 6))
    print('Throws dice...')
    time.sleep(1)
    print(dice1 + dice2)
    return dice1, dice2


# while loop to maintain game as long as player indicates 'Y'

while True:

    # define dice variables

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    # ask for player's input

    ask = input('Do you want to roll the dice (Y/N)? ')

    # if based on player's response and dice roll outcome

    if ask == 'Y'.lower():
        dice1, dice2 = roll()

        # if player rolls a double, they get to roll again

        if dice1 == dice2:
            print('You rolled doubles!', dice1, '&', dice2, 'Roll again')
            dice1, dice2 = roll()

            # if the player rolls doubles a second time they get a third roll

            if dice1 == dice2:
                print('You rolled doubles for a second time!',
                      dice1, '&', dice2, 'Roll again')
                dice1, dice2 = roll()

            # after the third roll the game loops back to ask

    else:
        quit()
