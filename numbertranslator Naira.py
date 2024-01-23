# -*- coding: iso-8859-15 -*-

# Scrivere un algoritmo che, dato un numero,
# ne mostri la sua rappresentazione a lettere in italiano
# Esempio:
#   input: 1234 -> output: milleduecentotrentaquattro
#
# Come funziona?
# Per i primi venti numeri, non c'� altra strada che quella
# di prevedere una traduzione semplice attraverso una tabella:
# 0 -> zero, 1 -> uno, 2 -> due, ..., 19 -> diciannove

def translate_to_20(n):
    if n > 19:
        return "Out of range"

    NUMBERS = ["","uno", "due", "tre", "quattro", "cinque", "sei", "sette",
               "otto", "nove", "dieci", "undici", "dodici", "tredici",
               "quattordici", "quindici", "sedici", "diciassette",
               "diciotto", "diciannove"]
    return NUMBERS[n]

# dal 20, fino al 100 (escluso), ho la possibilit� di prevedere
# una "traduzione" della decina e demandare la "traduzione"
# dell'unit� alla funzione che traduce fino a 20
# 25 -> decina = 2, unit� = 5


def translate_to_100(n):
    if n < 20:
        return translate_to_20(n)
    if n > 100:
        return "Out of range"
    DECADES = ["venti", "trenta", "quaranta", "cinquanta", "sessanta",
               "settanta", "ottanta", "novanta"]
    decade =  n // 10 # la decina da n
    unit = n % 10 # l'unit� di n

    return DECADES[decade-2] + translate_to_20(unit)


#Devo fare il continuo per arrivare a 1000, ho la possibilita di prevedere una "traduzione" della centinaia
# e demandare la "traduzione" dell'unità alla unzione che traduce fino a 100
# 125 -> 1 -> centinaia 2-> decina 5-> unità
    
def translate_to_1000(n):
    if n < 20:
        return translate_to_20(n)
    if n < 100:
        return translate_to_100(n)
    HUNDREDS = ["", "cento", "duecento", "trecento", "quattrocento", "cinquecento",
                "seicento", "settecento", "ottocento", "novecento"]
    hundred = n // 100
    rest = n % 100
    if hundred == 0:
        return translate_to_100(rest)
    elif rest == 0:
        return HUNDREDS[hundred]
    else:
        return HUNDREDS[hundred] + translate_to_100(rest)

def translate_number(n):
    if n < 1 or n > 1000:
        return "Out of range"
    return translate_to_1000(n)

for x in range(1, 1001):
    print(translate_number(x))

