import requests

cidade = input()
lista = cidade.split('-')
cidade = lista[0]
estado = lista[1]


for i in range(11,99):
    url = 'https://brasilapi.com.br/api/ddd/v1/'+str(i)
    cidades = requests.get(url).json()
    if 'state' in cidades.keys():
        if(cidades['state'] == estado):
            if cidade in cidades['cities']:
                print(i)
                break
