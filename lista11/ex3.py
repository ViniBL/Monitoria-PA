import time
def atraso(T):
    t0 = time.time()
    time.sleep(T)
    t1 = time.time()
    temp = t1-t0
    return temp/1000