#BIBLIOTECA MATPLOTLIB responsavel por plotar graficos com os dados obtidos

#essa biblioteca é feita para plotar imagems com python

#ela é muito versatil para esse tipo de aplicação

import numpy as np #como chamaremos a biblioteca
import matplotlib.pyplot as plt #como chamaremos a biblioteca

# .pyplot modulo para plotar imagem s em python, isso nos evita que chamemos toda a biblioteca
#sem necessidade

#criando dados para serem visualizados
#usando a função linspace

#eixo X dos dados 
x = np.linspace(0,7, 101) #start = 0, stop = 7, number = 101 numeros no array

#fazendo os eixos Y, temos:
y1 = np.cos(x)
y2 = np.cos(2*x)
y3 = np.cos(x/2)
y4 = np.sin(2*x + np.pi/3)
y5 = np.log10(1/x)

#porcesso de criação de um grafico em python

#Criando um grafico com Matplotlib  em python
#inicialmente precisamos criar uma figura que será responsavel por abrigar os graficos
#para isso usamos a seguinte função plt.figure essa função recebe como argumento um numero
#que é o idenficador da figura
#caso tivermos varias figuras abertas teremos elas separadas em cada janela
plt.figure(0) #criando uma figura com idetificador 0

#agora devemos usar o comando .plot para construir o grafico
#devemos passar os valores de x,y como argumento para a função .plot
plt.plot(x, y1)

#Agora para visualizar a figura usamos o comando plt.show
plt.show()

#apos terminarmos de visualizar o grafico e uma boa pratica de programação pecharmos a figura
#para desocupar esse espaço de memoria
plt.close()


# função exit()
#no ponto que é inserida indaica o fim do arquivo python que será executado
#exit()


#podemos plotar varios graficos em uma mesma figura, vejamos a seguir:

plt.figure(1) #criando uma nova figura com indice 1
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(x, y5)
#criando os 5 graficos em uma mesma figura

# podemos adicionar algumas anotações ao grafico para que ele fique mais legivel
#podemos adicional: Titulo, e legenda dos eixos. Podemos usar o padrão do Latex para
#inserir letras gregas e outros simbolos(elas devem ser passadas como um rawstring para que
# o Latex funcione)

# string -> "sou uma string"
#rawstring -> r"sou uma raw string"

#raw string = string bruto, trata uma barra invertida na string como um caractere normal
# em vez de tratalo como caractere de escape

plt.show()
plt.close()








