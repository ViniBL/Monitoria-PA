def troca(x,n):
    if(x>=0):
        x = bin(x)[2:]
    else:
        x = bin(x)[3:]
        
    x = list(map(int, str(x)))
    x = x[::-1]
    if(x[n] == 0):
        x[n] = 1
    else:
        x[n] = 0
    x = x[::-1]
    out = 0
    for bit in x:
        out = (out << 1) | bit
    
    return out
print(troca(5,2))
