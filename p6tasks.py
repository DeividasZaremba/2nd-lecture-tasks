### 1 uzduotis
class Automobilis():
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print(metai, modelis, kuro_tipas)

    def vaziuoti(self):
        print("Vaziuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai ipilti")


class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print("Baterija ikrauta")

    def vaziuoti_autonomiskai(self):
        print("Vaziuoja autonomiskai")


volvo = Automobilis("2018", "S60", "Benzinas")
volvo.vaziuoti()
volvo.stoveti()
volvo.pildyti_degalu()

tesla = Elektromobilis("2022", "X", "Elektra")
tesla.vaziuoti()
tesla.stoveti()
tesla.pildyti_degalu()
tesla.vaziuoti_autonomiskai()

### 2 uzduotis
import datetime

now = datetime.datetime.today()
date_format = "%Y-%m-%d"


class Darbuotojas():
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = datetime.datetime.strptime(dirba_nuo, date_format)

    def kiek_dirba(self):
        kiek = (now - self.dirba_nuo)
        print(kiek.days)

    def paskaiciuoti_atlyginima(self):
        kiek = (now - self.dirba_nuo)
        atlyginimas = self.valandos_ikainis * kiek.days * 8 / 3
        print(atlyginimas)


class NormalusDarbuotojas(Darbuotojas):
    def paskaiciuoti_atlyginima(self):
        kiek = (now - self.dirba_nuo)
        atlyginimas = round(self.valandos_ikainis * kiek.days / 7 * 5 * 8 / 3)
        print(atlyginimas)


jonas = Darbuotojas("Jonas", 15, "2022-09-01")
petras = NormalusDarbuotojas("Petras", 25, "2022-09-10")
jonas.paskaiciuoti_atlyginima()
petras.paskaiciuoti_atlyginima()

### 3 uzduotis
class Irasas:
    def __init__(self, suma):
        self.suma = suma


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_info = papildoma_info


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga


class Biudzetas:
    def __init__(self):
        self.biudzetas = []

    def prideti_pajamas(self, suma, siuntejas, papildoma_info):
        self.biudzetas.append(PajamuIrasas(suma, siuntejas, papildoma_info))

    def prideti_islaidas(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        self.biudzetas.append(IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga))

    def gauti_balansa(self):
        total = 0
        for x in self.biudzetas:
            if isinstance(x, PajamuIrasas):
                total += x.suma
            if isinstance(x, IslaiduIrasas):
                total -= x.suma
        print(f'Biudzeto suma: {total}')

    def gauti_ataskaita(self):
        for x in self.biudzetas:
            if isinstance(x, PajamuIrasas):
                print(f"Pajamos: {x.suma}")
            if isinstance(x, IslaiduIrasas):
                print(f"Islaidos: {x.suma}")


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
        print("Klaida, toks pasirinkimas neegzistuoja\nPasirinkite viena is duotu numeriu")
