#usando as funções basicas da biblioteca astropy
#introdução a biblioteca astropy

#from sqlite3 import Time
from turtle import pensize
import matplotlib.pyplot as plt
import numpy as np

#importando os modulos do astropy

from astropy import units as u # modulo das unidades
from astropy.time import  Time #modulo do tempo geografico
from astropy.coordinates import SkyCoord, Distance, EarthLocation, AltAz, get_sun #modulos das coordenadas

#definindo a angulação de observação

ra1 = 30*u.deg #converte o valor em graus
dec1 = 30*u.deg #converte o valor em graus

#criando um objeto para armazenar esses dados
print("Objeto numero 1")
obj1 = SkyCoord(ra=ra1, dec=dec1) #criando um objeto que representa um astro celeste

print(obj1) #mostrando os atributos do objeto

print("\n")
#mostrando a longitude e latitude separadamente
print("RA") #longitude do objeto
print(obj1.ra)

#latitude do objeto
print("DEC")
print(obj1.dec)


#Exibindo em graus o obj1.ra

print("RA em deg(graus")
print(obj1.ra.degree) #converte a corrdenada em coordenada em graus

#exibindo RA em horas

print("RA em horas")
print(obj1.ra.hour) #converte as coordenadas emcoordenadas horarias

#exibindo DEC em uma string
print("DEC em string: ")
print(obj1.to_string("hmsdms")) # não sei o que faz

# fazendo uma mudança nas cordenadas

print("\n\nRelacionando referencias")
print("FK5") #sistema de coordenadas
print(obj1.transform_to("fk5")) #trasforma as coordenadas do obj1 em coordenadas fk5


#CRIANDO OUTRO OBJETO

#fazendo um teste para verificar se o nome interere em alguma coisa
obj2_name = "SOL" # maneira de atribuir nome a um objeto no astropy
print("\n")

