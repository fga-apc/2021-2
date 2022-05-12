# Python já possui uma função igual a essa, min(x, y),
# mas segue a implementação de referência, já que teremos
# que repetir esta implementação em C.
def menor(x, y):
    if x < y:
        return x
    else:
        return y


# A solução do desafio de Feynman é particularmente elegante.
# No loop abaixo, considere que i, j é a coordenada da célula
# no canto inferior esquerdo da matriz.
#
# O valor m = min(i + 1, j + 1) consiste no maior quadrado que pode
# ser feito utilizando esta célula na posição inferior esquerda.
# Também é possível contar os quadrados de lado m - 1, m - 2, ... até 1.
def feynman(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += menor(i + 1, j + 1)
    return total


# O idioma if __name__ == "__main__" do Python acaba virando a
# função main() do C!
if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        print(feynman(n))
