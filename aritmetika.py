def dalyba(a, b):
    try:
        rezultatas = a / b

    except ZeroDivisionError:
        logger.exception("Dalyba is nulio")
    else:
        return rezultatas

a = 20
b = 0

padalinom = dalyba(a, b)
logger.info(f"Dalyba: {a} / {b} = {padalinom}")