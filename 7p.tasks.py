import datetime

now = datetime.datetime.now()
nowstr = datetime.datetime.strftime(now, "%Y-%m-%d %H:%M:%S")

with open('Textukas.txt', 'r+') as f:
    print(f.read())
    f.write(nowstr + '\n')

with open('Textukas.txt', 'r', encoding='utf-8') as f:
    contentlistas = f.readlines()

sk = 1
new_lines = []

for line in contentlistas:
    modified_line = f'{sk} {line}'
    new_lines.append(modified_line)
    sk += 1

with open('Textukas.txt', 'r+', encoding='utf-8') as f:
    f.writelines(new_lines)

with open('Textukas.txt', 'r') as f:
    original_text = f.read()
    modified_text = original_text.replace("Beatiful is better than ugly.", "Gražu yra geriau nei bjauru.")
    with open('Textukas.txt', 'w', encoding='utf-8') as f:
        f.write(modified_text)


def info(tekstas):
    zodziu_kiekis = len(tekstas.split())
    skaiciai = sum(i.isnumeric() for i in tekstas)
    didziosios = sum(i.isupper() for i in tekstas)
    mazosios = sum(i.islower() for i in tekstas)
    print(f"Zodziu kiekis: {zodziu_kiekis}, Skaiciai: {skaiciai}, Didziosios: {didziosios}, Mazosios: {mazosios}")


with open('Textukas.txt', 'r') as f:
    info(f.read())


### 2 uzduotis
filename = input("What is the name of the file?: ")
filename += '.txt'
lines = []

while True:
    line = input("Enter a line of text: ")
    if line:
        lines.append(line + '\n')
    else:
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        break


### 3 uzduotis
from datetime import datetime
import os

os.chdir('C:\\Users\\teh\\Desktop\\')

# with open('tekstas1.txt', 'w') as f:
#     f.write(str(datetime.now()))

stats = os.stat('tekstas1.txt')
size = stats.st_size
createtime = datetime.fromtimestamp(stats.st_mtime)

print(size)
print(createtime)
import os
import pickle


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
        if os.path.exists('biudzetas.pkl'):
            with open('biudzetas.pkl', 'rb') as pkl:
                self.biudzetas = pickle.load(pkl)
        else:
            self.biudzetas = []

    def irasyti_biudzeta(self):
        with open('biudzetas.pkl', 'wb') as f:
            pickle.dump(self.biudzetas, f)

    def prideti_pajamas(self, suma, siuntejas, papildoma_info):
        self.biudzetas.append(PajamuIrasas(suma, siuntejas, papildoma_info))
        self.irasyti_biudzeta()

    def prideti_islaidas(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        self.biudzetas.append(IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga))
        self.irasyti_biudzeta()

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
                print(
                    f"Islaidos: {x.suma}")


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
