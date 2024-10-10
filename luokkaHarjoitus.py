# Kokeillaan luokkia ja olioita

# LUOKKIA

# Yliluokka (Parent class, Mother class, Superclass)
class Henkilo:

    # Konstruktori (metodi), jonka avulla luodaan uusi Henkilö-olio
    # Oliota luotaessa etunimi ja sukunimi ovat pakollisia tietoja
    def __init__(self, etunimi, sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi

        # Oliolla on myös muita ominaisuuksia, joita ei määritellä olion luomisen yhteydessä
        self.ika = 0 # Oletusikä 0
        self.kaupunki = '' # Asuinkaupunki tyhjä
        self.harrastukset = [] # Harrastukset tyhjä lista

# Aliluokka (Child class, Daughter class, Subclass) perii (inherit) Henkilo-luokan
class Opiskelija(Henkilo):

    # Oliota luotaessa pakollisia ovat etunimi ja sukunimi (koska pakollisia)
    # yliluokassa Henkilö sekä ryhmä
    
    def __init__(self, etunimi, sukunimi, ryhma): # Metodi joka muodostaa opiskelija-olion
        super().__init__(etunimi, sukunimi) # Kertoo, että yliluokassa on määritelty etunimen ja sukunimen käsittely
        self.ryhma = ryhma # Tämän parametri käsittelyä ei ole kerrottu yliluokassa

# Aliluokka (Child class, Daughter class, Subclass) perii (inherit) Henkilo-luokan 
class Opettaja(Henkilo):
    def __init__(self, etunimi, sukunimi, aine):
        super().__init__(etunimi, sukunimi)
        self.aine = aine

# Aliluokka perii Opiskelija-luokan ominaisuuksia
class Oppivelvollinen(Opiskelija):
    def __init__(self, etunimi, sukunimi, ryhma, paattyy):
        super().__init__(etunimi, sukunimi, ryhma)
        self.paattyy = paattyy

if __name__ == "__main__":

    # Johdetaan (instantiate) luokasta Henkilö olio rehtori
    rehtori = Henkilo('Reijo', 'Rantanen')
    rehtori.harrastukset = ['sulkapallo', 'rullaluistelu']

    # Luodaan olio opiskelija
    opiskelija = Opiskelija('Jakke', 'Jäynä', 'Tivi20oA')
    opiskelija.harrastukset = ['kokkaaminen', 'punttisali']

    # Luodaan olio Oppivelvollinen-luokasta
    oppivelvollinen = Oppivelvollinen('Jonne', 'Jantteri', 'Tivi24A', '2027-05-20')
    oppivelvollinen.harrastukset = ['pelaaminen', 'velttoilu']

    print('Koulun rehtorina toimii', rehtori)

    print('Koulun rehtorina toimii', rehtori.etunimi, rehtori.sukunimi)

    print('Rehtori harrastaa', rehtori.harrastukset)

    print('Jakke Jäynä harrastaa', opiskelija.harrastukset)

    print('Jonne harrastaa', oppivelvollinen.harrastukset)