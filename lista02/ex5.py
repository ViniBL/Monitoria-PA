n1 = float(input())
n2 = float(input())
n3 = float(input())

ma = (n1+n2+n3)/3

maior = ma
menor = ma

mh = 3/((1/n1)+(1/n2)+(1/n3))
if(mh>maior):
    maior = mh
if(mh<menor):
    menor = mh
    
mg = (n1*n2*n3)**(1/3)

if(mg>maior):
    maior = mg
if(mg<menor):
    menor = mg
    
mq = ((n1**2+n2**2+n3**2)/3)**(1/2)

if(mq>maior):
    maior = mq
if(mq<menor):
    menor = mq
    
print(f"Menor: {menor}")
print(f"Maior: {maior}")
