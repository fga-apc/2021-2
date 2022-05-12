n = p1_acc = p2_acc = media_acc = 0
entrada = open("entrada.txt", "r")
saida = open("saida.txt", "w")

# Ignora a primeira linha do cabeçalho
entrada.readline()

# Lê cada linha do arquivo
print("Notas", file=saida)
for line in entrada:
    nome, mat, p1, p2 = line.split(",")
    p1, p2 = float(p1), float(p2)
    media = (p1 + p2) / 2.0
    p1_acc += p1
    p2_acc += p2
    media_acc += media
    n += 1
    print(f"{nome:>10s} (mat. {mat}): média = {media:.1f}", file=saida)

entrada.close()
print(f"P1 {p1_acc / n:.2f}", file=saida)
print(f"P2 {p2_acc / n:.2f}", file=saida)
print(f"Media {media_acc / n:.2f}!", file=saida)
saida.close()
