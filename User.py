from Utils import applyDoubleAndAddMethod, findModInverse, findPositiveModulus
from Curve import getBase, getP

class User:
    def __init__(self, name: str, secret_key: int):
        self.name = name
        self.secret_key = secret_key
        d = findPositiveModulus(-121665 * findModInverse(121666, getP()), getP())
        self.public_key = applyDoubleAndAddMethod(getBase(), secret_key, -1, d, getP())

    def __str__(self) -> str:
        return "Név: " + self.name + ", Titkos kulcs: " + str(self.secret_key) + " Publikus kulcs: " + str(self.public_key)