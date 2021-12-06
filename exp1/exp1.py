import math
import numpy as np

def chooseOption(i,Text):
    switcher = {
        1: substitution,
        2: rot13,
        3: transpose,
        4: double_transposition,
        5: vernam_cipher
    }
    switcher[i](Text)

def vernam_cipher(Text):

    key = input('Enter the key(NOTE: to be of the same length as the message):')
    while(len(key)!=len(Text)):
        print("Please enter the key of the same")
        key = input('Enter the key(NOTE: to be of the same length as the message):')

  
    encryptedText = ''
    for i in range(len(Text)):
        if Text[i] == ' ':
            encryptedText+=' '
        else:
            encryptedText += chr(((ord(Text[i])-65)^(ord(key[i])-65))+65)
    print('encrypted Text is as follows :',encryptedText)


    decryptedText = ''
    for i in range(len(encryptedText)):
        if Text[i]== ' ':
            decryptedText+=' '
        else:
            decryptedText += chr(((ord(encryptedText[i]) - 65)^(ord(key[i]) - 65)) + 65)
    print('decrypted Text is as follows :',decryptedText)
    return 

def substitution(Text):
    posShift = int(input('Enter the no. of Position shift: '))

    encryptedText = ''
    for char in Text:
        #check if its capital or small
        if(char.isupper()):
            encryptedText += chr((ord(char) + posShift-65) % 26 + 65)
        else:
            if char == ' ':
                encryptedText += ' '
            else:
                encryptedText += chr((ord(char) + posShift-97) % 26 + 97)
    print('encrypted Text is as follows :',encryptedText)

    decryptedText = ''
    for char in encryptedText:
        #check if its capital or small
        if(char.isupper()):
            decryptedText += chr((ord(char) - posShift-65) % 26 + 65)
        else:
            if char == ' ':
                decryptedText += ' '
            else:
                decryptedText += chr((ord(char) - posShift-97) % 26 + 97)
    print('decrypted Text is as follows :',decryptedText)
    return

def transpose(plainText):
    key = input('Enter the key: ')
    key.upper()
    order = sorted(list(key))
    col = len(key)

    # Encryption
    msg_len = len(plainText)
    msg_list = list(plainText)
    row = int(math.ceil(msg_len/col))
    null_values = row*col - msg_len
    msg_list.extend('_'*null_values)
    matrix = np.array(msg_list).reshape(row,col)
    encryptedText = ''
    
    for i in range(col):
        index = key.index(order[i])
        encryptedText += ''.join([row[index] for row in matrix])
    print('Encrypted Text is as follows:',encryptedText)

    # Decryption
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
    print('Decrypted Text is as follows:',decryptedText)
    return 
def rot13(Text):
    # 13 is the shift (predefined)
    encryptedText = ''

    for char in Text:
        if(char.isupper()):
            encryptedText += chr((ord(char) + 13 - 65) % 26 + 65)
        else:
            if char == ' ':
                encryptedText+=' '
            else:
                encryptedText += chr((ord(char) + 13 - 97) % 26 + 97)
    print('encrypted Text is as follows :',encryptedText)


    decryptedText = ''

    for char in encryptedText:
        if(char.isupper()):
            decryptedText += chr((ord(char) + 13 - 65) % 26 + 65)
        else:
            if char == ' ':
                decryptedText += ' '
            else:
                decryptedText += chr((ord(char) + 13 - 97) % 26 + 97)
    print('decrypted Text is as follows :',decryptedText)
    return
def double_transposition(plainText):
    key1 = input('\nEnter the first key for encrytopn: ')
    key2 = input('Enter the second key for encryption: ')
    key1.upper()
    key2.upper()
    order1 = sorted(list(key1))
    order2 = sorted(list(key2))
    col1 = len(key1)
    col2 = len(key2)

    ## Encryption
    msg_len = len(plainText)
    msg_list = list(plainText)
    row1 = int(math.ceil(msg_len/col1))
    null_values1 = row1*col1 - msg_len
    msg_list.extend('_'*null_values1)
    matrix = np.array(msg_list).reshape(row1,col1)
    middleText,encryptedText = '',''

    for i in range(col1):
        index = key1.index(order1[i])
        middleText += ''.join([row1[index] for row1 in matrix])
    print("Single encrypted as follows :",middleText)

    middle_msg_len = len(middleText)
    middle_msg_list = list(middleText)
    row2 = int(math.ceil(middle_msg_len/col2))
    null_values2 = row2*col2 - middle_msg_len
    middle_msg_list.extend('_'*null_values2)
    matrix = np.array(middle_msg_list).reshape(row2,col2)
    
    for i in range(col2):
        index = key2.index(order2[i])
        encryptedText += ''.join([row2[index] for row2 in matrix])
    print('Double encrypted as follows:',encryptedText)

    ## Decryption
    encryptedText_lst = list(encryptedText)
    middleText,decryptedText = '',''
    pointer = 0
    dec_matrix = np.array([None]*len(encryptedText)).reshape(row2,col2)
    for i in range(col2):
        index = key2.index(order2[i])
        for j in range(row2):
            dec_matrix[j,index] = encryptedText_lst[pointer]
            pointer += 1

    middleText = ''.join(''.join(col for col in row) for row in dec_matrix)
    if null_values2 > 0:
        middleText = middleText[:-null_values2]
    pointer = 0
    print('Single decrypted as follows :',middleText)

    middletxt_lst = list(middleText)
    dec_matrix = np.array([None]*len(middleText)).reshape(row1,col1)
    for i in range(col1):
        index = key1.index(order1[i])
        for j in range(row1):
            dec_matrix[j,index] = middletxt_lst[pointer]
            pointer += 1
    if null_values1 > 0:
        decryptedText = decryptedText[:-decryptedText.count('_')]
    decryptedText = ''.join(''.join(col for col in row) for row in dec_matrix)
    decryptedText = decryptedText[:-decryptedText.count('_')]
    print('Double decrypted as follows:',decryptedText)
    return
while(True):
    print("1.Substitution Method\n2.Rot13 Method\n3.Transpose Method\n4.Double Transposition Method\n5.Vernam Cipher Method\n0.For exiting")
    choice = int(input("Enter your option: "))
    if choice ==0:
        break
    Text = input('\nEnter Plain text to be encrypted: ')
    chooseOption(choice,Text)
print("Thanks for encrypting decrypting")