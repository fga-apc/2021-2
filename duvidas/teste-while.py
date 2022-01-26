# n = 10
# for i in range(n):
#     print(i + 1)

n = 42
i = 1
acc = 0
while i <= n:
    acc = acc + i
    print(i)
    i = i * 2

print("Soma", acc)