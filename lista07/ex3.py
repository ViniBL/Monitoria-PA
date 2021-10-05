pessoas = {}
while True:
    nome = input()
    if nome == 's':
        break
    idade = input()
    if nome not in pessoas.keys():
        pessoas[nome] = idade
print(pessoas)

