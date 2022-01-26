from turtle import *

cor1 = input("Cor 1: ")
cor2 = input("Cor 2: ")
cor3 = input("Cor 3: ")
n_de_bolas = int(input("Número de bolas: "))
n_de_pelatas = int(input("Número de pétalas: "))

# cor1 = "red"
# cor2 = "yellow"
# cor3 = "blue"
# n_de_bolas = 5
# n_de_pelatas = 6
pensize(6)

angulo = 360 / n_de_pelatas
lista_de_cores = [cor1, cor2, cor3]


def bolas(n, cores):
    raio_final = 30 + 10 * n
    i = 0
    for r in range(40, raio_final + 1, 10):
        cor = cores[i]
        color(cor)
        circle(r, 360)
        r = r + 10
        i = i + 1
        if i == 3:
            i = 0

speed(100)
for i in range(n_de_pelatas):
    bolas(n_de_bolas, lista_de_cores)
    penup()
    left(angulo)
    pendown()


done()
