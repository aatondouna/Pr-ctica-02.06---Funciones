def cuadrado(numero):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    numero: Es una lista de números (escribe los numeros dentro [ ].
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    lista = []
    for cuadra in numero:
        lista.append(cuadra**2)
    return lista


