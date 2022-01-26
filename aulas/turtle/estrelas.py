from turtle import *

peacecolors = (
    "red3",
    "orange",
    "yellow",
    "orchid4",
    "royalblue1",
    "dodgerblue4",
)


def estrela(n, m, lado):
    """
    Declara uma estrela generalizada.
    """
    angulo = m * 360 / n
    
    for _ in range(n):
        frente_arco_iris(lado)
        left(angulo)


def frente_arco_iris(lado):
    """
    Anda para frente desenhando um arco-íris.
    """
    n = len(peacecolors)
    cor_original = pencolor()
    
    for cor in peacecolors:
        pencolor(cor)
        forward(lado / n)
    
    pencolor(cor_original)


speed(10)
estrela(42, 19, 300)
done()
