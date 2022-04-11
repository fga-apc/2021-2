import pyxel

RES = 1024
X1, Y1 = RES / 2, 0
X2, Y2 = 0, RES
X3, Y3 = RES, RES
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


def draw():
    pyxel.cls(pyxel.COLOR_BLACK)
    sierpinski(X1, Y1, X2, Y2, X3, Y3, COLOR, N)
    pyxel.text(0, 0, f"{N=}", pyxel.COLOR_WHITE)


def sierpinski(x1, y1, x2, y2, x3, y3, col, n):
    if n == 0:
        pyxel.tri(x1, y1, x2, y2, x3, y3, col)
    else:
        x12 = (x1 + x2) / 2
        y12 = (y1 + y2) / 2
        x23 = (x2 + x3) / 2
        y23 = (y2 + y3) / 2
        x31 = (x3 + x1) / 2
        y31 = (y3 + y1) / 2
        sierpinski(x1, y1, x12, y12, x31, y31, col, n - 1)
        sierpinski(x2, y2, x23, y23, x12, y12, col, n - 1)
        sierpinski(x3, y3, x31, y31, x23, y23, col, n - 1)


init()
pyxel.run(update, draw)
