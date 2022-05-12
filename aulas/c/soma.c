#include <stdio.h>
/*
soma.c

Crie um programa que abre o arquivo numeros.txt,
com uma lista de números e calcule a soma destes números
*/

void main()
{
    FILE *nums = fopen("numeros.txt", "r");
    long soma = 0, x;
    while (fscanf(nums, " %ld", &x) == 1)
    {
        soma += x;
    }
    printf("soma = %ld\n", soma);
    fclose(nums);
}