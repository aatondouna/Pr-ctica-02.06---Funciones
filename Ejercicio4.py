def media(lista_numero):
 """ Funcion que muestra una lista de numeros y devuelve su media
            Parametros:
                 -lista_numeros: numeros de la lista usados para calcular su media
             Salidas:
            -Devuelve la media de la lita de numeros
"""
 sumatorio = sum(lista_numero)
 media = sumatorio / len(lista_numero)
 return media

lista_numero = []
while True:
    numero = float(input("Introduce una lista de numeros: \n"))
    if numero == 0:
        break
    lista_numero.append(numero)
print(media(lista_numero))
help(media)





