import numpy as np
import math
from string import ascii_letters 

#Formatea la llave de entrada para dejarla de la forma "n n; n n; ..."
#y así poderla ingresar en una matriz de Numpy
def formatKey( key ):

    key = key.split()
    size_key = math.sqrt( len( key ) )

    if not size_key.is_integer():
        print( "Matrix is not square" )
        exit(-1)

    new_key = ""
    numbers = 0
    
    for i in range(1, len( key ) + 1 ):
        if i % size_key != 0:
            new_key += key[i-1] + " "
        else:
            new_key += key[i-1] + "; " 

    return new_key[:len( new_key ) - 2]

#Formate el texto de entrada agregando letras sin importancia para 
#completar los blockes y poder encriptarlos
def formatText( block_size, text ):
    return text + (len( text ) % block_size) * 'x'

#Formatea el texto final para presentación al usuario
def formatSolution( text, block_size ):
    final_text = ""
    for i in range( 1, len( text ) + 1 ):
        final_text += text[i-1].lower()
        if i % block_size == 0:
            final_text += ' '
    
    return final_text

#Cifra o descifra el texto dependiendo de la opción ingresada
#En caso de que descifre lo hara con la inversa de la llave
def hillAlgorithm( text, key, option ):
    matrix_key = np.matrix( key )

    #inv(A) = 1/det(A) * cof(A).T
    #cof(A).T = inv(A) * det(A)
    #k^-1 = d^-1 * adj(k)
    #Para desencriptar se requiere hallar la matriz inversa modular
    #El proceso es parecido a hallar la inversa se debe multiplicar
    #la matriz de cofactores por el inverso modular del determinante
    #de A y sacarle el modulo 26
    if option != '1':
        det_matrix = abs( round( np.linalg.det( matrix_key ), 1 ) )
        cof_matrix = matrix_key.I * det_matrix
        inv_modular = extendedEuclidean( det_matrix, 26 )[1] % 26
        matrix_key = ( cof_matrix * inv_modular ) % 26

    block_size = matrix_key.shape[0]
    text = formatText( block_size, text )

    solution = []

    #Recorre el texto plano en bloques multiplicando cada bloque
    #por la matriz llave
    for i in range( 0, len(text), block_size ):
        codes_letters = []
        for j in range( block_size ):
            codes_letters.append( ascii_letters.find( text[i+j] ) )
        
        vector_block_text = np.array( codes_letters )

        #Multiplica el vector de letras por la llave con modulo 26
        solution_block = np.array(( vector_block_text * matrix_key ) % 26)

        #Recorre el arreglo de numpy para sacar los elementos
        solution += [ ascii_letters[int( round( item, 1 ) )] for item in solution_block[0] ]

    return formatSolution( solution, block_size )
print(ascii_letters[1])

"""
def extendedEuclidean( a, b ):
    if b == 0:
        return (a,1,0)
    (d,s,t) = extendedEuclidean( b, a % b )
    return ( d, t, s - (a/b)*t )
"""

#Algoritmo extendido de eclides
def extendedEuclidean(a,b):
    r = [a,b]
    s = [1,0] 
    t = [0,1]
    i = 1
    q = [[]]
    while (r[i] != 0): 
        q = q + [r[i-1] // r[i]]
        r = r + [r[i-1] % r[i]]
        s = s + [s[i-1] - q[i]*s[i]]
        t = t + [t[i-1] - q[i]*t[i]]
        i = i+1
    return (r[i-1], s[i-1], t[i-1]) 

print( "-----Menu-----" )
print( "1. Cipher text" )
print( "2. Decipher text" )
option = input( "Select the option: " )

if option == '1':
    text = input( "Enter the plain text: " ).replace(" ", "").lower()
else:
    text = input( "Enter the cipher text: " ).replace(" ", "").lower()

key = input( "Enter the key: " )
key = formatKey( key )

solution = hillAlgorithm( text, key, option )
if option == '1':
    print( "The cipher text is: " + solution )
else:
    print( "The plain text is: " + solution )


"""
number theory is easy
11 8 3 7
vk fz rv wt ia zs mi sg ka
11 8 3 7

Attack is tonight
3 10 20 20 9 17 9 4 17
fnw agw jgj kdn rrq
3 10 20 20 9 17 9 4 17

Move the troops tothe north and cut the pass to the enemy
1 8 6 2 5 3 10 20 18 9 17 9 4 17 11 8
ifpf umtc jnvo zars fhpl ewvj odye wczt vqwy rqez ovrd omul
1 8 6 2 5 3 10 20 18 9 17 9 4 17 11 8
"""