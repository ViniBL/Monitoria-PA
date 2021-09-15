l=list()
while True:
    n=input()
    if n=="s":
        break
    else:
        n=int(n)
        if n in l:
            l.remove(n)
        else:
            l.append(n)
if(len(l) == 0):
    print(0)
else:
    print(l[0])

