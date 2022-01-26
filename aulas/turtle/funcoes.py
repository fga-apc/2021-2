def raiz(x):
    """
    Calcula a raiz quadrada, mantendo o sinal.
    """
    if x >= 0:
        return x ** 0.5
    else:
        return -((-x) ** 0.5)


def diagonal(x, y):
    """
    Calcula a diagonal de um triângulo de lados x e y
    """
    return raiz(x ** 2 + y ** 2)


print(diagonal(3, 4))
