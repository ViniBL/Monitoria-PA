from sympy import *
def processa(expressao, var, var0=0):
    x = diff(expressao,var)
    y = integrate(expressao, var)
    z = limit(expressao,var,var0)
    
    return x,y,z

    
