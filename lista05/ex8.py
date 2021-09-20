conj = set()
conj2 = set()

# while True:
#     n = input()
#     if n == 's':
#         break
#     conj.add(int(n))
#     
# while True:
#     n = input()
#     if n == 's':
#         break
#     conj2.add(int(n))
l = list()

conj = {5,4}
conj2 = {4,9,7}


for i in conj:
    l.append(int(i))
        
for i in conj2:
    l.append(int(i))
        
i = 0
while i < len(l)-1:
    if l.count(l[i]) > 1:
        remover = l[i]
        l.remove(remover)
        l.remove(remover)
        i -= 2
    i += 1
        
print(sorted(l))
