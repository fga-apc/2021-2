import pyxel
import random
from math import sqrt

pyxel.init(160, 120)
pyxel.load("arte.pyxres")

# Inicializa os círculos
RADIUS = 4
COLOR_ACTIVE = pyxel.COLOR_RED
COLOR_SLEEP = pyxel.COLOR_PURPLE
STEP = 2

pyxel.game_over = False
pyxel.x1 = random.uniform(20, 140)
pyxel.y1 = random.uniform(20, 100)
pyxel.sleep1 = False
pyxel.x2 = random.uniform(20, 140)
pyxel.y2 = random.uniform(20, 100)
pyxel.sleep2 = False
pyxel.x3 = random.uniform(20, 140)
pyxel.y3 = random.uniform(20, 100)
pyxel.sleep3 = False


def in_circle(x, y, cx, cy):
    """
    Verifica se o ponto (x, y) está dentro do círculo de
    raio cx, cy
    """
    dist = sqrt((x - cx) ** 2 + (y - cy) ** 2)
    return dist <= RADIUS


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    if pyxel.frame_count > 30 * 2:
        if not (pyxel.sleep1 == pyxel.sleep2 == pyxel.sleep3 == True):
            pyxel.game_over = True

    if not pyxel.game_over:
        check_mouse_click()
        update_positions()


def check_mouse_click():
    """
    Verifica se o click do mouse se encontra em algum círculo
    e adormece o círculo correspondente.
    """
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.play(0, 0)

        if in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x1, pyxel.y1):
            pyxel.sleep1 = True

        if in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x2, pyxel.y2):
            pyxel.sleep2 = True

        if in_circle(pyxel.mouse_x, pyxel.mouse_y, pyxel.x3, pyxel.y3):
            pyxel.sleep3 = True


def update_positions():
    """
    Atualiza a posição dos círculos de acordo com o passo
    do bêbado
    """
    if not pyxel.sleep1:
        pyxel.x1 = pyxel.x1 + random.uniform(-STEP, STEP)
        pyxel.y1 = pyxel.y1 + random.uniform(-STEP, STEP)

    if not pyxel.sleep2:
        pyxel.x2 = pyxel.x2 + random.uniform(-STEP, STEP)
        pyxel.y2 = pyxel.y2 + random.uniform(-STEP, STEP)

    if not pyxel.sleep3:
        pyxel.x3 = pyxel.x3 + random.uniform(-STEP, STEP)
        pyxel.y3 = pyxel.y3 + random.uniform(-STEP, STEP)


def draw():
    pyxel.cls(0)
    pyxel.bltm(0, 0, tm=0, u=0, v=0, w=160, h=120, colkey=pyxel.COLOR_BLACK)
    draw_circles()
    draw_messages()


def draw_circles():
    x, y = pyxel.x1 - RADIUS, pyxel.y1 - RADIUS
    if pyxel.sleep1:
        u = 24
    else:
        u = (pyxel.frame_count // 5 % 3) * 8
    pyxel.blt(x, y, img=0, u=u, v=0, w=8, h=8, colkey=pyxel.COLOR_BLACK)

    x, y = pyxel.x2 - RADIUS, pyxel.y2 - RADIUS
    if pyxel.sleep2:
        u = 24
    else:
        u = (pyxel.frame_count // 5 % 3) * 8
    pyxel.blt(x, y, img=0, u=u, v=9, w=8, h=8, colkey=pyxel.COLOR_BLACK)

    x, y = pyxel.x3 - RADIUS, pyxel.y3 - RADIUS
    if pyxel.sleep3:
        u = 24
    else:
        u = (pyxel.frame_count // 5 % 3) * 8
    pyxel.blt(x, y, img=0, u=u, v=18, w=8, h=8, colkey=pyxel.COLOR_BLACK)


def draw_messages():
    if pyxel.game_over:
        x = 80 - 5 * pyxel.FONT_WIDTH
        pyxel.text(x + 1, 60 + 1, "GAME OVER!", pyxel.COLOR_YELLOW)
        if (pyxel.frame_count // 5) % 2 == 0:
            pyxel.text(x - 1, 60, "GAME OVER!", pyxel.COLOR_LIME)
        pyxel.text(x, 60, "GAME OVER!", pyxel.COLOR_WHITE)

    if pyxel.sleep1 == pyxel.sleep2 == pyxel.sleep3 == True:
        x = 80 - 5 * pyxel.FONT_WIDTH
        pyxel.text(x + 1, 60 + 1, "YOU WON! :)", pyxel.COLOR_YELLOW)
        if (pyxel.frame_count // 5) % 2 == 0:
            pyxel.text(x - 1, 60, "YOU WON! :)", pyxel.COLOR_ORANGE)
        pyxel.text(x, 60, "YOU WON! :)", pyxel.COLOR_RED)


pyxel.playm(0, loop=True)
pyxel.mouse(True)
pyxel.run(update, draw)
