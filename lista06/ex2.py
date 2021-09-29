import re
s = input()

lista = re.findall('([0-9]*[.])?[0-9]+',s)

lista = [float(i) for i in lista]
print(lista)
