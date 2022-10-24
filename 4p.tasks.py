# Sukurkite ir išsibandykite funkcijas, kurios:


# 1 Gražinti trijų paduotų skaičių sumą.
def sk_sum(sk1, sk2, sk3):
    return sum(sk1, sk2, sk3)

try:
    a = float(input("Iveskite pirma skaiciu: "))
    b = float(input("Iveskite antra skaiciu: "))
    c = float(input("Iveskite trecia skaiciu: "))
    print(sk_sum(a, b, c))
except ValueError:
    print("Ivedete ne skaiciu")


# 2 Gražintų paduoto sąrašo iš skaičių, sumą.
listas = [1, 2, 3, 4, 10]
def suma(*args):
    result = 0
    for i in args:
        result += i
    return result
    # return sum(args)

print(suma(*listas))
def suma_multi(*args):
   return sum(args)
print(suma_multi(1, 3, 6)


# 3 Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
def biggest(*args):
    k = 0
    for i in args:
        if i > k:
            k = i
    return i

print(biggest(1, 2, 3, 4, 5))


4 Gražintų paduotą stringą atbulai.
def backwards(stringas):
    return stringas[::-1]

print(backwards("Sveiki"))


# 5. Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.
def symbol_stats(text):
    num_of_words = len(text.split())
    capital_letters = 0
    lower_letter = 0
    digits = 0
    for char in text:
        if char.isupper():
            capital_letters += 1
        elif char.islower():
            lower_letter += 1
        elif char.isdigit():
            digits += 1
    print(f''' Tekste yra:
    Zodziu: {num_of_words},
    Didziuju raidziu: {capital_letters},
    Mazuju raidziu: {lower_letter},
    skaitmenu: {digits}
    ''')

print(symbol_stats("mano Batai buvo 2"))

# 6. Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.
def unique_nums(*args):
    return set(args)

print(unique_nums("as", "as", "Jonas", 12, 31, 1, 12, 12, "as"))


# 7. Gražintų, ar paduotas skaičius yra pirminis.
def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
            return True
    return True

print(is_prime(7))
print(is_prime(2))

# 8. Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo
def atbulai(text):
    listas = text.split()[::-1]
    return " ".join(listas)

print(atbulai("viens du trys"))


# 9. Gražina, ar paduoti metai yra keliamieji, ar ne.
from calendar import isleap

def ar_keliamieji(metai):
    return isleap(metai)

print(ar_keliamieji(2000))

