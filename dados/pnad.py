import json

# Genero:
HOMEM = 1
MULHER = 2

# Raca:
NA = 0
AMARELO = 1
PRETO = 2
PARDO = 3
INDIGENA = 4
BRANCO = 5


gen_count = {HOMEM: 0, MULHER: 0}
raca_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
raca_renda = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
raca_edu = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
raca_nome = {
    NA: "n/a", 
    AMARELO: "amarelo",
    PRETO: "preto",
    PARDO: "pardo",
    INDIGENA: "indígena",
    BRANCO: "branco",
}

with open("pnad.dat", "r") as fd:
    for line in fd:
        genero, raca, edu, renda = map(int, line.split(","))
        if renda == 0:
            continue
        gen_count[genero] += 1 
        raca_count[raca] += 1
        raca_renda[raca] += renda
        raca_edu[raca] += edu
    
renda_media = {}
for cat in range(1, 6):
    renda_media[cat] = 2 * round(raca_renda[cat] / raca_count[cat], 2)

edu_media = {}
for cat in range(1, 6):
    edu_media[cat] = round(raca_edu[cat] / raca_count[cat], 1)


with open("resumo.csv", "w") as fd:
    fd.write("raca,renda_media,escolaridade_media\n")
    for cat in range(1, 6):
        r = renda_media[cat]
        e = edu_media[cat]
        nome = raca_nome[cat]
        fd.write(f"{nome},{r},{e}\n")

data = {
    "renda": renda_media,
    "edu": edu_media,
    "racas": raca_count,
    "generos": gen_count,
}

with open("data.json", "w") as fd:
    json.dump(data, fd, indent=2)
    
