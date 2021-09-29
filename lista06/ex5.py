import re
s = input()

saida = re.findall('([\w ]+) possui (\d+) .* em ([\w ]+)-(\w+)',s)[0]

print(saida)
