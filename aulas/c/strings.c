#include <stdio.h>

void cifra(int n, char *st, char *out)
{
    int i = 0;
    if (n < 0)
    {
        n += 26;
    }

    while (st[i] != 0)
    {
        char c = st[i];

        if (c >= 'a' && c <= 'z')
        {
            c = (c - 'a' + n) % 26 + 'a';
        }

        if (c >= 'A' && c <= 'Z')
        {
            c = (c - 'A' + n) % 26 + 'A';
        }

        out[i] = c;
        i++;
    }
    out[i] = 0;
}

void cifra_cesar(char *st, char *out)
{
    cifra(3, st, out);
}

void cifra_cesar_inv(char *st, char *out)
{
    cifra(-3, st, out);
}

void cifra_rot13(char *st, char *out)
{
    cifra(13, st, out);
}

int numero_besta(char *st)
{
    int acc = 0;
    for (int i = 0; st[i] != 0; i++)
    {
        /*
        a - 1
        b - 2
        c - 3
        ...
        j - 10
        k - 20
        ...
        s - 100
        t - 200
        u - 300
        ...
        z - 800
        */
        char c = st[i];
        if (c < 'a' || c > 'z')
        {
            continue;
        }
        else if (c <= 'j')
        {
            acc += c - 'a' + 1;
        }
        else if (c <= 's')
        {
            acc += (c - 'j' + 1) * 10;
        }
        else if (c <= 'z')
        {
            acc += (c - 's' + 1) * 100;
        }
    }
    return acc;
}

void main()
{
    char msg[100], cesar[100], icesar[100], rot13[100];

    scanf("%100[^\n]", msg);
    int n = numero_besta(msg);

    cifra_cesar(msg, cesar);
    cifra_cesar_inv(msg, icesar);
    cifra_rot13(msg, rot13);

    printf("cesar  : %s\n", cesar);
    printf("icesar : %s\n", icesar);
    printf("rot13  : %s\n", rot13);
    printf("besta  : %d\n", n);
}