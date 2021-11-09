import pandas as pd
from Crypto.Hash import SHA256
def salva(dados):
    df = pd.DataFrame.from_dict(dados)
    
    df.to_csv('dados.csv')
    df.to_json('dados.json')
    df.to_html('dados.html')
    df.to_latex('dados.tex')
    
    h = SHA256.new()
    with open('dados.csv','rb') as f:
        h.update(f.read())
        csv = h.hexdigest()
        
    h = SHA256.new()
    with open('dados.json','rb') as f:
        h.update(f.read())
        json = h.hexdigest()
        
    h = SHA256.new()
    with open('dados.html','rb') as f:
        h.update(f.read())
        html = h.hexdigest()

    h = SHA256.new()
    with open('dados.tex','rb') as f:
        h.update(f.read())
        tex = h.hexdigest()

    return (csv,json,html,tex)

