from turtle import *

alice = Turtle()
bob = Turtle()
lado = 150

# Desloca sem desenhar no papel
bob.right(90)
bob.penup()
bob.forward(lado / 2)
bob.pendown()

# Desenha um quadrado com alice
alice.color('#87ceeb', '#c9e9f6')
bob.color('#ff6f69', '#ffeead')

alice.begin_fill()
bob.begin_fill()

alice.forward(lado)
bob.forward(lado)

alice.left(90)
bob.left(90)

alice.forward(lado)
bob.forward(lado)

alice.left(90)
bob.left(90)

alice.forward(lado)
bob.forward(lado)

alice.left(90)
bob.left(90)

alice.forward(lado)
bob.forward(lado)

alice.end_fill()
bob.end_fill()

done()
