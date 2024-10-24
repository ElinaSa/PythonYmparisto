#  SOVELLUKSEN PÄÄOHJELMA
# ========================

# KIRJASTOT
# ---------

# MODUULIT
# --------

from avtools import sound2 # Äänimerkit ja äänitiedostot
from avtools import video2 # Videomoduuli
import identityCheck2

# ASETUKSET
# ---------

kameraIndeksi: int = 1 # Ensimmäinen kamera on aina 0

userGivenSsn = input('Syötä asiakkaan henkilötunnus: ')
ssnToCheck = identityCheck2.NationalSSN(userGivenSsn)
if ssnToCheck.isValidSsn() == True:
    dateOfBirth = ssnToCheck.getDateOfBirth()
    ssnToCheck.getGender()
    age = ssnToCheck.calculateAge()
    print('Syntymäaika:', ssnToCheck.dateOfBirth)
    print('Ikä:', age)
    print('Sukupuoli:', ssnToCheck.gender)

# TESTIT KOODAUKSEN AIKANA
# ========================

if __name__ == "__main__":
    pass