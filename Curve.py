p = 2 ** 255 - 19
y = 4 * pow(5, -1, p)


def inv(number):
    return pow(number, p - 2, p)


c = -121665 * inv(121666)
i = pow(2, (p - 1) // 4, p)


def findx(number):
    xx = (number * number - 1) * inv(c * number * number + 1)
    foundx = pow(xx, (p + 3) // 8, p)
    if (foundx * foundx - xx) % p != 0:
        foundx = (foundx * i) % p
    if foundx % 2 != 0:
        foundx = p - foundx
    return foundx


x = findx(y)

base = x, \
       y


def getBase():
    return base


def getP():
    return p