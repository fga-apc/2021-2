from turtle import *

def cruz(lado):
    for _ in range(4):
        forward(lado)
        left(-90)
        forward(lado)
        right(-90)
        forward(lado)
        left(-90)

speed(9)
for _ in range(8):
    cruz(50)
    left(45)

done()