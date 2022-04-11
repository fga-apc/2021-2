"""
1 + 1/2 + 1/4 + 1/8 + ... = S
2 + 1   + 1/2 + 1/4 + ... = 2 * S
2 + (1 + 1/2 + 1/4 + ...) = 2 * S
2 + S = 2 * S
S = 2
"""

n = int(input("n: "))
soma = 0.0
x = 1.0

for i in range(n):
    soma += x
    x = x / 2.0

    print(f"{i}) soma = {soma}")
    if soma == 2:
        break
