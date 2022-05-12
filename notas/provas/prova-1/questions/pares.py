"""
Crie um programa que leia uma lista de strings separadas por vírgulas e
mostre uma lista de pares. Caso a lista possua um número ímpar de 
elementos, inclua a string vazia como segundo elemento do par final

* while: 1
* lst: 1
"""

strings = input("lst: ").split(",")
n = len(strings)
# n = len(pares)
pares = []

for i in range(0, n, 2):
    x = strings[i]
    if i == n - 1:
        y = ""
    else:
        y = strings[i + 1]
    pares.append([x, y])

for x, y in pares:
    print(x, y)
