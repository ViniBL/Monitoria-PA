import time
def atraso(T):
    t0 = time.time_ns()
    time.sleep(T)
    t1 = time.time_ns()
    temp = t1-t0
    return temp - T*10**9

print(atraso(1,))