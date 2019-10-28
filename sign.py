#!/usr/bin/python3
import math
import random
import sympy

class GF:
    def __init__ (self, p, n = 1):
        p, n = int(p), int(n)


def isSimple(n):
    if n == 1: return 0
    for i in range(2, int(n/2)):
        if not (n % i): return 0
    return 1

def cbin(n):
    return len(str(bin(n))[3:])

def H(x):
    sum = 0
    x_bin = cbin(x)
    for i in x_bin:
        if i == '1':
            sum += 1
    return sum
def gen_int(bit_len, simp):
    randint = -1
    while(1):
        randint = random.randint(2**(bit_len-1), (2**bit_len)-1)
        if simp and isSimple(randint):
            break
        elif not simp:
            break
    return randint
# MAIN
print("Cramer-Shoup sign algorithm")
print("Enter l (bit length)")
len = int(input())
p = gen_int(len, 1)
q = gen_int(len, 1)
n = p * q
print("p = " + str(p) + " ; q = " + str(q))
print("n = " + str(n))
