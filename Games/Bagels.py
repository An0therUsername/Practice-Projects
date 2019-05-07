#Bagels

'''
Bagels is a deduction game in which the player tries to guess a random three-digit number (with no repeating digits) gener-ated by the computer. After each guess, the computer gives the player three types of clues:

Bagels  None of the three digits guessed is in the secret number. 
Pico  One of the digits is in the secret number, but the guess has the digit in the wrong place. 
Fermi  The guess has a correct digit in the correct place.

The computer can give multiple clues, which are sorted in alphabeti-cal order. If the secret number is 456 and the player's guess is 546, the clues would be “fermi pico pico.” The “fermi” is from the 6 and “pico pico” are from the 4 and 5.
'''

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def getSecretNum():    
#Returns a string of unique random digits that is NUM_DIGITS long.

    numbers = list(range(10))
    random.shuffle(numbers)
    
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num
