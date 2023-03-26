#!/usr/bin/env python3

import random
import math
import sys
from multiprocessing import Pool, cpu_count

def check_guess(item):
    if item is None:
        return
    g, n = item
    r = find_r(g, n)
    if r is None or r % 2 == 1:
        return
    middle = g ** (r // 2)
    left = middle + 1
    right = middle - 1
    factor1 = math.gcd(left, n)
    factor2 = n // factor1
    if factor1 != 1 and factor2 != 1:
        return (factor1, factor2)
    return None


def factor(n):
    with Pool(cpu_count()) as p:
        for item in p.imap(check_guess, ((i, n) for i in range(2, n))):
            if item is not None:
                return item

def find_r(g, n):
    r = 1
    steps = 0
    while pow(g, r, n) != 1:
        if steps > 100_000:
            return
        r += 1
        steps += 1
    return r


def main(num):
    result = factor(num)
    if result is not None:
        f1, f2 = result
        print(f"{f1} {f2}")
        return
    sys.stderr.write(f"Couldn't factorize {num} into two distinct primes.")

if __name__ == '__main__':
    main(int(sys.argv[1]))

