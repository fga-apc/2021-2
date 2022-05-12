"""
Crie um programa que leia uma lista de números inteiros e forneça o valor e posição do maior
elemento.

* for: 1
* if: 1
"""


def maxarg(lst):
    if not lst:
        return None
    max_value = lst[0]
    max_pos = 0
    for i, x in enumerate(lst):
        if x > max_value:
            max_value = x
            max_pos = i
    return (max_pos, max_value)


ns = [int(x) for x in input("ns: ").split(",")]
pos, valor = maxarg(ns)
print(f"maior valor = {valor}, posição = {pos + 1}o")
