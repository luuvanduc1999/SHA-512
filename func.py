import math

def stringToBinary(s):
    return ' '.join('{0:08b}'.format(ord(x), 'b') for x in s)

def intToBinary(x, y):
    if y == 128:
        return "{0:0128b}".format(x)
    if y == 64:
        return "{0:064b}".format(x)

def xor(a, b):
    s = ''

    for i in range(len(b)):
        if a[i] == b[i]:
            s += '0'
        else:
            s += '1'
    return s

def RS187(s):
    x = xor(ROTR(s, 1), ROTR(s, 8))
    return xor(x, SHR(s, 7))

def ROTR(s, x):
    return s[len(s) - x:] + s[:len(s) - x]


def SHR(s, x):
    st = '0000000'
    return st[:x] + s[:len(s) - x]  # s[x:] + st[:x]

def RS19616(s):
    x = xor(ROTR(s, 19), ROTR(s, 61))
    return xor(x, SHR(s, 6))

def additionModulo(s1, s2):
    x = 0
    l1=len(s1)
    for i in range(l1):
        if s1[i] == '1':
            x += int(math.pow(2, len(s1) - 1 - i))

    y = 0
    l2=len(s2)
    for i in range(l2):
        if s2[i] == '1':
            y += int(math.pow(2, len(s2) - 1 - i))

    return intToBinary(int((x + y) % (2 ** 64)), 64)

def RA(m):
    x = xor(ROTR(m, 28), ROTR(m, 34))
    return xor(x, ROTR(m, 39))    

def maj(m, n, o):
    s = ''
    l=len(m)
    for i in range(l):
        s += str((int(m[i]) & int(n[i])) ^ (int(m[i]) & int(o[i])) ^ (int(n[i]) & int(o[i])))

    return s    

def conditional(m, n, o):
    s = ''
    l=len(m)
    for i in range(l):
        if m[i] == '1':
            s += n[i]
        else:
            s += o[i]

    return s

def RE(m):
    x = xor(ROTR(m, 14), ROTR(m, 18))
    return xor(x, ROTR(m, 41))        

def hexToBin(s):
    qw = bin(int(s, 16)).zfill(64)
    a, b = qw.split('b')

    l = len(b)

    for i in range(64 - l):
        b = '0' + b

    return b
