from string import ascii_letters 

dict_letters = {}
table = [[]]

def modifyKey( key ):
    new_key = ""
    for i in range( len( key ) ):
        if key[i] == ' ':
            continue
        new_key += key[i].upper()
    
    return new_key

def modifyPlainText( plain_text ):
    new_plain_text = ""
    for i in range( len( plain_text ) ):
        if plain_text[i] == ' ':
            continue
        if plain_text[i] == 'J':
            new_plain_text += 'I'
            continue
        new_plain_text += plain_text[i].upper()
        if i < len( plain_text ) - 1 and plain_text[i] == plain_text[i+1]:
            new_plain_text += 'X'
    
    if len( new_plain_text ) % 2 == 1:
        new_plain_text += 'X'
    
    return new_plain_text

def modifyCipherText( cipher_text ):
    new_cipher_text = ""
    for i in range( len( cipher_text ) ):
        if cipher_text[i] == ' ':
            continue
        new_cipher_text += cipher_text[i].upper()
    
    return new_cipher_text

def generateTable( key ):
    index = 0
    i = 0

    letters_key = modifyKey( key ) + ascii_letters.upper()

    for letter in letters_key:
        if letter in dict_letters:
            continue
        elif letter == 'J' or letter == 'I':
            dict_letters['I'] = 'I'
            dict_letters['J'] = 'J'
            table[index].append('I')
            i += 1
        else:
            dict_letters[letter] = letter
            table[index].append(letter)
            i += 1
        if i % 5 == 0:
            table.append([])
            index += 1

def cipherText( plain_Text ):
    plain_text = modifyPlainText( plain_Text )
    cipher_text = ""

    for i in range(0, len( plain_text ), 2 ):
        point1 = (0,0)
        point2 = (0,0)
        for j in range( 5 ):
            for k in range( 5 ):
                if plain_text[i] == table[j][k]:
                    point1 = (j,k)
                if plain_text[i+1] == table[j][k]:
                    point2 = (j,k)

        if point1[0] == point2[0]:
            cipher_col1 = point1[1]+1
            cipher_col2 = point2[1]+1

            if point1[1] == 4:
                cipher_col1 = 0
            if point2[1] == 4:
                cipher_col2 = 0

            cipher_text += table[point1[0]][cipher_col1]
            cipher_text += table[point2[0]][cipher_col2]
            cipher_text += ' '
        elif point1[1] == point2[1]:
            cipher_row1 = point1[0]+1
            cipher_row2 = point2[0]+1

            if point1[0] == 4:
                cipher_row1 = 0
            if point2[0] == 4:
                cipher_row2 = 0
                
            cipher_text += table[cipher_row1][point1[1]]
            cipher_text += table[cipher_row2][point2[1]]
            cipher_text += ' '
        else:
            cipher_text += table[point1[0]][point2[1]]
            cipher_text += table[point2[0]][point1[1]]
            cipher_text += ' '    
    
    return cipher_text

def decipherText(cipher_text):
    cipher_text = modifyCipherText( cipher_text )
    decipher_text = ""

    for i in range(0, len( cipher_text ), 2 ):
        point1 = (0,0)
        point2 = (0,0)
        for j in range( 5 ):
            for k in range( 5 ):
                if cipher_text[i] == table[j][k]:
                    point1 = (j,k)
                if cipher_text[i+1] == table[j][k]:
                    point2 = (j,k)

        if point1[0] == point2[0]:
            cipher_col1 = point1[1]-1
            cipher_col2 = point2[1]-1

            if point1[1] == 0:
                cipher_col1 = 4
            if point2[1] == 0:
                cipher_col2 = 4

            decipher_text += table[point1[0]][cipher_col1]
            decipher_text += table[point2[0]][cipher_col2]
            decipher_text += ' '
        elif point1[1] == point2[1]:
            cipher_row1 = point1[0]-1
            cipher_row2 = point2[0]-1

            if point1[0] == 0:
                cipher_row1 = 4
            if point2[0] == 0:
                cipher_row2 = 4
                
            decipher_text += table[cipher_row1][point1[1]]
            decipher_text += table[cipher_row2][point2[1]]
            decipher_text += ' '
        else:
            decipher_text += table[point1[0]][point2[1]]
            decipher_text += table[point2[0]][point1[1]]
            decipher_text += ' '    
    
    return decipher_text

print( "-----Menu-----" )
print( "1. Cipher text" )
print( "2. Decipher text" )
option = input( "Select the option: " )

if option == '1':
    key = input( "Enter the key: " )
    plain_text = input( "Enter the plaintext: " )

    generateTable( key )
    print ( "Cipher text: " + cipherText( plain_text ) )
else:
    key = input( "Enter the key: " )
    cipher_text = input( "Enter the ciphertext: " )

    generateTable( key )
    print ( "Decipher text: " + decipherText( cipher_text ) )

#playfair example - key
#BM OD ZB XD NA BE KU DM UI XM MO UV IF - cipher text
#Hide the gold in the tree stump - plain text

#hello world - key
#hide the gold - plain text
#LF GD NW DP WO AV - cipher text

