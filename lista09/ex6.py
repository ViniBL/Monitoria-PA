def msb(n):
    n = bin(n)
    n = list(n)
    count = 0
    for i in reversed(n):
        if i == 'b':
            return count-1
        count += 1
    