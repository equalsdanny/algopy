import math


def solution(n):
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])

    max_i = fibs[-1]

    fibs = set(fibs)
    prime = []
    not_prime = set()

    for i in range(2, max_i + 1):
        if i in not_prime:
            continue

        if i in fibs:
            prime.append(i)

        for p in range(2, math.floor(max_i / i)+1):
            not_prime.add(i * p)

    return prime


solution(6)