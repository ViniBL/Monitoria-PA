l = int(input())
c = int(input())
m = []
n = []
r = []

for i in range(l):
    a = []
    for j in range(c):
        a.append(int(input()))
    m.append(a)
    
for i in range(l):
    b = []
    for j in range(c):
        b.append(int(input()))
    n.append(b)
    
for i in range(l):
    d = []
    for j in range(c):
        d.append(m[i][j]+n[i][j])
    r.append(d)
    


        
    
print(r)

