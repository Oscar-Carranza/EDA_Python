# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:38:32 2019

@author: Propietario
"""

#Top-down

#Aquí se empiezan a hacer los cálculos de n hacia abajo
#Además, se aplica una técnica llamada memoización la cual consiste en guardar
#los resultados previamente calculados, de tal manera que no se tengan que
#repetir operaciones.

#Para aplicar la estrategia top-down, se utiliza un diccionario (memoria) el
#cual va a almacenar valores previamente calculados. 

#memoria inicial
memoria={1:0, 2:1, 3:1}

def fibonacci_iterativo(num):
    f1=0
    f2=1
    temp=0
    for i in range(1, num-1):
        temp=f1+f2
        f1=f2
        f2=temp
    return f2


def fibonacci_top_down(num):
    if num in memoria:
        return memoria[num]
    f=fibonacci_iterativo(num-1)+fibonacci_iterativo(num-2)
    memoria[num]=f
    return memoria[num]

#La deficiencia de este algoritmo es que hay cálculos que es están repitiendo.
#La ventaja, es que una vez que ya se calcularon, se guardan en una memoria,
#que en este caso es un diccionario; en dado caso de que se necesite un valor
#que ya ha sido calculado, sólo regresa y ya no se realizan los cálculos.
    
print(fibonacci_top_down(12))
print (memoria)
