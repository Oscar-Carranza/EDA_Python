# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:26:07 2019

@author: Propietario
"""

#Bottom-up (programación dinámica)

#El objetivo de esta estrategia es resolver un problema a partir de subproblemas 
#que ya han sido resueltos. La solución final se forma a partir de la 
#combinación de una o más soluciones que se guardan en una tabla, ésta previene
#que se vuelvan a calcular las soluciones.

#Sucesión de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

#Implementación iterativa
def fibonacci_iterativo(num):
    f1=0
    f2=1
    temp=0
    for i in range(1, num-1):
        temp=f1+f2
        f1=f2
        f2=temp
    return f2

print(fibonacci_iterativo(6))
print("\n")


#Ahora vamos a aplicar la estrategia bottom-up. 
#Partimos del hecho de que ya tenemos las soluciones para: 
#   f(0) = 0
#   f(1) = 1
#   f(2) = 1

def fibonacci_bottom_up(num):
    f_parciales=[0,1,1]
    while len(f_parciales)<num:
        f_parciales.append(f_parciales[-1]+f_parciales[-2])
        print(f_parciales)
    return f_parciales[num-1]

print(fibonacci_bottom_up(6))
print("\n")
