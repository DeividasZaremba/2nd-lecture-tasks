####
# 1 UZDUOTIS
class Sakinys:
    def __init__(self, tekstas="As 1 ejau i miska grybauti"):
        self.tekstas = tekstas

    def atbulai(self):
        return self.tekstas[::-1]

    def mazosios(self):
        return self.tekstas.lower()

    def didziosios(self):
        return self.tekstas.upper()

    def eiles_nr(self, zodzio_nr):
        grazinamas_zodis = self.tekstas.split()
        kk = grazinamas_zodis[zodzio_nr - 1]
        return kk

    def pakeistas(self, kuri_keiciam, i_ka_keiciam):
        return self.tekstas.replace(kuri_keiciam, i_ka_keiciam)

    def info(self):
        zodziu_kiekis = len(self.tekstas.split())
        skaiciai = sum(i.isnumeric() for i in self.tekstas)
        didziosios = sum(i.isupper() for i in self.tekstas)
        mazosios = sum(i.islower() for i in self.tekstas)
        print(f"Zodziu kiekis: {zodziu_kiekis}, Skaiciai: {skaiciai}, Didziosios: {didziosios}, Mazosios: {mazosios}")

a = Sakinys()

print(a.atbulai())
print(a.mazosios())
print(a.didziosios())
print(a.eiles_nr(3))
print(a.pakeistas("miska", "laukus"))
a.info()

# 2 UZDUOTIS
import datetime
import calendar

class Sukaktis:
    def __init__(self, metai=2000, menuo=12, diena=12, valandos=12, minutes=12):
        self.metai = metai
        self.menuo = menuo
        self.diena = diena
        self.valandos = valandos
        self.minutes = minutes
        self.data = datetime.datetime(metai, menuo, diena, valandos, minutes)
    def kiek(self):
        now = datetime.datetime.now()
        dif = now - self.data
        print(f'praejo metu: ', dif.days // 365)
        print(f'praejo menesiu: ', dif.days / 365 * 12)
        print(f'praejo savaiciu: ', dif.days / 7)
        print(f'praejo dienu: ', dif.days)
        print(f'praejo valandu: ', dif.total_seconds() / 3600)
        print(f'praejo minuciu: ', dif.total_seconds() / 60)
        print(f'praejo sekundziu: ', dif.total_seconds())

    def arkeliamieji(self):
        if calendar.isleap(self.metai):
            print("Keliamieji metai")

    def atimtidienas(self, dienos):
        return self.data - datetime.timedelta(days=dienos)

    def pridetdienas(self, dienos):
        return self.data + datetime.timedelta(days=dienos)

data1 = Sukaktis(2000, 1, 1, 12, 12)
data1.arkeliamieji()
data1.kiek()
print(data1.atimtidienas(5))
print(data1.pridetdienas(30))

