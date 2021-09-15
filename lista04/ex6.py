import math

l = list()
l2 = list()
while True:
    n = input()
    if(n == 's'):
        break
    l.append(int(n))
    
escolha = input()

if (escolha == '1'):
    l2 = list((int(math.factorial(l[i]))) for i in range (0,len(l)))
if (escolha == '2'):
    l2 = list((int(math.sqrt(l[i]))) for i in range (0,len(l)))
print(l2)