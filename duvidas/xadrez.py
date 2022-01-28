from turtle import *

# Configura propriedades do tabuleiro
speed(0)
lado = 50
X = lado * 4
Y = lado * 4

# Desenha borda do tabuleiro
penup()
goto(-4.5 * lado, -4.5 * lado)
pendown()
fillcolor("brown")
begin_fill()
for _ in range(4):
    forward(9 * lado)
    left(90)
end_fill()

# Prepara área com casas brancas
penup()
goto(-4 * lado, -4 * lado)
pendown()
fillcolor("white")
begin_fill()
for _ in range(4):
    forward(8 * lado)
    left(90)
end_fill()

# Desenha casas pretas
fillcolor("black")
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            penup()
            goto(lado * i - X, lado * j - Y)
            pendown()
            
            begin_fill()
            for _ in range(4):
                forward(lado)
                left(90)
            end_fill()
done()