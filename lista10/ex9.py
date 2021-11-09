from Crypto.Util.number import getPrime, isPrime
def ehprimo(n):
    a = isPrime(n)
    if a == 0:
        return False
    if a == 1:
        return True
    else:
        return a