import hashlib


def findPositiveModulus(a, p):
    if a < 0:
        a = (a + p * int(abs(a) / p) + p) % p
    return a


def setTextToInt(text):
    encoded_text = text.encode('utf-8')
    hexed = encoded_text.hex()
    result = int(hexed, 16)
    return result


def findGreatest(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    if a < 0:
        a = (a + m * int(abs(a) / m) + m) % m
    if findGreatest(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def applyDoubleAndAddMethod(P, k, a, d, mod):
    additionPoint = (P[0], P[1])
    # 0b1111111001
    kAsBinary = bin(k)
    # 1111111001
    kAsBinary = kAsBinary[2:len(kAsBinary)]
    for i in range(1, len(kAsBinary)):
        currentBit = kAsBinary[i: i + 1]
        additionPoint = pointAddition(additionPoint, additionPoint, a, d, mod)
        if currentBit == '1':
            additionPoint = pointAddition(additionPoint, P, a, d, mod)
    return additionPoint


def pointAddition(P, Q, a, d, mod):
    x1 = P[0]
    y1 = P[1]
    x2 = Q[0]
    y2 = Q[1]
    x3 = (((x1 * y2 + y1 * x2) % mod) * findModInverse(1 + d * x1 * x2 * y1 * y2, mod)) % mod
    y3 = (((y1 * y2 - a * x1 * x2) % mod) * findModInverse(1 - d * x1 * x2 * y1 * y2, mod)) % mod
    return x3, y3


def hashing(string):
    return int(hashlib.sha512(str(string).encode("utf-8")).hexdigest(), 16)
