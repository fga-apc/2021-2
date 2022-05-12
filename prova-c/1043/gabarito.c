#include <stdio.h>

double max(double a, double b)
{
    return (a > b) ? a : b;
}

void main()
{
    double a, b, c;
    scanf("%lf %lf %lf", &a, &b, &c);
    double perimetro = a + b + c,
           maior = max(a, max(b, c));

    if (perimetro <= 2 * maior)
        printf("Area = %.1lf\n", (a + b) * c / 2);
    else
        printf("Perimetro = %1f\n", perimetro);
}
