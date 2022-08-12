#BIBLIOTECA MATPLOTLIB responsavel por plotar graficos com os dados obtidos

#essa biblioteca é feita para plotar imagems com python

#ela é muito versatil para esse tipo de aplicação

from cProfile import label
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


# por padrão do matplotlib define autmomaticamnte as cores das linhas de cada grafico
#quando existe muitos graficos sore postos
#porem podemos modificar isso manualmente, vejamos a seguir:

#opções c: cores    -> "r", "b", "g", "o", "k", etc ou "red", "blue", "cyan", etc
# opção ls: linestyle  -> "-", "--", "-.", ":", etc

#podemos ainda usar a opção label para defiir um titulo para cada linha, vejamos a seguir algums
#exemplos
#para usar o label devemos usar o padrão de escrita do latex para adição de simbolos 

plt.figure(2) #criando uma nova imagem com o idenficador 2

plt.plot(x, y1, c="red", ls="-", label=r"$\cos(x)$") #criando o primeiro grafico

plt.plot(x,y2, c="g", ls="-.", label=r"$\cos(2x)$") # criando o grafico dois

plt.plot(x, y3, c="b", ls="--", label=r"$\cos(\frac{x}{2})$") #criando o grafico três

plt.plot(x, y4,c="cyan", ls=":", label=r"$\cos(2x + \frac{\pi}{3})$") #criando o grafico quatro

plt.plot(x, y5, c="k", ls=":", label=r"$\log10(\frac{1}{x})$") #criando o grafico cinco

#definindo um titulo para nosso grafico, temos:
plt.title("funções trigonometricas e log")

#definindo titulo para eixos 
plt.xlabel("x") #titulo para o eixo X
plt.ylabel("f(y)") # titulo para o eixo Y


#comando para aparecer a caixa de legenda na figura
plt.legend(loc="best") #definimos a posição da legenda com o argumento loc

plt.show() #mostrando o grafico que foi feito

plt.close() #libera o espaço de memoria que armazena as figura


# Funções adicionais da biblioteca matplotlib

#plt.scatter() -> faz o plot sem ligar os pontos 
#plt.hist() -> FAz um histograma
#plt.imshow / plt.pcolormesh -> plota imagens em 2D



# Com o matplotlib podemos ainda criar graficos 3D e graficos dinamicos

#usando as funções scatter e hist

plt.figure(3) #criando nova figura

plt.scatter(x, y1) #criar um grafico sem ligar os pontos

plt.hist(x, bins=[0,25,30,60,70]) # criar um hisotgrama (bins, largura da barra )

plt.show()
plt.close()

#verificar depois a função plt.hist() não aprendi a usar corretamente






