from re import findall

nome_arquivo = input()

with open(nome_arquivo) as f:
    texto = f.read()
    nlinhas = len(findall('(\n)',texto))
    nvogais = len(findall('[aeiouAEIOU]',texto))
    nconsoante = len(findall('[b-df-hj-np-tv-xz]',texto))
    ndigito = len(findall('\d',texto))
    npontuacao = len(findall('[\.\!\,\?\-\:\—\"\(\)\[\]]',texto))
    nespaco = len(findall(' ',texto))
#     lista = f.readlines()
# 
# f.close()
# 
# lista = [linha.rstrip('\n') for linha in lista]

tup = (nlinhas,nvogais,nconsoante,ndigito,npontuacao,nespaco)
print(tup)




