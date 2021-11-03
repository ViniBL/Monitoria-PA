def bit(x,n):
    count = 0
    if(x>=0):
        x = bin(x)[2:]
    else:
        x = bin(x)[3:]
        
    x = list(map(int, str(x)))
    for i in reversed(x):
        if count == n:
            return i
        count += 1
        