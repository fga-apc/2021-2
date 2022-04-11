from turtle import *

KOCH90 = {
    "angulo": 90,
    "regras": {"F": "F+F-F-F+F"},
    "inicial": "F",
}

KOCH60 = {
    "angulo": 60,
    "regras": {"F": "F+F--F+F"},
    "inicial": "F",
}

SIERPINSKI_A = {
    "angulo": 120,
    "regras": {
        "F": "F-G+F+G-F",
        "G": "GG",
    },
    "inicial": "F-G-G",
}

SIERPINSKI_B = {
    "angulo": 60,
    "regras": {
        "F": "G-F-G",
        "G": "F+G+F",
    },
    "inicial": "F",
}

DRAGON = {
    "angulo": 90,
    "inicial": "F",
    "regras": {"F": "F+G", "G": "F-G"},
}

FABIO = {
    "angulo": 45,
    "inicial": "F",
    "regras": {"F": "FF+F+G", "G": "FF-F-GG"},
}

PLANTA = {
    "angulo": 30,
    "inicial": "X",
    "regras": {
        "X": "F+[[X]-X]-F[-FX]+X",
        "F": "FF",
    },
}


def nova_geracao(regras: dict, st: str) -> str:
    passos = []
    for c in st:
        sub_regra = regras.get(c, c)
        passos.append(sub_regra)
    return "".join(passos)


def n_geracoes(regras, st: str, n: int) -> str:
    for _ in range(n):
        st = nova_geracao(regras, st)
    return st


def rodar(fractal, n, passo):
    angulo = fractal["angulo"]
    regras = fractal["regras"]
    st = fractal["inicial"]
    st = n_geracoes(regras, st, n)

    estados = []
    for cmd in st:
        if cmd in "ABFG":
            forward(passo)
        elif cmd == "+":
            left(angulo)
        elif cmd == "-":
            right(angulo)
        elif cmd == "[":
            estados.append((heading(), pos()))
        elif cmd == "]":
            teta, pt = estados.pop()
            pu()
            setheading(teta)
            setpos(pt)
            pd()


left(45)
speed(0)
rodar(PLANTA, n=5, passo=4)
done()
