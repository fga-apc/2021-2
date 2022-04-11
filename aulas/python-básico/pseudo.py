# Seção de comandos
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media <= 6.9:
    print("A media do(a) aluno(a) foi: ", media)
    print(" - aluno(a) reprovado(a) ")

if media >= 7:
    print("A media do(a) aluno(a) foi: ", media)
    print(" - aluno(a) aprovado(a) ")
