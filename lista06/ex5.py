import re
s = input()

saida = re.findall('([\w ]+) possui (\d+) .* em ([\w ]+)-(\w+)',s)[0]

saida = list(saida)

saida[1] = int(saida[1])
saida = tuple(saida)
print(saida)
