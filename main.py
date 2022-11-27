# https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication
from User import User
from Utils import findPositiveModulus, setTextToInt, findModInverse, applyDoubleAndAddMethod, pointAddition, hashing
from Signature import createSigniture
from Curve import getBase, getP
import random

# ax^2 + y^2  = 1 + dx^2y^2
# ed25519
a = -1
d = findPositiveModulus(-121665 * findModInverse(121666, getP()), getP())

print("Görbe: ", a, "x^2 + y^2 = 1 +", d, "x^2 y^2")
print("---------[Kulcsgenerálás]---------")
# privateKey = 47379675103498394144858916095175689
# 779086087640336534911165206022228115974270 #32 byte secret key
Tibor = None # User(name="Tibor", secret_key=5)
if Tibor:
    privateKey = Tibor.secret_key
    print("Név: " + Tibor.name)
else:
    privateKey = random.getrandbits(256)  # 32 byte secret key

print("Privát kulcs: ", privateKey)
publicKey = applyDoubleAndAddMethod(getBase(), privateKey, a, d, getP())
print("Publikus kulcs: ", publicKey)
message = setTextToInt("Kriptográfia")
r, R = createSigniture(getBase(), a, d, getP(), message)
h = hashing(R[0] + publicKey[0] + message) % getP()
s = (r + h * privateKey)

print("---------[Aláírás]---------")
print("Üzenet: ", message)
print("Signature (R, s)")
print("R: ", R)
print("s: ", s)
# Validáció
h = hashing(R[0] + publicKey[0] + message) % getP()
P1 = applyDoubleAndAddMethod(getBase(), s, a, d, getP())
P2 = pointAddition(R, applyDoubleAndAddMethod(publicKey, h, a, d, getP()), a, d, getP())

print("---------[Validáció]---------")
print("P1: ", P1)
print("P2: ", P2)
print("---------[Eredmény]---------")
if P1[0] == P2[0] and P1[1] == P2[1]:
    print("Az aláírás érvényes.")
else:
    print("Az aláírás NEM érvényes.")
