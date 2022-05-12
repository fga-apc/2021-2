x = float(input("x: "))
n = 0
resultado = 0.0
termo = 1.0

while n < 5:
    n = n + 1
    termo = termo * x
    resultado = resultado + termo / n

print(resultado)
