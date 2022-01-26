from turtle import *

bgcolor("blue")
color("yellow")

estrelas_centros = [
    (-50, -100),
    (0, 120),
    (200, 300),
    (-150, 200),
    (300, 50),
    (-250, -300),
]
angulo = 60


def estrela(x, y, tamanho):
    """
    Desenha uma estrela de Davi com o centro em x e y
    com o tamanho entre duas pontas dado.
    """
    global angulo
    
    penup()
    goto(x, y)

    lado = tamanho / 3
    forward(lado)
    left(2 * angulo)
    pendown()

    for i in range(6):
        forward(lado)
        left(angulo)

    for i in range(6):
        right(angulo)
        forward(lado)
        left(2 * angulo)
        forward(lado)
    
    angulo = 0.75 * angulo


speed(100)
for x, y in estrelas_centros:
    estrela(x, y, 20)

done()
