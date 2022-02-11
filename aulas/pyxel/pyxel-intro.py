import pyxel
import random
from math import sqrt

pyxel.init(160, 120)

# Inicializa os círculos
RADIUS = 5
COLOR_ACTIVE = pyxel.COLOR_RED
COLOR_SLEEP = pyxel.COLOR_PURPLE
STEP = 2


def start_game():
    pyxel.game_over = False
    pyxel.paused = True
    pyxel.n_frames = 30 * 2
    pyxel.x1 = random.uniform(20, 140)
    pyxel.y1 = random.uniform(20, 100)
    pyxel.sleep1 = False
    pyxel.x2 = random.uniform(20, 140)
    pyxel.y2 = random.uniform(20, 100)
    pyxel.sleep2 = False
    pyxel.x3 = random.uniform(20, 140)
    pyxel.y3 = random.uniform(20, 100)
    pyxel.sleep3 = False


def is_winner():
    return pyxel.sleep1 == pyxel.sleep2 == pyxel.sleep3 == True


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

    if pyxel.btnp(pyxel.KEY_SPACE):
        if pyxel.game_over or is_winner():
            start_game()
            pyxel.paused = FAlse
        else:
            pyxel.paused = not pyxel.paused

    if not pyxel.paused and not is_winner():
        pyxel.n_frames = pyxel.n_frames - 1

    if pyxel.n_frames <= 0:
        pyxel.game_over = True

    if not pyxel.game_over and not pyxel.paused:
        check_mouse_click()
        update_positions()


def check_mouse_click():
    """
    Verifica se o click do mouse se encontra em algum círculo
    e adormece o círculo correspondente.
    """
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
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
    pyxel.cls(pyxel.COLOR_BLACK)
    draw_circles()
    draw_messages()


def draw_circles():
    if pyxel.sleep1:
        color = COLOR_SLEEP
    else:
        color = COLOR_ACTIVE
    pyxel.circ(pyxel.x1, pyxel.y1, RADIUS, color)

    if pyxel.sleep2:
        color = COLOR_SLEEP
    else:
        color = COLOR_ACTIVE
    pyxel.circ(pyxel.x2, pyxel.y2, RADIUS, color)

    if pyxel.sleep3:
        color = COLOR_SLEEP
    else:
        color = COLOR_ACTIVE
    pyxel.circ(pyxel.x3, pyxel.y3, RADIUS, color)


def draw_messages():
    if pyxel.game_over:
        x = 80 - 5 * pyxel.FONT_WIDTH
        pyxel.text(x + 1, 60 + 1, "GAME OVER!", pyxel.COLOR_YELLOW)
        if (pyxel.frame_count // 5) % 2 == 0:
            pyxel.text(x - 1, 60, "GAME OVER!", pyxel.COLOR_LIME)
        pyxel.text(x, 60, "GAME OVER!", pyxel.COLOR_WHITE)
    elif is_winner():
        x = 80 - 5 * pyxel.FONT_WIDTH
        pyxel.text(x + 1, 60 + 1, "YOU WON! :)", pyxel.COLOR_YELLOW)
        if (pyxel.frame_count // 5) % 2 == 0:
            pyxel.text(x - 1, 60, "YOU WON! :)", pyxel.COLOR_CYAN)
        pyxel.text(x, 60, "YOU WON! :)", pyxel.COLOR_RED)
    elif pyxel.paused and (pyxel.frame_count // 10) % 2 == 0:
        x = pyxel.width / 2 - 4 * pyxel.FONT_WIDTH
        pyxel.text(x, 60, "PAUSADO!", pyxel.COLOR_WHITE)


start_game()
pyxel.mouse(True)
pyxel.run(update, draw)
