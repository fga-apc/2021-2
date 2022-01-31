from turtle import *

# Desenha dois quadrados.
def quadrado(lado):
    for i in range(8):
        forward(lado / 2)
        if i % 2 == 0:
            right(90)

lado = 200
quadrado(lado)
right(90)
quadrado(lado)

done()
