def soma(x,y):
    return x+y

def somaListas(lista1,lista2):

    
    if len(lista1) != len(lista2):
        return None
    for i in range(len(lista2)):
        lista1[i] = lista1[i]+lista2[i]
    return lista1
        

