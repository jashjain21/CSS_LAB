import math
import numpy as np

def substitution(Text):
    posShift = int(input('Enter the no. of Position shift: '))

    encryptedText = ''
    for char in Text:
        #check if its capital or small
        if(char.isupper()):
            encryptedText += chr((ord(char) + posShift-65) % 26 + 65)
        else:
            encryptedText += chr((ord(char) + posShift-97) % 26 + 97)
    print('Encrypted Text is as follows :',encryptedText)

    decryptedText = ''
    for char in encryptedText:
        #check if its capital or small
        if(char.isupper()):
            decryptedText += chr((ord(char) - posShift-65) % 26 + 65)
        else:
            decryptedText += chr((ord(char) - posShift-97) % 26 + 97)
    print('Decrypted Text is as follows :',decryptedText)

def rot13(Text):
    # 13 is the shift (predefined)
    encryptedText = ''

    for char in Text:
        if(char.isupper()):
            encryptedText += chr((ord(char) + 13 - 65) % 26 + 65)
        else:
            encryptedText += chr((ord(char) + 13 - 97) % 26 + 97)
    print('Encrypted Text is as follows :',encryptedText)


    decryptedText = ''

    for char in encryptedText:
        if(char.isupper()):
            decryptedText += chr((ord(char) + 13 - 65) % 26 + 65)
        else:
            decryptedText += chr((ord(char) + 13 - 97) % 26 + 97)
    print('Decrypted Text is as follows :',decryptedText)

def transpose(Text):

    key = input('Enter the key:')
    key.upper()
    order = sorted(list(key))
    col = len(key)


    text_len = len(Text)
    text_list = list(Text)
    row = int(math.ceil(text_len/col))
    null_values = row*col - text_len
    text_list.extend('_'*null_values)
    matrix = np.array(text_list).reshape(row,col)
    encryptedText = ''
    for i in range(col):
        index = key.index(order[i])
        encryptedText += ''.join([row[index] for row in matrix])
    print('Encrypted Text:',encryptedText)


    encryptedText_lst = list(encryptedText)
    decryptedText = ''
    pointer = 0
    dec_matrix = np.array([None]*len(encryptedText)).reshape(row,col)
    for i in range(col):
        index = key.index(order[i])
        for j in range(row):
            dec_matrix[j,index] = encryptedText_lst[pointer]
            pointer += 1
    decryptedText = ''.join(''.join(col for col in row) for row in dec_matrix)
    decryptedText = decryptedText[:-decryptedText.count('_')]
    print('Decrypted Text:',decryptedText)

def double_transposition(Text):
    key = input('Enter the key:')
    key.upper()
    order = sorted(list(key))
    col = len(key)


    text_len = len(Text)
    text_list = list(Text)
    row = int(math.ceil(text_len/col))
    null_values = row*col - text_len
    text_list.extend('_'*null_values)
    matrix = np.array(text_list).reshape(row,col)
    middleText,encryptedText = '',''

    for i in range(col):
        index = key.index(order[i])
        middleText += ''.join([row[index] for row in matrix])
    print("Single Encryption is as follows :",middleText)

    middletxt_lst = list(middleText)
    matrix = np.array(middletxt_lst).reshape(row,col)
    for i in range(col):
        index = key.index(order[i])
        encryptedText += ''.join([row[index] for row in matrix])
    print('Double Encryption is as follows :',encryptedText)


    encryptedText_lst = list(encryptedText)
    middleText,decryptedText = '',''
    pointer = 0
    dec_matrix = np.array([None]*len(encryptedText)).reshape(row,col)
    for i in range(col):
        index = key.index(order[i])
        for j in range(row):
            dec_matrix[j,index] = encryptedText_lst[pointer]
            pointer += 1

    middleText = ''.join(''.join(col for col in row) for row in dec_matrix)
    pointer = 0
    print('Single Decryption is as follows :',middleText)

    middletxt_lst = list(middleText)
    dec_matrix = np.array([None]*len(middleText)).reshape(row,col)
    for i in range(col):
        index = key.index(order[i])
        for j in range(row):
            dec_matrix[j,index] = middletxt_lst[pointer]
            pointer += 1
    decryptedText = decryptedText[:-decryptedText.count('_')]
    decryptedText = ''.join(''.join(col for col in row) for row in dec_matrix)
    decryptedText = decryptedText[:-decryptedText.count('_')]
    print('Double Decryption is as follows :',decryptedText)


def vernam_cipher(Text):

    key = input('Enter the key(NOTE: to be of the same length as the message):')
    while(len(key)!=len(Text)):
        print("Please enter the key of the same")
        key = input('Enter the key(NOTE: to be of the same length as the message):')

  
    encryptedText = ''
    for i in range(len(Text)):
        encryptedText += chr(((ord(Text[i])-65)^(ord(key[i])-65))+65)
    print('Encrypted Text is as follows :',encryptedText)


    decryptedText = ''
    for i in range(len(encryptedText)):
        decryptedText += chr(((ord(encryptedText[i]) - 65)^(ord(key[i]) - 65)) + 65)
    print('Decrypted Text is as follows :',decryptedText)

def chooseOption(i,Text):
    switcher = {
        1: substitution,
        2: rot13,
        3: transpose,
        4: double_transposition,
        5: vernam_cipher
    }
    switcher[i](Text)

print("1. Substitution Method\n2. Rot13 Method\n3. Transpose Method\n4. Double Transposition Method\n5. Vernam Cipher Method")
choice = int(input("Enter your option: "))
Text = input('\nEnter Plain text to be encrypted: ')
chooseOption(choice,Text)