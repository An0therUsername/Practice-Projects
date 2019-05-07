'''
In Dragon Cave the player decides between two caves and faces either a friendly or deadly dragon.
'''

import time, random


def intro_text():
    print(
        'You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.'
    )


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        cave = input('Choose cave 1 or 2. Cave: ')
    return cave


def check_cave(chosen_cave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    time.sleep(3)

    friendly_cave = random.randint(1, 2)

    if chosen_cave == str(friendly_cave):
        print('gives you his treasure. You win.\n')
    else:
        print('gobbles you down. Yumm!\n')


play_again = 'yes'
while play_again == 'Yes' or play_again == 'yes' or play_again == 'y':
    intro_text()
    check_cave(choose_cave())

    play_again = input('Do you want to play again? Yes or No?')

