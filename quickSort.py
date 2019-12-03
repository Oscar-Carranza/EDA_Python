def quicksort (lista):
    quicksort_aux(lista,0,len(lista)-1)
    
def quicksort_aux(lista, inicio, fin):
    if inicio<fin:
        pivote=particion(lista, inicio, fin)
        quicksort_aux(lista, inicio, pivote-1)
        quicksort_aux(lista, pivote+1, fin)
        
def particion(lista, inicio, fin):
    #Se asigna como pivote el número de la primera localidad
    pivote=lista[inicio]
    print("Valor del pivote {}".format(pivote))
    #Se crewan dos marcadores
    izquierda=inicio+1
    derecha=fin
    print("Índice izquierdo {}".format(izquierda))
    print("Índice derecho {}".format(derecha))
    
    bandera=False
    while not bandera:
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda= izquierda+1
        while lista[derecha] >= pivote and derecha >= izquierda:
            derecha = derecha-1
        if derecha < izquierda:
            bandera=True
        else:
            temp=lista[izquierda]
            lista[izquierda]=lista[derecha]
            lista[derecha]=temp
   
    print(lista)
    
    temp=lista[inicio]
    lista[inicio]=lista[derecha]
    lista[derecha]=temp
    return  derecha