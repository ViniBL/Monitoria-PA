nome_arquivo = input()

with open(nome_arquivo) as f:
    string = f.readlines()

f.close()

string = [row.rstrip('\n') for row in string]

string = string[::-1]

with open(nome_arquivo,'w') as f:
    for x in string:
        f.write(x + "\n")




