def tri(n):
    """
    Calcula o n-ésimo número triangular.
    """
    if n == 0:
        return 0
    else:
        return n + tri(n - 1)


def fat(n):
    """
    Calcula o fatorial de n.
    """
    if n == 0:
        return 1
    else:
        return n * fat(n - 1)


def ifat(n):
    """
    Calcula o fatorial de n.
    """
    total = 1
    for x in range(1, n + 1):
        total *= x
    return total


def rfib(n):
    """
    Retorna o n-ésimo número de Fibonacci
    """
    if n <= 1:
        return 1
    return rfib(n - 1) + rfib(n - 2)


def ifib(n):
    """
    Retorna o n-ésimo número de Fibonacci
    """
    x, y = 1, 1
    for _ in range(n):
        x, y = y, x + y
    return x


if __name__ == "__main__":
    n = int(input("n: "))
    print(f"ifib({n}) = {ifib(n)}")
    print(f"rfib({n}) = {rfib(n)}")

    # print(f"ifat({n}) = {ifat(n)}")
    # print(f"rfat({n}) = {fat(n)}")
    # print(f"tri({n}) = {tri(n)}")
