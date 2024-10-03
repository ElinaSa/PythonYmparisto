# MODUULI OPISKELIJANUMERON JA HENKILÖTUNNUKSEN TARKISTUKSEEN
# ===========================================================

"""Module makes sanity checks for Raseko student id and the Finnish Social Security Number
    """

# KIRJASTOT JA MODUULIT
# ---------------------

# FUNKTIOT
# --------

# Opiskelijatunnuksen oikea muoto
def opiskelijanumeroOk(opiskelijanumero: str) -> bool:
    """Checks if student number is 5 or 6 digits and does not contain any characters other than numerics

    Args:
        opiskelijanumero (str): Raseko's student id

    Returns:
        bool: True if correct otherwise False
    """
    result: bool = False
    pituus = len(opiskelijanumero)
    if pituus == 5 or pituus == 6:
        if opiskelijanumero.isdigit():
            result = True   
    return result 

# TODO: Tee testit HeTu:a varten ja vasta sitten kirjoita koodi

# Henkilötunnus esimerkki 130728-478N Testataan
# 1. Pituus
# 2. Syntymäaikaosan oikeellisuus
# 3. Vuosisatakoodit +, - ja A
# 4. Modulo 31 tarkistus

# Lopullisena Tavoitteena on funktio, joka tarkistaa henkilötunnuksen oikeellisuuden ja palauttaa virhekoodin ja
# virheilmoituksen, joka kertoo mikä vika HeTus:ssa on. Esim 0, OK tai 1, tunnus liian lyhyt, tai 2, tunnus liian pitkä jne.

def checkHeTu(hetu):

    # Oletustulos 0 OK jos kaikki on kunnossa
    result = (0, 'OK')

    # Lasketaan HeTu-parametrin pituus
    length = len(hetu)

    # Jos pituus on oikea tehdään eri osat
    if length== 11:
        dayPart = hetu[0:2]
        monthPart = hetu[2:4]
        yearPart = hetu[4:6]
        centuryPart = hetu[6:7]
        numberPart = hetu[7:10]
        checkSum = hetu[10]

    if length < 11:
        result = (1, 'Henkilötunnus liian lyhyt')

    if length > 11:
        result = (2, 'Henkilötunnus liian pitkä')

    # Tarkistetaan päiväosan oikeellisuus
    return result

if __name__ =="__main__":
    hetu = '130728-478N'
    paivat = hetu[0:2]
    kuukaudet = hetu[2:4]
    print(paivat)
    print(kuukaudet)