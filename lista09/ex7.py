def zeros(n):
    zero = 0
    if(n>=0):
        n = bin(n)[2:]
    else:
        n = bin(n)[3:]
    n = list(map(int, str(n)))
    for i in reversed(n):
        if i == 0:
            zero += 1
        else:
            break
    return zero
            