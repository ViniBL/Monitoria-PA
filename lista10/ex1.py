import numpy as np
def soma(m1=0, m2=0):
    
    if type(m1) == 'int':
        m1 = np.random.rand(m2.shape[1:-1])
    if type(m1) == 'int':
        m2 = np.random.rand(m1.shape[1:-1])
        
    try:
        return np.add(m1,m2)
    except ValueError:
        print("Tamanhos inconsistentes")
        
