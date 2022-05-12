"""
Crie um programa que peça dois números para o usuário e mostre o qual é o maior deles.

* if: 0
"""

a = int(input("a: "))
b = int(input("b: "))
# if b > a:
if a > b:
    print(f"o maior número é o a = {a}")
# elif a > b:
elif b > a:
    print(f"o maior número é o b = {b}")
else:
    print(f"os números são iguais")
