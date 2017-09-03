import random
import string

fileName = raw_input('What is the name of the file you want to encrypt?')
file = open(fileName, 'r')
plainText = file.read().upper()
cypherText = ''

def subEncryption():
    #    key = int(raw_input('What would you like the offset to be?'))
    if ord(plainText[i]) + key > ord('Z'):
        cypherBit = chr(ord(plainText[i]) + key - 26)
    else:
        cypherBit = chr(ord(plainText[i]) + key)
    return cypherBit


#Options for encryption
selection = ''
while True:
    selection = raw_input('What type of encryption would you like to do? \n(C)aesar Shift\t(R)andom Substitution\t(V)ignere\nTo quit, type "Q"\n>>>')
    #I've got too many identations in here.  How can I clean it up?
    if selection == 'C':
        key = int(raw_input('What would you like the offset to be?'))
        for i in range(len(plainText)):
            if ord(plainText[i]) < ord('A') or ord(plainText[i]) > ord('Z'):
                cypherBit = plainText[i]
            else:
                cypherBit = subEncryption()
            cypherText = cypherText + cypherBit
    elif selection == 'R':
        alphabet = list(string.ascii_uppercase)
        random.shuffle(alphabet)
        for i in range(len(plainText)):
            if ord(plainText[i]) < ord('A') or ord(plainText[i]) > ord('Z'):
                cypherBit = plainText[i]
            else:
                cypherBit = alphabet[ord(plainText[i])-65]
            cypherText = cypherText + cypherBit
    elif selection == 'V':
        key = raw_input('Please enter the key you would like to use.>>>').upper()
        while len(key) < len(plainText):
            key = key + key
        for i in range(len(plainText)):
            if ord(plainText[i]) < ord('A') or ord(plainText[i]) > ord('Z'):
                cypherBit = plainText[i]
            else:
                cypherBit = chr(((ord(plainText[i])+ord(key[i])-130)%26)+65)
            cypherText = cypherText + cypherBit
    elif selection =='Q':
        break
    else:
        print("Invalid selection.  Please select 'T','R','V', or 'exit")

encryptedFile = open(fileName[:fileName.index('.')] + '_encrypted.txt','w')
encryptedFile.write(cypherText)
print cypherText
encryptedFile.close()
