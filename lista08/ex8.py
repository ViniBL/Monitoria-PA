def rec(n,ini):
    soma = ini[0]+ini[1]

    i = 1
    anterior = ini[0]
    while i < n:
        temp = soma
        soma = anterior+soma
        anterior = temp
        i += 1
    return anterior
    
print(rec(5,[1,1]))
    
