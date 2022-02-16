from math import sqrt


lst = []

print("Digite as medições realizadas")
while True:
    n = input("n: ")
    if n == "":
        break
    lst.append(float(n))

print()

# Calcula a média das medições
media = sum(lst) / len(lst)
print("média:", media)

# Calcula o desvio padrão das medições
total = 0.0
for x in lst:
    total += (x - media) ** 2

print("desvpad:", sqrt(total / (len(lst) - 1)))
