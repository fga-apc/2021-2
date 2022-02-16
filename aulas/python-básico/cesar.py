import pyxel

COR_MSG = pyxel.COLOR_WHITE
COR_CIFRA = pyxel.COLOR_RED
ORD_A = ord("a")
ORD_Z = ord("z")


def init():
    pyxel.init(120, 80, title="Cifra de César")
    pyxel.mouse(True)
    pyxel.msg = "ave cesar"
    pyxel.cesar = "dyh fhvdu"


def update():
    for key in range(pyxel.KEY_A, pyxel.KEY_Z + 1):
        if pyxel.btnp(key):
            pyxel.msg = pyxel.msg + chr(key)

    if pyxel.btnp(pyxel.KEY_SPACE):
        pyxel.msg = pyxel.msg + " "

    if pyxel.btnp(pyxel.KEY_PERIOD):
        pyxel.msg = pyxel.msg + "."

    if pyxel.btnp(pyxel.KEY_BACKSPACE):
        pyxel.msg = pyxel.msg[:-1]

    pyxel.cesar = cesar(pyxel.msg)


def draw():
    pyxel.cls(0)
    y = 30
    pyxel.text(10, y, pyxel.msg, COR_MSG)
    pyxel.text(10, y + 20, pyxel.cesar, COR_CIFRA)

    n = len(pyxel.msg)  # tamanho da mensagem
    cursor_x = 10 + n * pyxel.FONT_WIDTH
    if pyxel.frame_count // 5 % 2 == 0:
        y_final = y + pyxel.FONT_HEIGHT - 2
        pyxel.line(cursor_x, y, cursor_x, y_final, COR_MSG)


def run():
    init()
    pyxel.run(update, draw)


def cesar(st):
    lst = []
    for c in st:
        if ORD_A <= ord(c) <= ORD_Z:
            n = (ord(c) - ORD_A + 3) % 26 + ORD_A
            lst.append(chr(n))
        else:
            lst.append(c)

    return "".join(lst)


if __name__ == "__main__":
    run()
