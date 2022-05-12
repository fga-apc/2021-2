from typing import List, Tuple

notes = [10000, 5000, 2000, 1000, 500, 200]
coins = [100, 50, 25, 10, 5, 1]
Distrib = List[Tuple[int, int]]


def money_distrib(cents: int, values: List[int]) -> Distrib:
    distrib = []
    for v in values:
        n = cents // v
        cents -= n * v
        distrib.append((v, n))
    return distrib, cents


def print_money_distrib(distrib: Distrib, name: str) -> None:
    for v, n in distrib:
        print(f"{n} {name} de R$ {v * 0.01:.2f}")


if __name__ == "__main__":
    real, cents = map(int, input().split("."))
    cents = real * 100 + cents

    print("NOTAS:")
    distrib, cents = money_distrib(cents, notes)
    print_money_distrib(distrib, "nota(s)")

    print("MOEDAS:")
    distrib, cents = money_distrib(cents, coins)
    print_money_distrib(distrib, "moeda(s)")
