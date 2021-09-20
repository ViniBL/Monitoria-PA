l = list()
while True:
    n = input()
    if n == 's':
        break
    l.append(int(n))


m = int(input())
l2 = list()
for i in l:
    if i<m:
        l2.append(i)
        
st = set(l2)

for i in st:
    print(i)
