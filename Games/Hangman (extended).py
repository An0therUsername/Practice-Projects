# Hangman 2.0
'''
Hangman is a game for two people in which one player thinks of a word and then draws a blank line on the page for each letter in the word. The second player then tries to guess letters that might be in the word. If the second player guesses the letter correctly, the first player writes  the letter in the proper blank. But if the second player guesses incorrectly, the first player draws a single body part of a hanging man. The second player has to guess all the letters in the word before the hanging man is completely drawn to win the game. 

===========================

This version has the following extended features:
    + Select difficulty and determine the number of possible failures
    + Select category of words to guess


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

words = {
    'Colors':'red orange yellow green blue indigo violet white black         brown'.split(), 
    'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid         chevron pentagon hexagon septagon octagon'.split(), 
    'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry         banana cantaloupe mango strawberry tomato'.split(), 
    'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle         fish frog goat leech lion lizard monkey moose mouse otter owl panda         python rabbit rat shark sheep skunk squid tiger turkey turtle weasel         whale wolf wombat zebra'.split(),
    'Cities':'berlin london munich amsterdam prag niece newyork boston athens paris sunderland'.split(),
    '5+ Letters':'paris berlin spunk'.split(),
    '10+ Letters':'bananasplit cheesecake'.split(),
    'Random' : 'red orange yellow green blue indigo violet white black         brown square triangle rectangle circle ellipse rhombus trapezoid         chevron pentagon hexagon septagon octagon apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato bat bear beaver cat cougar crab deer dog donkey duck eagle         fish frog goat leech lion lizard monkey moose mouse otter owl panda         python rabbit rat shark sheep skunk squid tiger turkey turtle weasel         whale wolf wombat zebra berlin london munich amsterdam prag niece newyork boston athens paris sunderland'.split(),
    }

def getRandomWord(word_dict, selected_category):
    '''Select random word out of provided word list'''
    #word_key = random.choice(list(word_dict.keys()))
    '''Selects word from player selected set'''
    word_key_list = list(word_dict.keys())
    word_key = word_key_list[int(selected_category)-1]
    word_index = random.randint(0, len(word_dict[word_key]) - 1)
    return [word_dict[word_key][word_index], word_key]
    
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
    print('Wrong letters: ', end = ' ')
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
    
def select_difficulty(difficulty):
    '''Select difficulty/number of possible tries'''
    options = ['E','M','H']
    while difficulty not in options:
        difficulty = input('Select difficulty: (E)asy, (M)edium, (H)ard: ').upper()
    if difficulty == 'E':
        print('Cool, you have 8 lives.')
    if difficulty == 'M':
        del HANGMAN_PICS [8]
        del HANGMAN_PICS [7]
        print('Cool, you have 6 lives.')
    if difficulty == 'H':
        del HANGMAN_PICS [8]
        del HANGMAN_PICS [7]
        del HANGMAN_PICS [5]
        del HANGMAN_PICS [3]
        print('Cool, you have 4 lives.')
        
def select_category(word_dict):
    '''Actively select a category to play'''
    print('\nAvailable categories: ')
    categories = list(word_dict.keys())
    for i in range(len(word_dict.keys())):
        print('[' + str(i+1) + ']' + str(categories[i]), end = ' ')
    selected_category = input('\nSelect the following category: ')
    return selected_category
    
print('H A N G M A N 2.0')
print('='*48)

difficulty = ''
select_difficulty(difficulty)
correct_letters = ''
missed_letters = ''
secret_word, secret_set = getRandomWord(words, select_category(words))
gameIsDone = False

while gameIsDone == False:
    print('The word is from the set: ' + secret_set.title())
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
           difficulty = ''
           select_difficulty(difficulty)
           correct_letters = ''
           missed_letters = ''
           secret_word, secret_set = getRandomWord(words, select_category(words))
           gameIsDone = False
       else:
           break
        
