import numpy as np
def soma(m1=0, m2=0):
    print(type(m2))
    if isinstance(m1, int):
        m1 = np.random.rand(1,1)
        return m1+m2
    elif isinstance(m2, int):
        m2 = np.random.rand(1,1)
        return m1+m2
        
    if(m1.shape == m2.shape):
        return m1 + m2
    else:
        raise ValueError("Tamanhos inconsistentes")
        
        
