from turtle import *


def quadrado(x, cor_linha="", cor_fundo=""):
    """
    Declara um quadrado
    """

    if cor_linha != "":
        pencolor(cor_linha)
    if cor_fundo != "":
        fillcolor(cor_fundo)
        begin_fill()

    forward(x)
    left(90)
    forward(x)
    left(90)
    forward(x)
    left(90)
    forward(x)
    left(90)

    if cor_fundo != "":
        end_fill()


quadrado(400)
quadrado(350, cor_fundo="red3")
quadrado(300, cor_fundo="orange")
quadrado(250, cor_fundo="yellow")
quadrado(200, cor_fundo="seagreen4")
quadrado(150, cor_fundo="orchid4")
quadrado(100, cor_fundo="royalblue1")
quadrado(50, cor_fundo="dodgerblue4")
left(45)
quadrado(200)

done()
