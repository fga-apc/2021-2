#include <stdio.h>
#include <string.h>

void crypto(char *msg)
{
    int i = 0;
    int n = strlen(msg);

    // Cifra de cesar
    for (i = 0; i < n; i++)
    {
        char c = msg[i];
        if (c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z')
            msg[i] = c + 3;
    }

    // Inverte a linha
    for (int i = 0; i < n / 2; i++)
    {
        char aux = msg[i];
        msg[i] = msg[n - i - 1];
        msg[n - i - 1] = aux;
    }

    // Muda metade da linha
    for (int i = n / 2; i < n; i++)
    {
        msg[i]--;
    }
}

void main()
{
    int n;
    scanf("%d ", &n);
    for (int i = 0; i < n; i++)
    {
        char msg[1001];
        gets(msg);
        crypto(msg);
        printf("%s\n", msg);
    }
}
