import re
s = input()

lista = re.findall('\d+',s)

lista = [float(i) for i in lista]
print(lista)
