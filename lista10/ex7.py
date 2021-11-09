import numpy as np
def sistema_linear(A, B):
    npa = np.array(A)
    npb = np.array(B)
    x = np.linalg.solve(npa,npb)
    list1 = x.tolist()
    return list1