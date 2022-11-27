from Utils import applyDoubleAndAddMethod, hashing


def createSigniture(base, a, d, p, message):
    r = hashing(hashing(message) + message) % p
    R = applyDoubleAndAddMethod(base, r, a, d, p)
    return r, R
