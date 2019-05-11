"""
Read before use:
    There are 3 forms to introduce the key where 'o' are free grills and
    'x' close ones
        1. All the key in one line, for example oxxxxxxxxoxoxxox
        2. Specifing the key matrix size and introducing row per 
            row of the key
                matrix key size = 4
                oxxx
                xxxx
                xoxo
                xxox
        3. Specifing the max index of the row and putting the indixes
            of the grills that make part of the key. Supposing that the key
            is a unidimensional array
                size key = 16
                key = 0 9 11 14
"""

import math

GRILLE_KEY = 'o'
GRILLE_NO_KEY = 'x'

ENCRYPT = '1'
DECRYPT = '2'

#Completa el texto introducido con caracteres sin significado 
# para completar la longitud necesaria
def completeTextLen( text ):
    while math.ceil( math.sqrt( len( text ) ) ) != math.sqrt( len( text ) ):
        text += 'x'
    return text

#Crea la matrix para la llave cuando la llave es pasada 
# toda en una sola linea
def fillKeyOneLine( key, text ):
    matrix_size = math.ceil( math.sqrt( len( text ) ) )
    matrix_key = []
    for i in range( matrix_size ):
        new_row = []
        for j in range( matrix_size ):
            new_row.append( key[i*matrix_size + j] )
        matrix_key.append( new_row )
    return matrix_key

def fillKeyIndexes( indexes, size ):
    index_i = 0
    matrix_size = math.ceil( math.sqrt( size ) )
    matrix = []
    for i in range( matrix_size ):
        matrix.append( [] )
        for j in range( matrix_size ):
            if index_i < len( indexes ) and int(indexes[index_i]) == i*matrix_size + j:
                matrix[i].append('o')
                index_i += 1
            else:
                matrix[i].append('x')
    return matrix

#Crea una matrix cuadrada de tamaño size vacia
def createMatrix( size ):
    matrix = []
    for i in range( size ):
        matrix.append( ['']*size )
    return matrix

#Genera la matriz que contendra el texto encriptado
def generateEncryptedMatrix( text, size ):
    matrix = []
    for i in range( size ):
        matrix.append([])
        for j in range( size ):
            matrix[i].append( text[j+i*size] )
    return matrix

#Función para encriptar con turning grille
def encrypt( text, key, option ):
    #Crea una matriz de tamaño size que va a 
    # contener el texto encriptado
    text_modified = createMatrix( len( key ) )
    #Aplica el algoritmo de giro de la grilla 
    # para encriptar el texto
    text_modified = turningGrille( text, key, option, text_modified )
    return toString( text_modified, option )

#Función para desencriptar con turning grille
def decrypt( text, key, option ):
    text = generateEncryptedMatrix( text, len( key ) )
    #Crea un string que contendra el texto desencriptado
    text_modified = ""
    #Aplica el algoritmo de giro de la grilla 
    # para desencriptar el texto
    text_modified = turningGrille( text, key, option, text_modified )
    return toString( text_modified, option )

#Algoritmo de turning grille para encriptar 
# y desencriptar un texto dado una clave
def turningGrille( text, key, option, text_modified ):
    key_size = len( key )
    index_text = 0
    
    for k in range( 4 ): #Recorre las 4 posiciones de la grilla
        #Contendra la nueva matriz o la matriz girada
        turned_key = createMatrix( key_size ) 
        for i in range( key_size ): 
            for j in range( key_size ):

                if key[i][j] == GRILLE_KEY:#Si hay un hueco en la matriz
                    if option == ENCRYPT:
                        #Si se trata de encriptar entonces en la posición
                        #donde hay un huevo se agrega la letra i del texto
                        #a encriptar
                        text_modified[i][j] = text[index_text]
                        index_text += 1
                    elif option == DECRYPT:
                        #Si se trata de desencriptar se agrega el texto 
                        #en  la posición del hueco a la cadena 
                        text_modified += text[i][j]
                #Se gira la posición i,j de la grilla
                turned_key[i][j] = turnGrille( key, i, j )
        #Se usa la nueva key girada para el mismo proceso
        key = turned_key
    return text_modified

