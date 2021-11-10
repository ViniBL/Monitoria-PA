import numpy as np
def soma(m1=0, m2=0):
    
    if type(m1) == 'int':
        m1 = np.random.rand(m2.shape[1:-1])
        print("alo")
    if type(m1) == 'int':
        m2 = np.random.rand(m1.shape[1:-1])
        print("alo")
        
    if(m1.shape == m2.shape):
        return m1 + m2
    else:
        raise ValueError("Tamanhos inconsistentes")
        

        
