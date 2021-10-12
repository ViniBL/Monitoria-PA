def mdc(a,b):
    n2 = a
    n1 = b
    
    temp = n1%n2
    while temp != 0:
        temp = n2 % n1
        n2 = n1
        n1 = temp
    
    return n2
        
        