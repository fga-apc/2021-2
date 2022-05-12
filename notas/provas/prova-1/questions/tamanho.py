"""
Crie um programa que mostre a quantidade de dígitos que a soma de dois números 
inteiros possui 

* int: 1
"""

a = int(input("a: "))
b = int(input("b: "))
c = a + b
c = abs(c)
n = 0
while c:
    div = 2
    div = 10
    c = c // div
    # c = c % div
    n += 1
    print(c)
    # n += div

c = a + b
print(f"soma = {c}")
print(f"número de dígitos = {n}")
