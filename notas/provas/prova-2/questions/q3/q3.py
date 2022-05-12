# Pergunte o valor de "n" para o usuário e salve-o como uma variável inteira.
n = int(input("n: "))

# Calcule a sequência de Collatz para esse número
seq = [n]
while n > 1:
    if n % 2 == 1:
        n = n * 3 + 1
    else:
        n = n // 2
    seq.append(n)
    print(n)
print("seq =", seq)

# Calcule quantos termos possui a sequência obtida
n_termos = len(seq)
print("n termos =", n_termos)

# Diga qual é o maior valor atingido nesta sequência.
maior = max(seq)
print("maior valor =", maior)
