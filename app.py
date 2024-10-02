#  SOVELLUKSEN PÄÄOHJELMA
# ========================

# KIRJASTOT
# ---------

# MODUULIT
# --------

import sound2 # Äänimerkit ja äänitiedostot
import video2 # Videomoduuli

# ASETUKSET
# ---------

kameraIndeksi: int = 1 # Ensimmäinen kamera on aina 0

# Käynnistetään videokuva ja ilmoitetaan sen käynnistymisestä äänimerkillä
sound2.parametricBeep(400,330)
sound2.playWav('Alkaa.WAV')

# TESTIT KOODAUKSEN AIKANA
# ========================

if __name__ == "__main__":
    pass