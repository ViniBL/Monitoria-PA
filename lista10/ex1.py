import numpy as np
def soma(m1=np.random.rand(3,2), m2=np.random.rand(3,2)):
    try:
        return np.add(m1,m2)
    except ValueError:
        print("Tamanhos inconsistentes")
        
