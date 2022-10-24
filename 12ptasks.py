import logging

logger = logging.getLogger('LOGAS')
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logeris.log', encoding='UTF-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
stream_handler.setFormatter(formatter)

def suma(*args):
    rezultatas = 0
    for i in args:
        rezultatas += i
    logger.info(f'Skaiciu {args} suma lygi: {rezultatas}')
    return rezultatas


print(suma(10, 3, 4))


import math
def saknis(arg):
    rez = "Nieko neapskaiciavo"
    try:
        rez = math.sqrt(arg)
        logger.info(f'Saknis is skaiciaus {arg} yra {rez}')
    except TypeError:
        logger.exception("Paduotas ne skaicius")
    return rez


print(saknis(0))


def sakinio_ilgis(arg):
    ilgis = len(arg)
    logger.info(f'Duoto sakinio ({arg}) ilgis yra is {ilgis} simboliu.')
    return ilgis


print(sakinio_ilgis("Siandien lija bet ir sviecia saule"))


def dalyba(x, y):
    rez = "Nieko neapskaiciavo"
    try:
        rez = x / y
    except ZeroDivisionError:
        logger.exception("Dalyba is nulio negalima")
    else:
        logger.info(f'Daliname {x} is {y}, rezultatas: {rez}')
        return print(rez)
    return rez


dalyba(4, 1)
