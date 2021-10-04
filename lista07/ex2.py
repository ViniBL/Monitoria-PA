import ast
pessoas = ast.literal_eval(input("Insira o dicionario: "))
idades = list(pessoas.values())

idades = sorted(idades)
    
if(len(idades) % 2 == 0):
    posA,posB = (len(idades)/2,len(idades)/2+1)
    posA,posB = int(posA),int(posB)
    print((idades[posA]+idades[posB])/2)
    
else:
    pos = int((len(idades)/2))
    print(idades[pos])
    