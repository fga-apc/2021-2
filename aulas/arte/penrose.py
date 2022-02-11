import pyxel
from math import cos, sin, sqrt, radians, pi

phi = 0.5 * (1 + sqrt(5))
COLOR_ACUTE = pyxel.COLOR_GRAY
COLOR_OBTUSE = pyxel.COLOR_NAVY
tri = pyxel.tri
n = 4
x0 = 0
y0 = 0


def acute(x, y, size, angle, gen=0, flip=1, tri=tri):
    delta = flip * pi / 5
    if gen == 0:
        x1 = x + size * cos(angle)
        y1 = y + size * sin(angle)
        x2 = x + size * cos(angle - delta)
        y2 = y + size * sin(angle - delta)
        tri(x, y, x1, y1, x2, y2, COLOR_ACUTE)

    else:
        x_ = x + size * cos(angle - delta)
        y_ = y + size * sin(angle - delta)

        angle_ = angle + 3 * delta
        size /= phi
        acute(x_, y_, size, angle_, flip=+1, gen=gen - 1)
        acute(x_, y_, size, angle_, flip=-1, gen=gen - 1)

        size /= phi
        x_ = x + size * cos(angle - delta)
        y_ = y + size * sin(angle - delta)

        angle += 4 * delta
        obtuse(x_, y_, size, angle, flip=flip, gen=gen - 1)


def obtuse(x, y, size, angle, flip=1, gen=0):
    delta = flip * radians(108)
    if gen == 0:
        x1 = x + size * cos(angle)
        y1 = y + size * sin(angle)
        x2 = x + size * cos(angle - delta)
        y2 = y + size * sin(angle - delta)
        tri(x, y, x1, y1, x2, y2, COLOR_OBTUSE)
    else:
        x_ = x + size * cos(angle)
        y_ = y + size * sin(angle)
        acute(x_, y_, size, angle + flip * radians(180), flip=-flip, gen=gen - 1)

        angle -= flip * 2 * pi / 5
        x_ = x + size / phi * cos(angle)
        y_ = y + size / phi * sin(angle)
        obtuse(x_, y_, size / phi, angle - flip * radians(72), flip=flip, gen=gen - 1)


def acute(x, y, size, angle, gen=0, flip=1, tri=tri):
    delta = flip * pi / 5
    if gen == 0:
        x1 = x + size * cos(angle)
        y1 = y + size * sin(angle)
        x2 = x + size * cos(angle - delta)
        y2 = y + size * sin(angle - delta)
        tri(x, y, x1, y1, x2, y2, COLOR_ACUTE)

    else:
        obtuse(x, y, size / phi, angle, flip=flip, gen=gen - 1)

        x_ = x + size * cos(angle)
        y_ = y + size * sin(angle)

        angle_ = angle - 3 * delta
        acute(x_, y_, size / phi, angle_, flip=flip, gen=gen - 1)


def obtuse(x, y, size, angle, flip=1, gen=0):
    delta = flip * radians(36)
    if gen == 0:
        x1 = x + size * phi * cos(angle)
        y1 = y + size * phi * sin(angle)
        x2 = x + size * cos(angle - delta)
        y2 = y + size * sin(angle - delta)
        tri(x, y, x1, y1, x2, y2, COLOR_OBTUSE)
    else:
        x_ = x + size * cos(angle - flip * radians(36))
        y_ = y + size * sin(angle - flip * radians(36))
        obtuse(x_, y_, size / phi, angle - flip * radians(216), flip=flip, gen=gen - 1)

        x_ = x + size / phi * cos(angle)
        y_ = y + size / phi * sin(angle)
        acute(x_, y_, size / phi, angle - 2 * flip * pi / 5, flip=-flip, gen=gen - 1)

        x_ = x + size * phi * cos(angle)
        y_ = y + size * phi * sin(angle)
        obtuse(x_, y_, size / phi, angle - pi, flip=-flip, gen=gen - 1)


def update():
    global n, x0, y0
    step = 5
    if pyxel.btnp(pyxel.KEY_W):
        n += 1
    if pyxel.btnp(pyxel.KEY_S):
        n = max(0, n - 1)
    if pyxel.btn(pyxel.KEY_UP):
        y0 += step
    if pyxel.btn(pyxel.KEY_DOWN):
        y0 -= step
    if pyxel.btn(pyxel.KEY_LEFT):
        x0 += step
    if pyxel.btn(pyxel.KEY_RIGHT):
        x0 -= step

    pyxel.camera(-pyxel.width / 2 - x0, -pyxel.height / 2 - y0)


def draw():
    pyxel.cls(0)

    size = 1024
    for i in range(5):
        x = -size * phi * cos(2 * pi * i / 5)
        y = -size * phi * sin(2 * pi * i / 5)
        obtuse(x, y, size, radians(72 * i), flip=-1, gen=n)
        obtuse(x, y, size, radians(72 * i), flip=+1, gen=n)
        # acute(0, 0, size, radians(72 * i), flip=+1, gen=n)


pyxel.init(1024, 1024)
pyxel.camera(-pyxel.width / 2, -pyxel.height / 2)
pyxel.run(update, draw)
