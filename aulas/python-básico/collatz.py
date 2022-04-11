def ler_numero(msg, tipo=int):
    st = input(msg)
    try:
        return tipo(st)
    except ValueError:
        print("Digite um valor válido!")
        return ler_numero(msg)


def ler_numeros(msg):
    return ler_numero(msg, tipo=_str_num_lst)


def _str_num_lst(st):
    lst = []
    for n in st.split(","):
        lst.append(int(n.strip()))
    return lst


def collatz(n):
    seq = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq


ns = ler_numeros("ns: ")
for n in ns:
    seq = str(collatz(n))[1:-1]
    print(f"{n}: {seq}")
