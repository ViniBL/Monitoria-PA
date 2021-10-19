def min(lista):
    if len(lista)==2:
        if lista[0]>lista[1]:
            return lista[1]
        return lista[0]
    n = min(lista[1:])
    if lista[0]<n:
        return lista[0]
    return n


