import pyxel

PASSO = 1.5


def init():
    pyxel.x = 10  # posição do canto superior esquerdo
    pyxel.forward = True


def update():
    if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
        pyxel.x -= PASSO
        pyxel.forward = False

    if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
        pyxel.x += PASSO
        pyxel.forward = True


def draw():
    pyxel.cls(pyxel.COLOR_LIGHT_BLUE)
    draw_player()
    pyxel.rect(0, 60, 120, 20, pyxel.COLOR_BROWN)


def draw_player():
    x = pyxel.x
    y = 50  # (pyxel.height - 20 - 10)
    img = 0
    i = int(pyxel.x / 4) % 4
    u = 16 * i
    v = 0
    w = 10
    h = 10
    if not pyxel.forward:
        w = -w
    pyxel.blt(x, y, img, u, v, w, h, colkey=pyxel.COLOR_GRAY)


pyxel.init(120, 80)
pyxel.load("arte.pyxres")
init()
pyxel.mouse(True)
pyxel.run(update, draw)
