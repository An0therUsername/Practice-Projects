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
    
def getClue(secret_num, guess):
# Return clue to player

    if secret_num == guess:
        print('You got it. Congratulations.\n')

    clue = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clue.append('Fermi')
        elif guess[i] in secret_num:
            clue.append('Poco')
    if len(clue) == 0:
        print('Bagels!')
            
    clue.sort()
    return ' '.join(clue)
    
def isOnlyDigits(num):
# Returns True if num is a string of only digits. Otherwise, returns False.
    if num == '':
        return False
        
    for i in num:
        if i not in '1 2 3 4 5 6 7 8 9 0'.split():
            return False
    
    return True
    
print('I am thinking of a %s-digit number. Try to guess what it is.' %(NUM_DIGITS))
print('The clues I give are...')
print('When I say:    That means:') 
print('  Bagels       None of the digits is correct.')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')

while True:
#Main game loop

    secret_num = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it.\n' %(MAX_GUESSES))
    
    guesses_taken = 1
    
    while guesses_taken <= MAX_GUESSES:
        guess = ''
        while len(guess) != NUM_DIGITS or isOnlyDigits(guess) == False:
            guess = input('Guess %s: '%(guesses_taken))
            print(getClue(secret_num, guess))
            guesses_taken += 1
            if guess == secret_num:
                break
            if guesses_taken > MAX_GUESSES:
                print('You ran out of guesses. The correct answer was %s.'%(secret_num))
                
    print('Do you want to play again? (yes or no)')     
    if not input().lower().startswith('y'):   
        break
