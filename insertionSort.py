def insertionSort (lis):
    for index in range(1, len(lis)):
        actual=lis[index]
        posicion=index
        print("El valor a ordenar : {}".format(actual))
        while posicion>0 and lis[posicion-1]>actual:
            lis[posicion]=lis[posicion-1]
            posicion=posicion-1
        lis[posicion]=actual
        print(lis)
        print()
    return lis