def map(lista,funcao):
    for i in range(len(lista)):
        lista[i] = funcao(lista[i])
    return lista

