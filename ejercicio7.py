def cadenacaracter(palabras):
    palabras = palabras.split(" ")
    dic = {}
    for palabra in palabras:
        if palabra in dic:
            dic[palabra] +=1
        else:
            dic[palabra] = 1
    return dic
