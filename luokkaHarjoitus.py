# Kokeillaan luokkia ja olioita

# LUOKKIA

# Yliluokka (Parent class, Mother class, Superclass)
class Henkilo:
    def __init__(self, etunimi, sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi

# Aliluokka (Child class, Daughter class, Subclass) perii (inherit) Henkilo-luokan
class Opiskelija(Henkilo):
    def __init__(self, etunimi, sukunimi, ryhma):
        super().__init__(etunimi, sukunimi)
        self.ryhma = ryhma

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

    # Luodaan olio opiskelija
    opiskelija = Opiskelija('Jakke', 'Jäynä', 'Tivi20oA')

    # Luodaan olio Oppivelvollinen-luokasta
    oppivelvollinen = Oppivelvollinen('Jonne', 'Jantteri', 'Tivi24A', '2027-05-20')

    print('Koulun rehtorina toimii', rehtori)

    print('Koulun rehtorina toimii', rehtori.etunimi, rehtori.sukunimi)