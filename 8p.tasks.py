# 1 uzduotis
sakinys = "Pirmas sakinys. Random zodziai. Ieskau gyvenimo prasmes. Nieko nebemoku daryt."
sakinys = sakinys.split(".")
for a in sakinys:
    if a == "":
        sakinys.remove("")
# print(sakinys)

apvalytas = []
for a in sakinys:
    if a != " ":
        ab = a.lstrip(" ")
        apvalytas.append(ab)

naujas_sakinys = [x + "!" for x in apvalytas]
for a in naujas_sakinys:
    print(a)


# 2 uzduotis
sarasas = range(0, 51)
iks10 = map(lambda x: x * 10, sarasas)
print(list(iks10))

is7 = [x for x in sarasas if x % 7 == 0]
print (is7)

kvadratu = [x**2 for x in sarasas]
print(kvadratu)

suma = sum(x for x in kvadratu)
print(suma)

maziausias = min(x for x in kvadratu)
print(maziausias)

didziausias = max(x for x in kvadratu)
print(didziausias)

from statistics import mean, median

vidurkis = mean(kvadratu)
print(vidurkis)

medianas = median(kvadratu)
print(medianas)

atbulai = sorted(kvadratu, reverse=True)
print(atbulai)


# 3 uzduotis
from functools import reduce

sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
intai = list(filter(lambda x: type(x) is int, sarasas))
floatai = list(filter(lambda x: type(x) is float, sarasas))
skaiciai = intai + floatai

for i in skaiciai:
    if i == int:
        i = float(i)

def skaiciu_suma(self):
    x = reduce(lambda x, y: x + y, self)
    return x

print(skaiciu_suma(skaiciai))


def zodziu_suma(self):
    zodziai = filter(lambda x: type(x) is str, self)
    zodziai = " ".join(zodziai)
    return zodziai

print(zodziu_suma(sarasas))


def true_booleanai(self):
    true_boolean = sum(b is True for b in self)
    return true_boolean

print(true_booleanai(sarasas))

# 4 uzduotis
class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return (f'{self.vardas}: {self.amzius}')


z1 = Zmogus("Ignas", 34)
z2 = Zmogus("Rimvydas", 33)
z3 = Zmogus("Rolandas", 32)
sarasas = [z1, z2, z3]

from operator import attrgetter

surusiuotas_v = sorted(sarasas, key=attrgetter("vardas"))
print(surusiuotas_v)
naujas = sorted(sarasas, key=lambda z: z.vardas)
print(naujas)
surusiuotas_a = sorted(sarasas, key=attrgetter("amzius"))
print(surusiuotas_a)
naujas = sorted(sarasas, key=lambda z: z.amzius)
print(naujas)