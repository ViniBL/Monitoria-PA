from re import findall
s = input()

saida = findall('([\w ]+) possui (\d+) .* em ([\w ]+)-(\w+)',s)

print(saida)