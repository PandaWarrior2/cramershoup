#!/usr/bin/python3
import math
import random
import sympy
import sys

class GF:
    def __init__ (self, p, n = 1):
        p, n = int(p), int(n)


def isSimple(n):
    if n == 1: return 0
    for i in range(2, int(n/2)):
        if not (n % i): return 0
    return 1

def cbin(n):
    return str(bin(n))[2:]

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
def find_qd(mod):
    ds = []
    for i in range(1, mod):
        k = (i**2) % mod
        if k not in ds:
            ds.append(k)
    ds = sorted(ds)
    return ds
# MAIN
values = []
print("Cramer-Shoup sign algorithm")
print("Enter l (bit length)")
b_len = int(sys.argv[1])
print("1. Генерация ключей: ")
p,q = gen_int(b_len, 1), gen_int(b_len, 1)
n = p * q
h, x = (random.randint(1, n) ** 2) % n, (random.randint(1, n) ** 2) % n
es = gen_int(b_len, 1)
print("Открытый ключ: {n, h, x, e'} = {%s, %s, %s, %s}" % (n, h, x, es))
print("Закрытый ключ: {p,q} = {%s, %s}" % (p,q))

print("2. Формирование подписи: ")
M = gen_int(b_len, 0)
p,q,n,h,x,es,M = 17,23,391,246,140,29, 28
print("M = " + str(M) + " ; H(M) = " + str(H(M)))
e = es
while(e == es):
    e = gen_int(b_len, 1)
ys = random.randint(1,n) ** 2 % n
ys = 324
e = 19

xs = 0
print("Ищем x' из уравнения: %s**%s = (x')%s**%s" % ( ys, es, h, H(M)))
for i in range(1, n):
    result = ((ys**es % n) == (xs*(h**H(M)) % n))
    if result:
        break
    else:
        xs += 1
print("x' = " + str(xs) + " ; H(x') = " + str(H(xs)))
y = 0
print("Ищем y из уравнения: y**%s = %s*%s**%s" % (e, x, h, H(xs)))
for i in range(1, n):
    #print("%s**%s = %s(%s**%s) mod %s" % (ys, es, xs, h, H(M), n))
    result = (y**e % n) == ((x*(h**H(xs))) % n)
    if result:
        break
    else:
        y += 1
print("y = " + str(y))
print("Цифровая подпись: {e, y, y'} = {%s, %s, %s}" % (e, y, ys))

print("3. Проверка подписи: ")
print(e, len(cbin(e)) == b_len)
print(x, ((y**e) * (h**(-H(xs)))) % n)
result = (x % n == ((y**e)*(h**(-H(xs)))) % n)
print(result)
print(xs, ((ys**es)*(h**(-H(M)))) % n)
result = (xs == ((ys**es)*(h**(-H(M)))) % n)
print(result)
