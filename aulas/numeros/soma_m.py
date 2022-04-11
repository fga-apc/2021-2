"""
1 + 1/m + 1/m**2 + 1/m**3 + ... = S
m + 1   + 1/m + 1/m**2 + ... = m * S
m + (1 + 1/m + 1/m**2 + ...) = m * S
m + S = m * S
S = m / (m - 1)
"""

n = int(input("n: "))
m = int(input("m: "))
tol = 1e-9
res = m / (m - 1)
soma = 0.0
x = 1.0

for i in range(n):
    soma += x
    x = x / m
    print(f"{i}) soma = {soma}")

    if abs(soma - res) < tol:
        break

    if abs(soma / res - 1) < tol:
        break
