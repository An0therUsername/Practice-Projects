#Ceaser Cypher
# Bug: Adds additional characters around symbols and spaces. 

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()'
MAX_KEYLENGTH = len(SYMBOLS)

def getMode():
    while True:
        print('Do you want to encrypt, decrypt or brute force a message?')
        mode = input().lower()
        if mode in ['encrypt', 'decrypt', 'brute force', 'd', 'e', 'b']:
            return mode
        else:
            print("Please enter 'encrypt', 'decrypt', 'brute force', 'd', 'e', 'b'")

def getMessage():
    print('Please enter your message:')
    return input()
    
def getKey():
    key = 0
    while True:
        print('Please enter your key between 1 and %s' %(MAX_KEYLENGTH))
        key = int(input())
        if (key >= 1 and key <= MAX_KEYLENGTH):
            return key
            
def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated_message = ''
    
    for symbol in message:
        symbol_index = SYMBOLS.find(symbol) 
        
        if symbol_index == -1:
            translated_message += symbol
        else:
            symbol_index += key
                                
            if symbol_index >= len(SYMBOLS):
                symbol_index -= len(SYMBOLS)
            elif symbol_index < 0:
                symbol_index += len(SYMBOLS)
             
            translated_message += SYMBOLS[symbol_index]
        
    return translated_message
    
mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()
print('Your tranlated messege is: ')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEYLENGTH + 1):
        print(key, getTranslatedMessage('decrypt', message, key))
