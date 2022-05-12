#include <stdio.h>

int NOTE_VALUES[6] = {100, 50, 20, 10, 5, 2};
int COIN_VALUES[6] = {100, 50, 25, 10, 5, 1};

int money_distrib(int cents, int *values, int *distrib)
{
    for (int i = 0; i < 6; i++)
    {
        int n = cents / values[i];
        cents -= n * values[i];
        distrib[i] = n;
    }
    return cents;
}

void print_money_distrib(int *distrib, char *name, int *values, float scale)
{
    for (int i = 0; i < 6; i++)
        printf("%d %s de R$ %.2f\n", distrib[i], name, scale * values[i]);
}

void main()
{
    int notes, cents;
    int distrib[6];

    scanf("%d.%d", &notes, &cents);

    printf("NOTAS:\n");
    notes = money_distrib(notes, NOTE_VALUES, distrib);
    print_money_distrib(distrib, "nota(s)", NOTE_VALUES, 1.0);

    printf("MOEDAS:\n");
    money_distrib(cents + 100 * notes, COIN_VALUES, distrib);
    print_money_distrib(distrib, "moeda(s)", COIN_VALUES, 0.01);
}
