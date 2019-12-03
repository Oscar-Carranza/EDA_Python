def factorial_no_recursivo (numero):
    fact=1
    for i in range(numero, 1,-1):
        fact -=1
    return fact

factorial_no_recursivo(6)