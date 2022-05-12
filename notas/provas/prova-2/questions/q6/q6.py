orig = "abcdefghijklmnopqrstuvwxyz"
dest = "nvxkrgpszdeailyuhfbocqjmwt"
code = dict(zip(orig, dest))

msg = input()
print("".join(code.get(c, c) for c in msg))
