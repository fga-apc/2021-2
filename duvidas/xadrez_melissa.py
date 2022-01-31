from turtle import *


speed(200)


def quadrado(lado):
    for i in range(4):
        forward(lado)
        left(90)
    forward(lado)


def tabuleiro(lado):
    for x in range(8):
        penup()
        goto(-4 * lado, (x - 4) * lado)
        pendown()
        for y in range(8):
            if (x + y) % 2 == 0:
                fillcolor("red")
            else:
                fillcolor("black")

            begin_fill()
            quadrado(lado)
            end_fill()

lado = 50
tabuleiro(lado)
done()
