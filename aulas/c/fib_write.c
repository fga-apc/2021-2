#include <stdio.h>
/*
fib_write.c

 Crie um programa que pergunta um número n
 e grave os n primeiros fibonacci no arquivo numeros.txt
*/

void main()
{
    FILE *out = fopen("numeros.txt", "w");
    int n;
    long x = 1, y = 1;
    printf("n: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        fprintf(out, "%ld\n", x);
        int x_old = x;
        x = y;
        y = x_old + y;
    }

    fclose(out);
}