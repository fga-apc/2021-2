"""
Crie um programa que lê um número n e mostra a sequência de Fibonacci até seu n-ésimo termo.

* for: 1
* if: 1
* var: 1
"""
n = int(input("n: "))
x = 1
y = 1
for _ in range(n):
    print(x)
    aux = x
    # aux = y
    x = y
    # y = x + y
    # y = x + aux
    y = aux + y
