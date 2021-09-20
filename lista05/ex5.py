l = list()
while True:
    n = input()
    if n == 's':
        break
    l.append(n)

print(any(l.count(i) > 1 for i in l))
