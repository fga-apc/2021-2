"""
Crie um programa que peça um número e calcule o seu fatorial

* for: 1
"""

n = int(input("n: "))
fat = 0
fat = 1
# for i in range(n):
for x in range(1, n + 1):
    fat *= x
    # fat *= x + 1
print(f"fat({n}) = {fat}")
