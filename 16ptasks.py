import requests
from bs4 import BeautifulSoup

html = requests.get("https://orai.15min.lt/prognozes").text
soup = BeautifulSoup(html, 'html.parser')

prognozes = soup.find_all('div', class_='item full clearfix')
city_and_temp = {}

for card in prognozes:
    miestas = card.find('a', class_='city').text.strip()
    miestas_temp = card.find('div', class_='temperature alert-hot').text.strip()
    city_and_temp[miestas] = miestas_temp

a = input("""Yra sie miestai: Vilnius / Kaunas / Klaipėda / Šiauliai / Panevėžys / Alytus / Marijampolė / Mažeikiai / Utena
Iveskite miesta kurio dabartine prognoze norite matyti: """)
print(f'Mieste "{a}" siuo metu yra {city_and_temp[a]} temperatura')