#Función que gira la posición i,j hacia la izquierda
def turnGrille( key, i, j ):
    key_size = len( key ) - 1
    return key[j][key_size-i] #Si se cifra gira hacia la izquierda

#Función que formatea el texto encriptado o desencriptado para
# su presentación al usuario
def toString( text, option ):
    new_text = ""

    if option == ENCRYPT:
        for row in text:
            for col in row:
                new_text += col
            new_text += " "
    elif option == DECRYPT:
        for i in range(len(text)):
            if i % math.ceil( math.sqrt( len( text ) ) ) == 0:
                new_text += " "
            new_text += text[i]
            
    return new_text

key = []

print( "-----Menu-----" )
print( "--------------" )
print( "1. Cipher." )
print( "2. Decipher." )
print( "--------------" )
option = input( "Select option: " )

if option == ENCRYPT:
    text = input( "Enter the plain text: " ).replace(" ","").lower()
elif option == DECRYPT:
    text = input( "Enter the cipher text: " ).replace(" ","").lower()

text = completeTextLen( text )

#Permite recibir la clave tanto en una linea como en multiples lineas
print( "-----key Menu-----" )
print( "--------------" )
print( "1. One line." )
print( "2. Multiple lines." )
print( "3. Indexes of one line key." )
print( "--------------" )
key_option = input( "Select key option: " )

if key_option == '1':
    key = input( "Enter all the key in one line: " ).replace(" ","").lower()
    key = fillKeyOneLine( key, text )
elif key_option == '2':
    size_key = int( input( "Digit the size of the matrix key: " ) )
    for i in range( size_key ):
        row = input( "Enter row matrix key: " ).replace(" ","").lower()
        key.append([])
        for j in row:
            key[i].append( j )
elif key_option == '3':
    size_key = int( input( "Digit the size key: " ) )
    key = fillKeyIndexes( input( "Digit key: " ).strip().split(" "), size_key )

if option == ENCRYPT:
    solution = encrypt( text, key, option )
    print( "\n" )
    print( "The cipher text is: ", solution )
    print( "\n" )
elif option == DECRYPT:
    solution = decrypt( text, key, option )
    print( "\n" )
    print( "\nThe plain text is: ", solution )
    print( "\n" )


#Ejemplos de prueba
"""
1
JIM ATTACKS AT DAWN
2
4
oxxx
xxxx
xoxo
xxox

1
JIM ATTACKS AT DAWN
1
oxxxxxxxxoxoxxox

1
JIM ATTACKS AT DAWN
3
16
0 9 11 14

2
jktdsaatwiamcnat
2
4
oxxx
xxxx
xoxo
xxox

2
jktdsaatwiamcnat
1
oxxxxxxxxoxoxxox

2
jktdsaatwiamcnat
3
16
0 9 11 14
"""
"""
2
TESHN INCIG LSRGY LRIUS PITSA TLILM REENS ATTOG SIAWG IPVER TOTEH HVAEA XITDT UAIME RANPM TLHIE I
2
9
oxxoxoxxx
xxoxxxxxo
xoxxxxoxx
xxoxoxxox
xxxxxxoxo
xxxoxxxox
oxxxxoxxx
xoxxoxxxo
xxoxxxxxx

2
TESHN INCIG LSRGY LRIUS PITSA TLILM REENS ATTOG SIAWG IPVER TOTEH HVAEA XITDT UAIME RANPM TLHIE I
3
81
0 3 5 11 17 19 24 29 31 34 42 44 48 52 54 59 64 67 71 74

1
thisisame sagethati amencrypt ingwithat urninggri lletoprov idethisil lustrativ eexample
2
9
oxxoxoxxx
xxoxxxxxo
xoxxxxoxx
xxoxoxxox
xxxxxxoxo
xxxoxxxox
oxxxxoxxx
xoxxoxxxo
xxoxxxxxx

1
thisisame sagethati amencrypt ingwithat urninggri lletoprov idethisil lustrativ eexample
3
81
0 3 5 11 17 19 24 29 31 34 42 44 48 52 54 59 64 67 71 74
"""