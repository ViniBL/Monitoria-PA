import re
nome_arquivo = input()

with open(nome_arquivo) as f:
    texto = f.read()
    nlinhas = len(re.findall('(\n)',texto))
    nvogais = len(re.findall('[aeiouAEIOU]',texto))
    nconsoante = len(re.findall('[b-df-hj-np-tv-xz]',texto))
    ndigito = len(re.findall('\d',texto))
    npontuacao = len(re.findall('[\.\!\,\?\-\:\—\"\(\)\[\]]',texto))
    nespaco = len(re.findall(' ',texto))

tup = (nlinhas,nvogais,nconsoante,ndigito,npontuacao,nespaco)
print(tup)




