import ast
pessoas = ast.literal_eval(input())
chaves = list(pessoas.keys())
json = True
for i in chaves:
    if type(i) != str:
        json = False

print(json)
        