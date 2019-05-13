#Ceaser Cypher

_SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_MAX_KEYLENGTH=len(_SYMBOLS)

def getMode():
    while True:
        print('Do you want to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'decrypt', 'd', 'e']:
            return mode
        else:
            print("Please enter 'encrypt', 'decrypt', 'd', 'e'")

def getMessage():
    print('Please enter your message:')
    return input()
    
def getKey():
    key = 0
    while True:
        print('Please enter your key between 1 and %s' %(_MAX_KEYLENGTH))
        key = int(input())
        if (key >= 1 and key <= _MAX_KEYLENGTH):
            return key
            
def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated_message = ''
    
    for symbol in message:
        symbol_index = _SYMBOLS.find(symbol)
        if symbol_index == -1:
            translated_message += symbol
        symbol_index += key
        
        if symbol_index >= len(_SYMBOLS):
            symbol_index -= len(_SYMBOLS)
        elif symbol_index < 0:
            symbol_index += len(_SYMBOLS)
            
        translated_message += _SYMBOLS[symbol_index]
        
    return translated_message
    
mode = getMode()
message = getMessage()
key = getKey()
print('Your tranlated messege is: ')
print(getTranslatedMessage(mode, message, key))
