import math


def generalizedGCD(num, arr):
    imax = min(arr)
    imin = 2

    for i in range(imax, imin - 1, -1):
        ok = True
        for a in arr:
            if a % i != 0:
                ok = False
                break

        if ok:
            return i

    return 1

print(generalizedGCD(3, [10, 5, 20]))