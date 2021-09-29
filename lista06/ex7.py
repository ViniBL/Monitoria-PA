import re
nome_arquivo = input()

with open(nome_arquivo) as f:
    texto = f.read()
    nlinhas = len(re.findall('(\n)',texto))+1
    nvogais = len(re.findall('[aeiouAEIOU]',texto))
    nconsoante = len(re.findall('[b-df-hj-np-tv-xzB-DF-HJ-NP-TV-XZ]',texto))
    ndigito = len(re.findall('\d',texto))
    npontuacao = len(re.findall('[\.\!\,\?\-\:\—\"\(\)\[\]]',texto))
    nespaco = len(re.findall(' ',texto))

tup = (nlinhas,nvogais,nconsoante,ndigito,npontuacao,nespaco)
print(tup)




