def troca(x,n):
    if(x>=0):
        x = bin(x)[2:]
        negativo = False
    else:
        x = bin(x)[3:]
        negativo = True
        
    x = list(map(int, str(x)))
    x = x[::-1]
    if(x[n] == 0):
        x[n] = 1
    else:
        x[n] = 0
    x = x[::-1]
    x = list(map(str, x))
    
    if(negativo):
        a = "-0"
        b = "b"
        x.insert(0, b)
        x.insert(0,a)
    string = "" 
    
    for element in x:
        string += element
    
