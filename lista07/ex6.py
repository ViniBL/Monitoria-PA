import requests

cidade = input()
lista = cidade.split('-')
if(len(lista)>2):
    cidade = lista[0]+"-"+lista[1]
    estado = lista[2]
else:
    cidade = lista[0]
    estado = lista[1]


cidade = cidade.upper()

for i in range(11,99):
    url = 'https://brasilapi.com.br/api/ddd/v1/'+str(i)
    cidades = requests.get(url).json()
    if 'state' in cidades.keys():
        if(cidades['state'] == estado):
            if cidade in cidades['cities']:
                print(i)
                break
