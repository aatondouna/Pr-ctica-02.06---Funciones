def binario_a_decimal(binario):
    """
    :param binario: parametro entre (" ")  que expresa el valor en binario
    de un numero.
    :return: retorna el valor en dicimal
    """
    binario = list(binario)
    binario.reverse()
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[i]) * 2 ** i
    return decimal

def decimal_a_binario(decimal):
    """
    :param decimal: un numero natural
    :return: numero natural en binario
    """
    binario = 0
    multiplicador = 1
    while decimal != 0:
        binario = binario + decimal % 2 * multiplicador
        decimal //= 2
        multiplicador *= 10
    return binario
