from turtle import *

# Desenha uma estrela de cinco lados
lado = 150
n = 5
m = 2

for _ in range(n):
    forward(lado)
    right(m * 360 / n)

done()
