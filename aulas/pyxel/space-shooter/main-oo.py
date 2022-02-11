import pyxel
import random
from math import sqrt

pyxel.init(160, 120)
pyxel.load("arte.pyxres")

# Inicializa os círculos
RADIUS = 4
COLOR_ACTIVE = pyxel.COLOR_RED
COLOR_SLEEP = pyxel.COLOR_PURPLE
VSTEP = 5


class Enemy:
    def __init__(self):
        self.x = random.uniform(20, 140)
        self.y = random.uniform(20, 100)
        self.vx = 0
        self.vy = 0
        self.sleep = False

    def draw(self, v):
        x, y = self.x - RADIUS, self.y - RADIUS
        if self.sleep:
            u = 24
        else:
            u = (pyxel.frame_count // 5 % 3) * 8
        pyxel.blt(x, y, img=0, u=u, v=v, w=8, h=8, colkey=pyxel.COLOR_BLACK)

    def update(self):
        if not self.sleep:
            dt = 1 / 30.0
            self.vx = self.vx + random.uniform(-VSTEP, VSTEP)
            self.vy = self.vy + random.uniform(-VSTEP, VSTEP)
            self.x = self.x + self.vx * dt
            self.y = self.y + self.vy * dt

    def includes_point(self, x, y):
        """
        Verifica se o ponto (x, y) está dentro do objeto
        """
        dist = sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        return dist <= RADIUS + 2

    def update_click(self, x, y):
        """
        Verifica se o mouse na posição x, y coloca o objeto para dormir.
        """
        if self.includes_point(x, y):
            self.sleep = True


class Game:
    def __init__(self):
        self.game_over = False
        self.e1 = Enemy()
        self.e2 = Enemy()
        self.e3 = Enemy()
        self.e4 = Enemy()

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.frame_count > 30 * 2:
            if not self._is_all_sleeping():
                pyxel.game_over = True

        if not self.game_over:
            self._update_mouse_click()
            self._update_positions()

    def _is_all_sleeping(self):
        return self.e1.sleep == self.e2.sleep == self.e3.sleep == self.e4.sleep == True

    def _update_mouse_click(self):
        """
        Verifica se o click do mouse se encontra em algum círculo
        e adormece o círculo correspondente.
        """
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.play(0, 0)
            x, y = pyxel.mouse_x, pyxel.mouse_y
            self.e1.update_click(x, y)
            self.e2.update_click(x, y)
            self.e3.update_click(x, y)
            self.e4.update_click(x, y)

    def _update_positions(self):
        """
        Atualiza a posição dos círculos de acordo com o passo
        do bêbado
        """
        self.e1.update()
        self.e2.update()
        self.e3.update()
        self.e4.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, tm=0, u=0, v=0, w=160, h=120, colkey=pyxel.COLOR_BLACK)
        self._draw_circles()
        self._draw_messages()

    def _draw_circles(self):
        self.e1.draw(0)
        self.e2.draw(9)
        self.e3.draw(18)
        self.e4.draw(18)

    def _draw_messages(self):
        if self.game_over:
            x = 80 - 5 * pyxel.FONT_WIDTH
            pyxel.text(x + 1, 60 + 1, "GAME OVER!", pyxel.COLOR_YELLOW)
            if (pyxel.frame_count // 5) % 2 == 0:
                pyxel.text(x - 1, 60, "GAME OVER!", pyxel.COLOR_LIME)
            pyxel.text(x, 60, "GAME OVER!", pyxel.COLOR_WHITE)

        if self._is_all_sleeping():
            x = 80 - 5 * pyxel.FONT_WIDTH
            pyxel.text(x + 1, 60 + 1, "YOU WON! :)", pyxel.COLOR_YELLOW)
            if (pyxel.frame_count // 5) % 2 == 0:
                pyxel.text(x - 1, 60, "YOU WON! :)", pyxel.COLOR_ORANGE)
            pyxel.text(x, 60, "YOU WON! :)", pyxel.COLOR_RED)

    def run(self):
        pyxel.run(self.update, self.draw)


pyxel.playm(0, loop=True)
pyxel.mouse(True)
game = Game()
game.run()
