def menor(lista):
    posicoes = []
    menor = lista[0]
    posicoes.append(0)
    for i in range(1,len(lista)):
        if(lista[i]<menor):
            posicoes.clear()
            menor = lista[i]
        if(menor == lista[i]):
            posicoes.append(i)

    tupla = (menor,posicoes)
    return tupla



