import pyxel
from math import cos, sin, sqrt, pi

X0 = 100
Y0 = 100
ANGULO_VAR = 0.1


def init():
    pyxel.init(200, 200)
    pyxel.mouse(True)
    pyxel.razao = 0.5
    pyxel.n = 10
    pyxel.m = 0
    pyxel.wireframe = False
    pyxel.func = desenhar_folha
    pyxel.mono = False
    pyxel.linhas = []


def update():
    pyxel.wireframe = pyxel.btn(pyxel.KEY_SPACE)
    pyxel.mono = pyxel.btn(pyxel.KEY_R)

    if pyxel.btn(pyxel.KEY_UP):
        pyxel.razao -= ANGULO_VAR / (pyxel.n ** 2 + 10)
    if pyxel.btn(pyxel.KEY_DOWN):
        pyxel.razao += ANGULO_VAR / (pyxel.n ** 2 + 10)
    if pyxel.btn(pyxel.KEY_RIGHT):
        pyxel.n += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        pyxel.n = max(pyxel.n - 1, 1)

    if pyxel.btn(pyxel.KEY_G):
        pyxel.razao = 1 / ((1 + sqrt(5)) / 2)

    if pyxel.btn(pyxel.KEY_S):
        pyxel.func = desenhar_semente
    else:
        pyxel.func = desenhar_folha

    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.linhas.append([])
    if pyxel.linhas and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.linhas[-1].append([pyxel.mouse_x, pyxel.mouse_y])
    if pyxel.btnr(pyxel.MOUSE_BUTTON_RIGHT):
        pyxel.linhas.pop()

    for i in range(10):
        if pyxel.btnp(pyxel.KEY_0 + i):
            if pyxel.m == 0:
                pyxel.m = i
            else:
                pyxel.razao = i / pyxel.m
                pyxel.m = 0


def draw():
    pyxel.cls(pyxel.COLOR_BLACK)

    angulo = 0
    tamanho = 80
    for i in range(pyxel.n):
        r = (pyxel.n ** 2 - i ** 2) / pyxel.n ** 2
        pyxel.func(tamanho * r, angulo, 7 + i % 8)
        angulo -= 2 * pi * pyxel.razao

    n_escuros = 0
    n_claros = 0
    for x in range(X0 - tamanho, X0 + tamanho + 1):
        for y in range(X0 - tamanho, X0 + tamanho + 1):
            if pyxel.pget(x, y) == pyxel.COLOR_BLACK:
                n_escuros += 1
            else:
                n_claros += 1

    prop = 100 * n_claros / (n_escuros + n_claros)
    pyxel.text(0, 0, f"f = {1 / pyxel.razao}", pyxel.COLOR_WHITE)
    pyxel.text(0, 10, f"n = {pyxel.n}", pyxel.COLOR_WHITE)
    pyxel.text(0, 20, f"p = {prop}", pyxel.COLOR_WHITE)

    for linha in pyxel.linhas:
        x0, y0 = linha[0]
        for x1, y1 in linha[1:]:
            pyxel.line(x0, y0, x1, y1, 2)
            x0, y0 = x1, y1


def desenhar_folha(tam, angulo, cor):
    r = 2.5
    x1 = X0 + tam * cos(angulo)
    y1 = Y0 + tam * sin(angulo)
    x2 = X0 + tam * cos(angulo + pi / 10) / r
    y2 = Y0 + tam * sin(angulo + pi / 10) / r
    x3 = X0 + tam * cos(angulo - pi / 10) / r
    y3 = Y0 + tam * sin(angulo - pi / 10) / r

    if pyxel.mono:
        cor = pyxel.COLOR_RED

    if pyxel.wireframe:
        pyxel.line(X0, Y0, x2, y2, cor)
        pyxel.line(x2, y2, x1, y1, cor)
        pyxel.line(x1, y1, x3, y3, cor)
        pyxel.line(x3, y3, X0, Y0, cor)
    else:
        pyxel.tri(X0, Y0, x1, y1, x2, y2, cor)
        pyxel.tri(X0, Y0, x1, y1, x3, y3, cor)


def desenhar_semente(tam, angulo, cor):
    r = 2.5
    x = X0 + tam * cos(angulo)
    y = Y0 + tam * sin(angulo)

    if pyxel.mono:
        cor = pyxel.COLOR_RED

    if pyxel.wireframe:
        pyxel.circb(x, y, r, cor)
    else:
        pyxel.circ(x, y, r, cor)


def run():
    init()
    pyxel.run(update, draw)


if __name__ == "__main__":
    run()
