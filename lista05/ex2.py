l = int(input())
c = int(input())
m = []

for i in range(l):
    a = []
    for j in range(c):
        a.append(int(input()))
    m.append(a)

n = []
for i in range(c):
    b = []
    for j in m:
        b.append(j[i])
    n.append(b)


print(n)
    


