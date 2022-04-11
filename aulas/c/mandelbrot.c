#include <stdio.h>
#include <math.h>
#include <time.h>

/**
 * Aplica a iteração do conjunto de mandelbrot por n vezes.
 *
 * Retorna 0 se a iteração convergiu ou 1 se ela divergiu.
 */
int mandelbrot(double cx, double cy, int n)
{
    // Regra de Mandelbrot
    //      z(n + 1) = z(n) * z(n) + c
    //
    // Reescrevendo como pares de números reais
    //     z = (x, y) = x + iy
    //     z * z = (x + iy) * (x + iy)
    //           = xx + 2ixy + i²yy
    //           = xx - yy + 2ixy
    //           = (xx - yy, 2xy)
    //
    // Juntamos o par de coordenadas na equação
    //    (x', y') = (xx - yy + cx, 2xy + cy)
    //
    // Isto cria as seguintes regras de recorrência
    //     x' = xx - yy + cx
    //     y' = 2xy + cy
    double x = 0, y = 0;
    for (int i = 0; i < n; i++)
    {
        x = x * x - y * y + cx;
        y = 2 * x * y + cy;

        // Testa se a trajetória já divergiu
        double dist_sqr = x * x + y * y;
        if (dist_sqr >= 4)
        {
            return i + 1;
        }
    }
    return 0;
}

void main_ask_coordinate()
{
    double x, y;
    printf("x, y: ");
    scanf("%lf, %lf", &x, &y);

    int res = mandelbrot(x, y, 100);
    printf("Resultado: %d\n", res);
}

void main()
{
    /*
      Calcula os coeficientes
      x = m j + c
     -2 = m 0 + c  => c = -2
      1 = m N + c  => m = 3 / N

      y = m i + c
     -1.5 = m 0 + c      => c = -1.5
      1.5 = m N / 2 + c  => m = 6 / N
    */
    int N = 80;
    double mx = 3.0 / N,
           my = 6.0 / N,
           cx = -2.0,
           cy = -1.5;

    clock_t t0 = clock();
    char line[N + 2];
    line[N] = '\x00';
    line[N - 1] = '\n';

    for (int i = 0; i < N / 2; i++)
    {
        for (int j = 0; j < N; j++)
        {
            double x = mx * j + cx;
            double y = my * i + cy;
            int color = mandelbrot(x, y, 100);

            if (color == 0)
            {
                line[j] = '$';
            }
            else if (color > 10)
            {
                line[j] = '.';
            }
            else
            {
                line[j] = ' ';
            }
        }
        printf(line);
    }
    double dt = (double)(clock() - t0) / CLOCKS_PER_SEC;
    printf("tempo: %.2f ms\n", 1000 * dt);
}