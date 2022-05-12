#include <stdio.h>

void main()
{
    int N = 20;
    int vetor[20];

    // Lê coordenadas do vetor
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &vetor[i]);
    }

    // Inverte os valores do vetor
    for (int i = 0; i < N / 2; i++)
    {
        int aux,
            j = N - i - 1;
        aux = vetor[i];
        vetor[i] = vetor[j];
        vetor[j] = aux; // antigo vetor[i]
    }

    // Imprime o vetor
    for (int i = 0; i < N; i++)
    {
        printf("N[%d] = %d\n", i, vetor[i]);
    }
}