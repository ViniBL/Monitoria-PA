total = float(input())
valor = float(input())
troco = valor-total

print(f"Troco: R$ {troco}")

c100 = troco/100
troco = troco%100
c100 = int(c100)

c50 = troco/50
troco = troco%50
c50 = int(c50)

c20 = troco/20
troco = troco%20
c20 = int(c20)

c10 = troco/10
troco = troco%10
c10 = int(c10)

c5 = troco/5
troco = troco%5
c5 = int(c5)

c2 = troco/2
troco = troco%2
c2 = int(c2)

c1 = troco/1
troco = troco%1
c1 = int(c1)

m50 = troco/0.50
troco = troco%0.50
m50 = int(m50)

m25 = troco/0.25
troco = troco%0.25
m25 = int(m25)

m10 = troco/0.10
troco = troco%0.10
m10 = int(m10)

m5 = troco/0.05
troco = troco%0.05
m5 = int(m5)

m1 = troco/0.01
troco = troco%0.01
m1 = int(m1)

print(f"{c100} de R$ 100.00")
print(f"{c50} de R$ 50.00")
print(f"{c20} de R$ 20.00")
print(f"{c10} de R$ 10.00")
print(f"{c5} de R$ 5.00")
print(f"{c2} de R$ 2.00")
print(f"{c1} de R$ 1.00")
print(f"{m50} de R$ 0.50")
print(f"{m25} de R$ 0.25")
print(f"{m10} de R$ 0.10")
print(f"{m5} de R$ 0.05")
print(f"{m1} de R$ 0.01")


