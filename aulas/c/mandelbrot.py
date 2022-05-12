import pyxel
import time
from ctypes import cdll, c_int, c_double

COLORS = {
    1: 8,
    2: 9,
    3: 10,
    4: 11,
    5: 12,
    6: 13,
    7: 14,
}

cmodule = cdll.LoadLibrary("./mandelbrot.so")
mandelbrot = cmodule.mandelbrot
mandelbrot.argtypes = (c_double, c_double, c_int)
mandelbrot.restype = c_int


def init():
    global scale, x0, y0

    size = 256
    pyxel.init(size, size, title="Mandelbrot", fps=15)
    pyxel.mouse(True)

    scale = 1.5  # Fator de escala
    x0 = -0.5
    y0 = 0.0


def update():
    global scale, x0, y0
    ZOOM_FACTOR = 1.05
    STEP = scale * 0.03

    if pyxel.btn(pyxel.KEY_A):
        scale /= ZOOM_FACTOR
    if pyxel.btn(pyxel.KEY_Z):
        scale *= ZOOM_FACTOR

    if pyxel.btn(pyxel.KEY_LEFT):
        x0 -= STEP
    if pyxel.btn(pyxel.KEY_RIGHT):
        x0 += STEP
    if pyxel.btn(pyxel.KEY_UP):
        y0 -= STEP
    if pyxel.btn(pyxel.KEY_DOWN):
        y0 += STEP


def draw():
    """
    Calcula os coeficientes
    x = m i + c   (x in [-2, 1])
    (x0 - s) = m 0 + c  => c = -2
    (x0 + s) = m N + c  => m = 3 / N

    c = x0 - s
    c + m N = x0 + s

    2c + mN = 2 x0
    mN = 2 s
    m = 2 s / N

    2c + 2s = 2x0
    c + s = x0
    c = x0 - s
    """
    pyxel.cls(pyxel.COLOR_BLACK)

    t0 = time.time()
    N = pyxel.width
    mx = 2 * scale / N
    my = 2 * scale / N
    cx = x0 - scale
    cy = y0 - scale

    for i in range(N):
        for j in range(N):
            x = mx * i + cx
            y = my * j + cy
            color = mandelbrot(x, y, 100)

            if color == 0:
                pyxel.pset(i, j, pyxel.COLOR_WHITE)
            else:
                color = COLORS.get(color, pyxel.COLOR_BLACK)
                pyxel.pset(i, j, color)

    dt_ms = int(1000 * (time.time() - t0))
    pyxel.text(0, 0, f"dt = {dt_ms}ms", pyxel.COLOR_GREEN)


init()
pyxel.run(update, draw)
