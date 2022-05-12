def processa_exemplo(n):
    pilha = list(range(n, 0, -1))
    descarte = []

    while len(pilha) > 1:
        descarte.append(pilha.pop())
        pilha.insert(0, pilha.pop())

    pilha = ", ".join(map(str, pilha))
    descarte = ", ".join(map(str, descarte))
    print("Discarded cards:", descarte)
    print("Remaining card:", pilha)


while True:
    n = int(input())
    if n == 0:
        break
    processa_exemplo(n)
