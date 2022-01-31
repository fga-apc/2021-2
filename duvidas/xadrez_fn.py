from calendar import c
from this import d
from tkinter import E
from turtle import *
from random import choice

def cor_aleatoria():
    """
    Retorna uma cor aleatoria
    """
    a = choice("0123456789abcdef")
    b = choice("0123456789abcdef")
    c = choice("0123456789abcdef")
    d = choice("0123456789abcdef")
    e = choice("0123456789abcdef")
    f = choice("0123456789abcdef") 
    return "#" + a + b + c + d + e + f


def desenhar_quadrado(tamanho, x, y, cor="black"):
    """
    Desenha um quadrado de lado "tamanho" preenchido com uma
    determinada "cor" de fundo.

    As coordenadas x, y determinam a posição do canto inferior esquerdo.
    """
    penup()
    goto(x, y)
    pendown()

    fillcolor(cor)
    begin_fill()
    for _ in range(4):
        forward(tamanho)
        left(90)
    end_fill()


# Configura propriedades do tabuleiro
speed(10)
lado = 80
X = lado * 4
Y = lado * 4

# Desenha borda do tabuleiro
desenhar_quadrado(9 * lado, -4.5 * lado, -4.5 * lado, "brown")

# Prepara área com casas brancas
desenhar_quadrado(8 * lado, -4 * lado, -4 * lado, "white")

# Desenha casas pretas
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            desenhar_quadrado(
                tamanho=lado, x=lado * i - X, y=lado * j - Y, cor=cor_aleatoria()
            )
done()
