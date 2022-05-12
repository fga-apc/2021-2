"""
Crie um programa que mostre uma lista com todos os primos de 1 até n, onde
n é um valor fornecido pelo usuário.

O exercício possui algumas dicas de implementação na forma de comentários.

* for: 2
"""

n = int(input("n: "))
primos = [2, 3]
nums = range(2, n + 1)
# nums = range(2, n)
# nums = range(n)

for x in nums:
    # Assumimos que o número é primo e tentamos encontrar o divisor.
    é_primo = True
    for p in primos:
        # Um número não pode ser primo se for divisível por outro primo.
        if x % p == 0:
            é_primo = False
    # Acrescentamos os novos primos à lista de primos.
    if é_primo:
        primos.append(x)

print(primos)
