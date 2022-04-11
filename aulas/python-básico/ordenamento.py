def ordenar(entrada: list) -> list:
    entrada = entrada.copy()
    saida = []

    # Consome a lista de entrada, passando os valores para a lista
    # de saída, do menor para o maior.
    while entrada:
        # Posição do menor valor da lista
        i = entrada.index(min(entrada))

        # Transfere menor valor para o fim da lista de saída
        saida.append(entrada.pop(i))

    return saida


def mergesort(a):
    n = len(a)
    if n <= 1:
        return a
    else:
        return _mesclar(mergesort(a[0 : n // 2]), mergesort(a[n // 2 :]))


def _mesclar(a, b):
    c = []

    # Consome as listas tirando o menor elemento do início.
    while a and b:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    return c + a + b
