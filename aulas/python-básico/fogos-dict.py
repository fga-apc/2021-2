import pyxel
import random
import math

GRAVIDADE = 100.0
VELOCIDADE = 50
DT = 1.0 / 30.0


def nova_bola(pos, vel):
    return {"pos": pos, "vel": vel, "cor": 1, "alive": True}


def init():
    """
    Inicializa o jogo.
    """
    pyxel.init(120, 80, fps=30)
    pyxel.mouse(True)
    pyxel.bolas = []


def update():
    """
    Atualiza física do jogo.
    """
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        pos = [pyxel.mouse_x, pyxel.mouse_y]
        vel = vetor_aleatorio(VELOCIDADE)
        pyxel.bolas.append(nova_bola(pos, vel))
    else:
        for bola in pyxel.bolas:
            vel = bola["vel"]
            pos = bola["pos"]

            if bola["alive"]:
                bola["vel"] = passo(vel, [0, GRAVIDADE])
                bola["pos"] = passo(pos, vel)
            if pyxel.frame_count % 7 == 0:
                bola["cor"] = (bola["cor"] + 1) % 16

            if random.random() < 0.001:
                bola["alive"] = False


def draw():
    """
    Desenha elementos na tela.
    """
    pyxel.cls(0)
    for bola in pyxel.bolas:
        x, y = bola["pos"]
        pyxel.circ(x, y, 4, bola["cor"])


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
