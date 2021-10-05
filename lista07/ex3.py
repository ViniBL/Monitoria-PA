pessoas = {}
while True:
    nome = input()
    if nome == 's':
        break
    idade = int(input())
    if nome not in pessoas.keys():
        pessoas[nome] = idade
print(pessoas)

