import datetime
import time

## 1 UZDUOTIS
now = datetime.datetime.now()
print(now)
print(now - datetime.timedelta(days = 5))

try:
    date1 = input("Iveskite pradzios data formatu YYYY-MM-dd HH:MM:SS: ")
    data1 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    print(data1)
    date2 = input("Iveskite pabaigos data formatu YYYY-MM-dd HH:MM:SS: ")
    data2 = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    print(data2)
    skirtumas = (data1 - data2)
    print(skirtumas.total_seconds())
except:
    print("Netinkamas datos formatas")

## 2 UZDUOTIS
now = datetime.datetime.now()
print(now)
print(now - datetime.timedelta(days = 5))
print(now + datetime.timedelta(hours = 8))
print(now.strftime("%Y %m %d, %H:%M:%S"))

## 3 UZDUOTIS
bd = input("Iveskite savo gimtadieni ir laika formatu YYYY-MM-DD HH:SS : ")
try:
    data = datetime.datetime.strptime(bd, "%Y-%m-%d %H:%M")
    dif = datetime.datetime.now() - data
    print(str(round(dif.days/365)) + " metai")
    print(str(round(dif.days/12)) + " menesiai")
    print(str(round(dif.days)) + " dienos")
    print(str(round(dif.days*24)) + " valandos")
    print(str(round(dif.days*24*60)) + " minutes")
    print(str(round(dif.days*24*60*60)) + " sekundes")
except ValueError:
    print("Netinkamas datos formatas")

## 4 UZDUOTIS
# pataisytos 1-3 kad butu try/except

## 5 UZDUOTIS
while True:
    try:
        a = float(input("Iveskite laika sekundemis: "))
        laikas = datetime.timedelta(seconds=a)
        break
    except ValueError:
        print("Netinkamas formatas, pakartokite teisingu formatu")

z = input("Iveskite zodi: ")
while True:
    print(z)
    time.sleep(a)
