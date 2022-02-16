import pyxel
import random
import math

GRAVIDADE = 100.0
VELOCIDADE = 50
DT = 1.0 / 30.0


def init():
    """
    Inicializa o jogo.
    """
    pyxel.init(120, 80, fps=30)
    pyxel.mouse(True)
    pyxel.vel_lst = [[0, 0]]
    pyxel.pos_lst = [[60, 100]]


def update():
    """
    Atualiza física do jogo.
    """
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        pos = pyxel.mouse_x, pyxel.mouse_y
        vel = vetor_aleatorio(VELOCIDADE)
        pyxel.pos_lst.append(pos)
        pyxel.vel_lst.append(vel)
    else:
        for i in range(len(pyxel.pos_lst)):
            vel = pyxel.vel_lst[i]
            pos = pyxel.pos_lst[i]
            pyxel.vel_lst[i] = passo(vel, [0, GRAVIDADE])
            pyxel.pos_lst[i] = passo(pos, vel)


def draw():
    """
    Desenha elementos na tela.
    """
    pyxel.cls(0)
    for i, pos in enumerate(pyxel.pos_lst):
        x, y = pos
        pyxel.circ(x, y, 4, i % 15 + 1)


def passo(v, variacao):
    """
    Avança um vetor "v" de acordo com uma taxa de variação.
    """
    x, y = v
    vx, vy = variacao
    return [x + vx * DT, y + vy * DT]


def vetor_aleatorio(tamanho):
    """
    Retorna um vetor aleatório com um tamanho médio específico.
    """
    v = random.uniform(0.5 * tamanho, 1.5 * tamanho)
    angulo = -random.uniform(0, math.pi)
    return [v * math.cos(angulo), v * math.sin(angulo)]


init()
pyxel.run(update, draw)
