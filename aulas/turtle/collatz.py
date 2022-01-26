from turtle import *
import turtle

n = 61
i = 0
title(f"Sequência de collatz para o número {n}")

while n != 1:
    goto(i * 10, n * 3)
    
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    
    i = i + 1

goto(i * 10, n * 3)

done()