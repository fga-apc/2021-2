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


def mergesort(a: list) -> list:
    n = len(a)
    if n <= 1:
        return a
    else:
        u = mergesort(a[0 : n // 2])
        v = mergesort(a[n // 2 :])
        u.reverse()
        v.reverse()
        return _mesclar(u, v)


def _mesclar(a, b):
    c = []

    # Consome as listas tirando o menor elemento do início.
    while a and b:
        if a[-1] < b[-1]:
            c.append(a.pop())
        else:
            c.append(b.pop())
    c.extend(reversed(a))
    c.extend(reversed(b))
    return c


if __name__ == "__main__":
    from time import time

    lst = [40, 42, 10, 1, -10, 100, 1000] * 10000
    assert ordenar(lst) == mergesort(lst)

    t0 = time()

    for _ in range(10):
        mergesort(lst)
        mergesort(lst)
        mergesort(lst)
        mergesort(lst)
        mergesort(lst)

    t1 = time()
    dt = t1 - t0
    print(f"\ndt = {dt * 1000:.4}ms")
    # ~530ms
