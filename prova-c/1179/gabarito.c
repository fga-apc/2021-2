#include <stdio.h>

void print_nums(int *lst, int n, char *nome)
{
    for (int i = 0; i < n; i++)
    {
        printf("%s[%d] = %d\n", nome, i, lst[i]);
    }
}

void main()
{
    int par[5], impar[5], n_par = 0, n_impar = 0;

    for (int i = 0; i < 15; i++)
    {
        int n;
        scanf("%d", &n);

        if (n % 2 == 0)
        {
            par[n_par] = n;
            n_par++;
            if (n_par == 5)
            {
                print_nums(par, n_par, "par");
                n_par = 0;
            }
        }
        else
        {
            impar[n_impar] = n;
            n_impar++;
            if (n_impar == 5)
            {
                print_nums(impar, n_impar, "impar");
                n_impar = 0;
            }
        }
    }
    print_nums(par, n_par, "par");
    print_nums(impar, n_impar, "impar");
}
