import re
s = input()

lista = re.findall('(\d+(?:\.\d+)?)',s)

print(lista)
