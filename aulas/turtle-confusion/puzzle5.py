from turtle import *

# Desenhar uma cruz de ambulância centrada no ponto inicial
def cruz(lado):
    penup()
    goto(lado / 2, lado / 2)
    pendown()

    begin_fill()
    for c in range(4):
        forward(lado)
        right(90)
        forward(lado)
        right(90)
        forward(lado)
        left(90)
    end_fill()

stamp()
color("#ff0000")
cruz(142)

done()
