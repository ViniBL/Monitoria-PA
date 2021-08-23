a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4*a*c

if(a == 0):
    x1 = -c/b
    print(f"A raiz é {x1}")
else:
    if(d > 0):
        x1 = (-b + d**(1/2))/(2*a)
        x2 = (-b - d**(1/2))/(2*a)
        if(x1>x2):
            temp = x2
            x2 = x1
            x1 = temp
        print(f"As raízes são {x1} e {x2}")
        
    if(d==0):
        x1 = (-b + d**(1/2))/(2*a)
        print(f"A raiz é {x1}")

    if(d<0):
        print("Nenhuma raiz")


