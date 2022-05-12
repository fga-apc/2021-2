#include <stdio.h>

int menor(int x, int y)
{
    if (x < y)
        return x;
    else
        return y;
}

int feynman(int n)
{
    int total = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            total += menor(i + 1, j + 1);
        }
    }
    return total;
}

void main()
{
    while (1)
    {
        int n = 0;
        scanf("%d", &n);
        if (n == 0)
            break;
        printf("%d\n", feynman(n));
    }
}