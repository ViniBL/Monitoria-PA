l = list()
l1 = list()
l2 = list()

while True:
    n = input()
    if(n == 's'):
        break
    l.append(int(n))
    
while True:
    n = input()
    if(n == 's'):
        break
    l1.append(int(n))

for e in l:
    if e in l1:
       l2.append(e)  
    
print(l2)


