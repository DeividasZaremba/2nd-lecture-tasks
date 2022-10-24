# 1 uzduotis

men = ["Sausis", "Vasaris", "Kovas"]
print(men[0])
men.append("Balandis")
print(men)
men.pop(1)
print(men)
men[0] = "January"
print(men)
men.clear()

zodynas = {"sausis": "January",
           "Vasaris": "February",
           "Kovas": "march"
           }
zodynas["Balandis"] = "April"
print(zodynas)
zodynas["Kovas"] = "March"
print(zodynas)
del zodynas["Kovas"]
print(zodynas)
zodynas.clear()
print(zodynas)


#################
# 2 uzduotis
import time
total = 0
num = 0
while num >= 0:
    num = int(input("Iveskite skaiciu: "))
    if num >= 0:
        total += num
    else:
        break
print("Skaiciuojama ivestu teigiamu skaiciu suma")
time.sleep(1.50)
print("Beveik suskaiciavau")
time.sleep(2.00)
print(f"Jusu ivestu teigiamu skaiciu suma yra {total}.")

#################
# 3 uzduotis (sudetingiau)
a = input("Iveskite kiek norite zodziu, atskirtu tarpais: ")
b = a.split()
print(b)
for i in b:
    print("Zodis: " + i)
    print("Zodzio ilgis: " + str(len(i)))
    print("Zodzio eiles numeris sarase: " + str(b.index(i)))
    print("--------")
print("Saraso pabaiga")

#################
# 4 uzduotis
import random
list = []
while len(list) < 3:
    num = random.randint(1, 6)
    list.append(num)
    print(list)
if 5 in list:
    print("Pralaimejai...")
else:
    print("Laimejai!")


#################
# 5 uzduotis
metai = int(input("Iveskite metus: "))
if metai <= 0:
    print("Metai neegzistuoja")
elif metai % 400 == 0:
    print("Keliamieji metai")
elif metai % 4 == 0:
    if metai % 100 == 0:
        print("Nekeliamieji metai")
    else:
        print("Keliamieji metai")


#################
# 6 uzduotis - Perdaryti 5 užduoti taip, kad programa atspausdintų visus keliamuosius metus, nuo 1900 iki 2100 metų.
for i in range(1900, 2100):
    if i % 4 == 0:
        if i % 100 == 0:
            if i % 400 == 0:
                print(i)
            continue
        print(i)