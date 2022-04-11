x = 1
y = 1
n = 20
fibs = []

for _ in range(n):
    fibs.append(x)
    x, y = y, x + y

print(fibs)
