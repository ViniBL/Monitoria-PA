arquivo1 = input()
arquivo2 = input()
arquivo3 = input()

with open(arquivo1) as f:
    lista1 = f.readlines()

f.close()

lista1 = [row.rstrip('\n') for row in lista1]

with open(arquivo2) as f:
    lista2 = f.readlines()

lista2 = string = [row.rstrip('\n') for row in lista2]
    
f.close()

lista3 = sorted(list(set(lista1) | set(lista2)))

with open(arquivo3,'w') as f:
    for x in lista3:
        f.write(x + "\n")
        






