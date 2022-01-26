fib = 1, 1, 2, 3, 5, 8, 13, 21, ...
print("Sequência de Fibonacci")

ultimo = 1
penultimo = 0
n = 1
while ultimo < 1_000_000:
    print(n, ultimo)
    ultimo, penultimo = ultimo + penultimo, ultimo
    n = n + 1