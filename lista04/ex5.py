l = list()

while True:
    n = input()
    if n == 's':
        break
    l.append(int(n))

m = int(input())
l2 = list()
l2 = [0] * m
for n in range(len(l)):
    posicao = n%m
    l2[posicao] = l2[posicao]+l[n]
    
print(l2)
    