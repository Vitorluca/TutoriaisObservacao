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


#multiplicando um inteiro por array


array3 = array2 * 2
print("\n")

print(array3)

#funções para trabalhar com array


# função np.arange produz uma sequencia de numeros em python
#no.range(start, stop, step), onde start é o numero que inicia a sequencia 
#stop é o numero de parada da sequencia(ele não é incluido na lista)
#step indica o tamanho do passo entre cada valor da sequencia 

#o comando np.range não produz listar precisamos usar o comando list() para trasformalo

start = 500 #valor de inicio da sequencia
stop = 1000
step = 1.9

#usando o comando range do python
print("\n")


list_range = list(range(start, stop, step))


print(list_range)


#usando o comando pess.arange da biblioteca numpy

array_arange = pess.arange(start, stop, step)


print(array_arange)

# aprincipal diferença entre np.arange e renge e que arenge trabalha com numeros float e renge
# apenas com inteiros



