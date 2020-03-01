import math



def ReverseCypher(message):
    translated = ''
    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i = i - 1
    return translated

def CaeserCypher(message, step, mode):
    Symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(),./[]'
    translated = ''
    for letter in message:
        if letter in Symbols:
            symbolIndex = Symbols.find(letter) 
            if mode == 'e':
                transIndex = symbolIndex + step
            elif mode == 'd':
                transIndex = symbolIndex - step

            if transIndex > len(Symbols):
                transIndex = transIndex - len(Symbols)
            elif transIndex < 0:
                transIndex = transIndex + len(Symbols)
            
            translated = translated + Symbols[transIndex]
            code = '000'
        else:
            translated = translated + letter
            code = '403'
        
    return translated, code

def TranspositionCypher(key, message, mode):
    if mode == 'e':
        ciphertext = [''] * key    
        for column in range(key):
            currentIndex = column        
            while currentIndex < len(message):                  
                ciphertext[column] += message[currentIndex]             
                currentIndex += key
        
        return ''.join(ciphertext)
    elif mode == 'd':
        
        numOfColumns = int(math.ceil(len(message) / float(key)))
    
        numOfRows = key            
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)    
        plaintext = [''] * numOfColumns
        column = 0
        row = 0
        for symbol in message:
            plaintext[column] += symbol
            column += 1 
            if (column == numOfColumns) or (column == numOfColumns - 1 and
                row >= numOfRows - numOfShadedBoxes):
                column = 0
                row += 1

        return ''.join(plaintext)

def EnigmaCypher(message, step, mode):
   
    indexSet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !@#$%^&*()_+-=/[]{}\?'
    translated = ''
    for symbol in message:
        if symbol in indexSet:
            if mode == 'e':
                symbolIndex = indexSet.find(symbol)
                symbolIndex = symbolIndex + 1 + 42
                symbolIndex = symbolIndex + step
                if symbolIndex > len(indexSet):
                    symbolIndex = symbolIndex - len(indexSet)
                if symbolIndex > 42:
                    part = symbolIndex ** 2 + 1
                    strpart = str(part)
                    translated = translated + strpart + '|'
                elif symbolIndex <= 42:
                    part = symbolIndex ** 2 - 1
                    strpart = str(part)
                    translated = translated + strpart + '|'
                
            elif mode == 'd':

                numlist = []
                

                numlist = message.split('|')

                
                while len(translated) <= len(numlist):
                    for num in numlist:
                        
                        if int(num) > (42 ** 2 + 1):
                            print(num)
                            part = math.sqrt(int(num) - 1)
                            
                            symbolIndex = part - step
                            symbolIndex = symbolIndex - 1 - 42
                            translated = translated + indexSet[int(symbolIndex)]
                        elif int(num) <= (42 ** 2 - 1):
                            part = math.sqrt(int(num) + 1)
                            
                            symbolIndex = part - step
                            symbolIndex = symbolIndex - 1 - 42
                            translated = translated + indexSet[int(symbolIndex)]
        else:
            translated = translated + symbol

    
    return translated