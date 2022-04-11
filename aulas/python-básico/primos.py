def primes(n):
    ps = []
    for x in range(2, n + 1):
        is_prime = True
        for p in ps:
            if x % p == 0:
                is_prime = False
                break
        if is_prime:
            ps.append(x)
    return ps


def sieve(n):
    ps = list(range(2, n + 1))
    pos = range(len(ps))
    i = 0

    while i < len(ps):
        n = ps[i]
        if n != 0:
            indices = pos[i + n :: n]
            for j in indices:
                ps[j] = 0
        i += 1

    return list(filter(None, ps))


print(sieve(13))
