# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:04:53 2019

@author: Propietario
"""

#PROBLEMA DE CAMBIO DE MONEDAS

#El problema consiste en regresar el cambio de monedas, de cierta denominación, 
#usando el menor número de éstas. Este problema se resuelve escogiendo
#sucesivamente las monedas de mayor valor hasta que ya no se pueda seguir
#usándolas y cuando esto pasa, se utiliza la siguiente de mayor valor. 
#La desventaja en esta solución es que, si no se da la denominación de monedas
#en orden de mayor a menor, se resuelve el problema, pero no de una manera óptima.


#Divisón entre entero usando el operador //
#Por ejemplo:
#   5/2 = 2.5
#   5//2 = 2


def cambio (cantidad, denominaciones):
    resultado=[]
    while(cantidad>0):
        if(cantidad>=denominaciones[0]):
            num=cantidad//denominaciones[0]
            cantidad=cantidad-(num*denominaciones[0])
            resultado.append([denominaciones[0], num])
        denominaciones=denominaciones[1:]
    return resultado


#Pruebas del algoritmo
print(cambio(1000, [500,200,100,50,20,5,1]))
print("\n")
print(cambio(500, [500,200,100,50,20,5,1]))
print("\n")
print(cambio(300, [50,20,5,1]))
print("\n")
print(cambio(200, [5]))
print("\n")
print(cambio(98, [50,20,5,1]))
print("\n")
##En el siguiente ejemplo no regresa la solución óptima, si no existiera la 
#moneda de valor 1, la solución fallaría
print(cambio(98, [5,20,1,50]))
        