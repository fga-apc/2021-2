# https://www.youtube.com/watch?v=i7sm9dzFtEI
def ack(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, n + 1)
    else:
        return ack(m - 1, ack(m, n - 1))


for m in range(6):
    for n in range(6):
        print(f"{m=}, {n=}")
        print(f"   ack={ack(m, n)}")
