import scipy.integrate as integrate
def integral(funcao, ini = 0, fim=1):
    return integrate.quad(funcao,ini,fim)[0]

