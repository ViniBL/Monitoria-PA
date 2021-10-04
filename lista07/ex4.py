notas = {}
while True:
    nome = input("Insira um nome (ou s para sair): ")
    if nome == 's':
        break
    nota = float(input("Insira a nota: "))
    if nome not in notas.keys():
        notas[nome] = nota
    else:
        temp = notas[nome]
        notas[nome] = (notas[nome]+nota)/2
print(notas)
