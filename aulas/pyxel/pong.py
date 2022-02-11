import pyxel
import random


class Player:
    HEIGHT = 12
    WIDTH = 3
    COLOR = pyxel.COLOR_WHITE

    def __init__(self, x):
        self.x = x
        self.y = pyxel.height / 2 - self.HEIGHT / 2
        self.score = 0

    def update(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 1

    def collide_ball(self, ball):
        xmin = max(self.xmin(), ball.xmin())
        xmax = min(self.xmax(), ball.xmax())

        ymin = max(self.ymin(), ball.ymin())
        ymax = min(self.ymax(), ball.ymax())

        if xmax >= xmin and ymax >= ymin:
            ball.vx = -ball.vx
            ball.update()

    def draw(self):
        pyxel.rect(self.x, self.y, self.WIDTH, self.HEIGHT, self.COLOR)

    def xmax(self):
        return self.x + self.WIDTH

    def xmin(self):
        return self.x

    def ymax(self):
        return self.y + self.HEIGHT

    def ymin(self):
        return self.y


class Ball:
    RADIUS = 3
    COLOR = pyxel.COLOR_WHITE

    def __init__(self):
        self.x = pyxel.width / 2
        self.y = pyxel.height / 2
        self.vx = random.choice([-1, 1])
        self.vy = random.choice([-1, 1])

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # Verifica a colisão com o topo da tela
        if self.y < self.RADIUS:
            self.vy = +abs(self.vy)

        # Verifica a colisão com a parte de baixo da tela
        if self.y > pyxel.height - self.RADIUS:
            self.vy = -abs(self.vy)

    def draw(self):
        pyxel.circ(self.x, self.y, self.RADIUS, self.COLOR)

    def xmax(self):
        return self.x + self.RADIUS

    def xmin(self):
        return self.x - self.RADIUS

    def ymax(self):
        return self.y + self.RADIUS

    def ymin(self):
        return self.y - self.RADIUS


class Game:
    def __init__(self):
        self.ball = Ball()
        self.player1 = Player(x=2)
        self.player2 = Player(x=pyxel.width - Player.WIDTH - 2)
        self.is_paused = True

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)

        x_max = pyxel.width
        y_max = pyxel.height - 1
        x_middle = pyxel.width / 2

        pyxel.line(0, 0, x_max, 0, pyxel.COLOR_WHITE)
        pyxel.line(0, y_max, x_max, y_max, pyxel.COLOR_WHITE)
        pyxel.line(x_middle, 5, x_middle, y_max - 5, pyxel.COLOR_PURPLE)

        self.ball.draw()
        self.player1.draw()
        self.player2.draw()

        if self.is_paused and (pyxel.frame_count // 7) % 2 == 0:
            x = pyxel.width / 2 - 4 * pyxel.FONT_WIDTH
            pyxel.text(x, (2 / 3) * pyxel.height, "PAUSADO!", pyxel.COLOR_WHITE)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.is_paused = not self.is_paused

        if not self.is_paused:
            self.ball.update()
            self.player1.update()
            self.player2.update()
            self.player1.collide_ball(self.ball)
            self.player2.collide_ball(self.ball)

    def run(self):
        pyxel.run(self.update, self.draw)


pyxel.init(120, 80)
pyxel.mouse(True)
game = Game()
# Game.run(game)
game.run()
