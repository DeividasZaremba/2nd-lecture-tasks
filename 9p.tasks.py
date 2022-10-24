# 1 uzduotis
import datetime

now_datetime = datetime.datetime.now()
print(now_datetime)

now_date = datetime.date.today()
print(now_date)

now_time = datetime.datetime.now().time()
print(now_time)

from datetime import date

now_date = date.today()
print(now_date)

from datetime import date as data
now_date = data.today()
print(now_date)


# 2 uzduotis
import modulis

print(modulis.kintamasis)
modulis.funkcija()
modulis.Objektas()


# 3 uzduotis

from p6tasks import Irasas, Biudzetas, PajamuIrasas, IslaiduIrasas

biudzetas = Biudzetas()

while True:
    print("\n/// ------- Biudzeto konsole ------ ///\n"
          "/// 1 - Prideti pajamas             ///\n"
          "/// 2 - Prideti islaidas            ///\n"
          "/// 3 - Perziureti balansa          ///\n"
          "/// 4 - Perziureti ataskaita        ///\n"
          "/// 9 - Uzdaryti biudzeto tvarkykle ///\n"
          "///////////////////////////////////////")

    selection = int(input("Pasirinkite: "))

    if selection == 1:
        suma = float(input("Iveskite suma: "))
        siuntejas = input("Iveskite siunteja: ")
        papildoma_info = input("Iveskite papildoma info: ")
        biudzetas.prideti_pajamas(suma, siuntejas, papildoma_info)

    if selection == 2:
        suma = float(input("Iveskite suma: "))
        atsiskaitymo_budas = input("Iveskite atsiskaitymo buda: ")
        isigyta_preke_paslauga = input("Iveskite preke ar paslauga: ")
        biudzetas.prideti_islaidas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)

    elif selection == 3:
        biudzetas.gauti_balansa()

    elif selection == 4:
        biudzetas.gauti_ataskaita()

    elif selection == 9:
        print("Biudzeto tvarkymas uzdaromas")
        break

    else:
        print("Klaida, toks pasirinkimas neegzistuoja\nPasirinkite viena is duotu numeriu ")

