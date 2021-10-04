pessoas = {}
while True:
    nome = input("Insira um nome (ou s para sair): ")
    if nome == 's':
        break
    idade = input("Insira a idade: ")
    if nome not in pessoas.keys():
        pessoas[nome] = idade
print(pessoas)

