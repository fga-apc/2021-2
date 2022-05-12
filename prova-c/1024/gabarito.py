def crypto(msg):
    split = len(msg) // 2

    msg = "".join(chr(ord(c) + 3) if c.isalpha() else c for c in msg)
    msg = msg[::-1]
    msg = msg[:split] + "".join(chr(ord(c) - 1) for c in msg[split:])
    return msg


n = int(input())
for i in range(n):
    msg = input()
    print(crypto(msg))
