notas = {}
n_vezes = {}
while True:
    nome = input()
    if nome == 's':
        break
    nota = float(input())
    if nome not in notas.keys():
        notas[nome] = nota
    else:
        notas[nome] = notas[nome]+nota
        if nome not in n_vezes.keys():
            n_vezes[nome] = 2
        else:
            n_vezes[nome] = n_vezes[nome]+1
for i in notas.keys():
    if i in n_vezes.keys():
        notas[i] = notas[i]/n_vezes[i]
print(notas)
