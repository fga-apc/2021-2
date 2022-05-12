def show_nums(lst, nome):
    for i, x in enumerate(lst):
        print(f"{nome}[{i}] = {x}")


par = []
impar = []

for i in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
        if len(par) == 5:
            show_nums(par, "par")
            par.clear()
    else:
        impar.append(n)
        if len(impar) == 5:
            show_nums(impar, "impar")
            impar.clear()

show_nums(impar, "impar")
show_nums(par, "par")
