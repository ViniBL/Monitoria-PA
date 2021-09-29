s = input()
s = s.strip()
s = s.split(' ')
s = list(s)
s = map(lambda x: int(x),s)
s = sorted(s)
for linha in s:
    print(linha)