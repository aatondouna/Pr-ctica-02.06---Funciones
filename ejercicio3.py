def area_circulo(rad):
    """
    :param rad: el radio de el circulo
    :return: ejecuta el calculo del area de un circulo
    """
    pi = 3.14
    return pi * rad ** 2


def volumen_cilindro(rad, alt):
    """
    :param rad: el radio de el circulo
    :param alt: la altura de un cilindro
    :return: ejecuta el calculo del volumen
    """
    return area_circulo(rad)*alt
