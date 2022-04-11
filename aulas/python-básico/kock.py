import pyxel
from math import cos, sin, sqrt, pi

RES = 1024
PONTOS = []
COLOR = pyxel.COLOR_YELLOW
N = 0


def init():
    pyxel.init(RES, RES)
    pyxel.mouse(True)


def update():
    global N
    if pyxel.btnp(pyxel.KEY_UP):
        N += 1
    if pyxel.btnp(pyxel.KEY_DOWN):
        N = max(N - 1, 0)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        pt = pyxel.mouse_x, pyxel.mouse_y
        PONTOS.append(pt)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT) and PONTOS:
        PONTOS.pop()


def draw():
    pyxel.cls(pyxel.COLOR_BLACK)
    if PONTOS:
        p1 = PONTOS[0]
        for p2 in PONTOS[1:]:
            x1, y1 = p1
            x2, y2 = p2
            koch(x1, y1, x2, y2, COLOR, N)
            p1 = p2
    for pt in PONTOS:
        x, y = pt
        pyxel.circ(x, y, 1, pyxel.COLOR_RED)

    pyxel.text(0, 0, f"{N=}", pyxel.COLOR_WHITE)


def koch(x1, y1, x2, y2, col, n):
    if n == 0:
        pyxel.line(x1, y1, x2, y2, col)
    else:
        dx = x2 - x1
        dy = y2 - y1
        x_T = cos(pi / 3) * dx - sin(pi / 3) * dy
        y_T = sin(pi / 3) * dx + cos(pi / 3) * dy

        xa = (2 * x1 + x2) / 3
        ya = (2 * y1 + y2) / 3
        xb = xa + x_T / 3
        yb = ya + y_T / 3
        xc = (x1 + 2 * x2) / 3
        yc = (y1 + 2 * y2) / 3
        koch(x1, y1, xa, ya, col, n - 1)
        koch(xa, ya, xb, yb, col, n - 1)
        koch(xb, yb, xc, yc, col, n - 1)
        koch(xc, yc, x2, y2, col, n - 1)


init()
pyxel.run(update, draw)
