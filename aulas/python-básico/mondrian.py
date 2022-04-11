import pyxel
import random

COLORS = [0, 8, 9, 5, 10, 11]
MARGIN = 10
N = 0
S = 0


def init():
    pyxel.init(256, 256)
    pyxel.mouse(True)


def update():
    global S, N

    if pyxel.btnp(pyxel.KEY_UP):
        N += 1
    if pyxel.btnp(pyxel.KEY_DOWN):
        N = max(0, N - 1)
    if pyxel.btnp(pyxel.KEY_LEFT):
        S += 1
    if pyxel.btnp(pyxel.KEY_RIGHT):
        S -= 1


def draw():
    pyxel.cls(pyxel.COLOR_WHITE)

    m = MARGIN
    random.seed(S)
    mondrian(m, m, pyxel.width - m, pyxel.height - m, N)


def mondrian(x1, y1, x2, y2, N):
    w = x2 - x1
    h = y2 - y1

    if N == 0:
        if random.random() < 0.25:
            color = random.choice(COLORS)
            pyxel.rect(x1, y1, w, h, color)

        # Margens
        pyxel.rect(x1 - 1, y1, 2, h, pyxel.COLOR_BLACK)
        pyxel.rect(x2 - 1, y1, 2, h, pyxel.COLOR_BLACK)
        pyxel.rect(x1, y1 - 1, w, 2, pyxel.COLOR_BLACK)
        pyxel.rect(x1, y2 - 1, w, 2, pyxel.COLOR_BLACK)

    else:

        def f(x):
            return random.uniform(0, x)

        xm = x1 + int(f(w / 3) + f(w / 3) + f(w / 3))
        ym = y1 + int(f(h / 3) + f(h / 3) + f(h / 3))

        mondrian(x1, y1, xm, ym, N - 1)
        mondrian(x1, ym, xm, y2, N - 1)
        mondrian(xm, y1, x2, ym, N - 1)
        mondrian(xm, ym, x2, y2, N - 1)


init()
pyxel.run(update, draw)
