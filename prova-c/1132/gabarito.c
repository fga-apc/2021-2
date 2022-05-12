#include <stdio.h>

// Múltiplos de 13
void main()
{
    int a, b, total = 0;
    scanf("%d %d", &a, &b);
    int step = b > a ? 1 : -1;

    for (int i = a; i != b; i += step)
    {
        if (i % 13)
            total += i;
    }
    printf("%d\n", total);
}
