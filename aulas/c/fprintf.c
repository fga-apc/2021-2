#include <stdio.h>

void main()
{
    int n = 0;
    double p1_acc = 0, p2_acc = 0, media_acc = 0;
    double p1, p2;
    char nome[10], mat[10], cabecalho[100];

    FILE *entrada = fopen("entrada.txt", "r");
    FILE *saida = fopen("saida.txt", "w");

    // Ignora a primeira linha do cabeçalho
    fscanf(entrada, "%[^\n] ", cabecalho);

    // Lê cada linha do arquivo
    fprintf(saida, "Notas\n");
    while (1)
    {
        int n_args = fscanf(entrada, "%[^,\n],%[^,\n],%lf,%lf ", nome, mat, &p1, &p2);
        if (n_args != 4)
        {
            break;
        }
        double media = (p1 + p2) / 2.0;
        p1_acc += p1;
        p2_acc += p2;
        media_acc += media;
        n++;
        fprintf(saida, "%10s (mat. %4s): média = %.1lf\n", nome, mat, media);
    }
    fclose(entrada);

    fprintf(saida, "P1 %.2lf!\n", p1_acc / n);
    fprintf(saida, "P2 %.2lf!\n", p2_acc / n);
    fprintf(saida, "Media %.2lf!\n", media_acc / n);
    fclose(saida);
}