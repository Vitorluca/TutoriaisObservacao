#arrays são vetores da biblioteca numpy

import numpy as pess #essa linha define que importamos numpy e que para usarmos ele digitamos np

array1 = pess.array([1,2,3,4,5])
array2 = pess.array([6,7,8,9,10])

array3 = array1 + array2 #quando somamos dois arrays temos como resultado a soma de cada elemento desse array com o elemento correspondente do outro array

print(array1, array2, array3) #exibe o resultado

print("\n")

#array3 = array1 * 15.148 #com os arrays podemos somar cada elemento da sequencia a um int/float

array3 = array1 * array2

print(array1, array2, array3)