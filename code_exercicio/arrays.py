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

start = 157 #valor de inicio da sequencia
stop = 645
step = 2

#usando o comando range do python
print("\n")


list_range = list(range(start, stop, step))


print(list_range)


#usando o comando pess.arange da biblioteca numpy

array_arange = pess.arange(start, stop, step)


print(array_arange)

# aprincipal diferença entre np.arange e renge e que arenge trabalha com numeros float e renge
# apenas com inteiros


#usando a função linspace
#a principal diferença entre a função linspace e as funções arenge e renge é:
#na linspace temos a seguinte estrutura: (start,stop, number)
#onde start e o numero que inicia a sequencia, stop define o numero de parada, e number indica
#a quantidade de pontos que existirão dentro do intervalo estipulado, alterando assim
#automaticamente o tamanho de cada numero, vejamos:

number = 1000 #numeros de pontos que devem existir no array linspace

array_linspace = pess.linspace(start, stop, number)

print("\n\n\n")

print(array_linspace) #O linspace inclui o numero de stop diferente entre o arange e range


#metodos para obter novos arrays e para obtermos informações sobre eles

#array basico 
array_basico = pess.arange(0,10,1) # start = 2, stop = 200, step = 1.25

print("\n\n")

print(array_basico) #array basico

#dimenções de uma lista em python usamos a função len()
#dimenções de um array na biblioteca Numy usamos a função .shape

# .shape - indica o tamanho do array, vejamos: 


print("\n")

print(array_basico.shape)

#pegado a primeira dimenção de um array

print("\n")

print(array_basico.shape[0]) #pega apenas a primeira dimenção do shape


#podemos remodelar um array com a função .reshape

dimencao = [2,5]

array_bidimencional =  array_basico.reshape(dimencao) # Modificando as dimenções do array original

print(array_bidimencional) #o numero de elementos do array original é prezervado
#mudando apenas sua organização


#Operações matematicas com Numpy

#A biblioteca numpy ofereça uma variedade de operações matematicas
#outra liberdade que ele nos dá é a possibilidade de aplicar essas operações matematicas
#em numeros (int, float) e em arrays inteiros

#vejamos algums exemplos:

#usando log:
operacao1 = pess.log10(45.587)
print("\n")
print(operacao1)

#fazendo log para arrays:
operacao1 = pess.log10(array_bidimencional)
print("\n")
print(operacao1)

#calculando o cosseno:

operacao2 = pess.cos(25)
print("\n")
print(operacao2)

#calculando o cosseno para um array

operacao2 = pess.cos(array_basico)
print("\n")
print(operacao2)












 