from turtle import *


def figura(n, lado):
    """
    Declara um quadrado
    """
    angulo = 360 / n 
    _andar_e_girar(lado, angulo, n)

def _andar_e_girar(lado, angulo, n=1):
    if n == 1:
        forward(lado)
        left(angulo)
    elif n > 1:
        forward(lado)
        left(angulo)
        _andar_e_girar(lado, angulo, n - 1)


figura(3, 100)
figura(4, 100)
figura(5, 100)
figura(6, 100)
done()
