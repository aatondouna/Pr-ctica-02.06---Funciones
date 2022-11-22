def factorial_recursivo(numero):
    """Función que calcula un factorial en recursiva.

     Parámetros:
         - numero: numero insertado por el usuario

     Salida:
         - factorial: el resultado factorial del numero introducido
     """

    if numero == 0:
        return 1
    else:
        return numero * factorial_recursivo(numero-1)


numero = int(input('ingresa un numero'))
print(factorial_recursivo(numero))
help(factorial_recursivo)


def factorial_bucle(numero):
    """Función que calcula un factorial en bulce iterativo.

        Parámetros:
            - numero: numero insertado por el usuario

        Salida:
            - factorial: el resultado factorial del numero introducido
        """
    factorial = 1
    for num in range(1, numero+1):
        factorial = factorial * num
    return factorial
facto = int(input('Introduce un nunmero:\n'))
print(factorial_bucle(facto))
help(factorial_bucle)