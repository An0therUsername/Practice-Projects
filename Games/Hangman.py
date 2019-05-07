# Hangman
'''
Hangman is a game for two people in which one player thinks of a word and then draws a blank line on the page for each letter in the word. The second player then tries to guess letters that might be in the word. If the second player guesses the letter correctly, the first player writes  the letter in the proper blank. But if the second player guesses incorrectly, the first player draws a single body part of a hanging man. The second player has to guess all the letters in the word before the hanging man is completely drawn to win the game. 
'''

import random

HANGMAN_PICS = ['''  
   +---+  
       |  
       |  
       |  
      ===''', '''  
   +---+  
   O   | 
       | 
       | 
      ===''', ''' 
   +---+ 
   O   | 
   |   | 
       | 
      ===''', ''' 
   +---+ 
   O   | 
  /|   | 
       | 
      ===''', ''' 
   +---+ 
   O   | 
  /|\  | 
       |
      ===''', ''' 
   +---+ 
   O   | 
  /|\  | 
  /    | 
      ===''', ''' 
   +---+ 
   O   | 
  /|\  |
  / \  | 
      ===''','''
   +---+ 
  [O   | 
  /|\  | 
  / \  | 
      ===''', ''' 
   +---+ 
  [O]  | 
  /|\  | 
  / \  | 
      ==='''
]

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar        coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk        lion lizard llama mole monkey moose mouse mule newt otter owl panda        parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep        skunk sloth snake spider stork swan tiger toad trout turkey turtle        weasel whale wolf wombat zebra lucy jan allenheads berlin bicycle'.split()

def getRandomWord(wordlist):
    '''Select random word out of provided word list'''
    random_word_index = random.randint(0,len(wordlist) - 1)
    return wordlist[random_word_index]
    
def displayBoard(missed_letters, correct_letters, secret_word):
    '''Display Hangman board depensing on number of wrong answers'''
    print(HANGMAN_PICS[len(missed_letters)])
    print()
        
    blanks = '_'*len(secret_word)
    
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
            
    for letter in blanks:
        print(letter, end = ' ')
    
    print() 
    print()   
    print('Missed letters: ', end = ' ')
    for letter in missed_letters:
        print(letter, end = ' ')
    print()
    print()


def getGuess(already_guessed):
    '''Get players guesses'''
    while True:
        guess = input('Please guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter only one letter.')
        elif guess in already_guessed:
            print('You already guessed this letter.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please only enter a letter from this known alphabet.')
        else:
            return guess
    
def playAgain():
    '''Ask player if she wants to play again'''
    answer = input('Do you want to play again. Yes or No?')
    return answer.lower().startswith('y')
    
print('H A N G M A N')
print('='*48)
correct_letters = ''
missed_letters = ''
secret_word = getRandomWord(words)
gameIsDone = False

while gameIsDone == False:
    displayBoard(missed_letters, correct_letters, secret_word)
    guess = getGuess(missed_letters + correct_letters)
    if guess in secret_word:
        correct_letters = correct_letters + guess
        
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print("You won! The secret word was '%s'." %secret_word.title())
            gameIsDone = True
    else:
        missed_letters = missed_letters + guess
    
    if len(missed_letters) == len(HANGMAN_PICS)-1:
        displayBoard(missed_letters, correct_letters, secret_word)
        print('You run out of tries :-( \nAfter ' + str(len(missed_letters)) + ' false letters and ' + str(len(correct_letters)) + " correct guesses, the correct word was '" + str(secret_word).title() + "'.")
        gameIsDone = True
    
    if gameIsDone == True:
       if playAgain():
           correct_letters = ''
           missed_letters = ''
           gameIsDone = False
           secret_word = getRandomWord(words)
       else:
           break
        
