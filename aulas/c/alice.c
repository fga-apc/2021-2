#include <stdio.h>

void print_pilha(int *pilha, int size)
{
    for (int i = 0; i < size; i++)
    {
        if (i != 0)
            printf(", ");
        printf("%d", pilha[i]);
    }
    printf("\n");
}

void processa_exemplo(int n)
{
    // pilha = list(range(n, 0, -1))
    // descarte = []
    int pilha[n], descarte[n];
    int pilha_size = n, descarte_size = 0;
    for (int i = 0; i < n; i++)
        pilha[i] = n - i;

    while (pilha_size > 1)
    {
        // x = pilha.pop()
        int x = pilha[pilha_size - 1];
        pilha_size--;

        // descarte.append(x)
        descarte[descarte_size] = x;
        descarte_size++;

        // pilha.insert(0, pilha.pop());
        int last = pilha[pilha_size - 1];
        for (int i = pilha_size - 2; i >= 0; i--)
        {
            pilha[i + 1] = pilha[i];
        }
        pilha[0] = last;
    }

    // pilha = ", ".join(map(str, pilha))
    // descarte = ", ".join(map(str, descarte))

    // print("Discarded cards:", descarte);
    printf("Discarded cards: ");
    print_pilha(descarte, descarte_size);

    // print("Remaining card:", pilha);
    printf("Remaining card: ");
    print_pilha(pilha, pilha_size);
}

void main()
{
    while (1)
    {
        int n;
        scanf("%d", &n);
        if (n == 0)
        {
            break;
        }
        processa_exemplo(n);
    }
}