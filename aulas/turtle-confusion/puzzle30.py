from turtle import *

# Desenha uma padronagem com losângos
def figura(lado):
    for _ in range(6):
        losango(lado)
        left(60)

    forward(lado)
    left(60)
    forward(lado)
    left(60)
    hexagono(2 * lado)


def losango(lado):
    for _ in range(2):
        forward(lado)
        left(60)
        forward(lado)
        left(120)


def hexagono(lado):
    for _ in range(6):
        forward(lado / 2)
        left(60)
        forward(lado / 2)


right(30)
speed(0)
figura(150)

done()
