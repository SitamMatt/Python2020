# sieve of Eratosthenes

from math import sqrt


def sieveOfEratosthenes(start, end):
    res = []
    it = start
    while it <= end:
        res.append(it)
        it += 1
    det = sqrt(end)
    ind = 2
    while ind <= det:
        for i in res:
            if (i % ind == 0) & (i != ind):
                res.remove(i)
        ind += 1
    return res



