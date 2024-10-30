# MODUULI  VIIVAKOODIEN TUOTTAMISEEN
# ==================================

# KIRJASTOT
# ---------

# ASETUKSET
# ---------

# FUNKTIOT
# --------

def barCodeValue(character: str) -> int:
    """Calculates a value of character used in Code128B barcode generation

    Args:
        character (str): a single character to convert 

    Returns:
        int: Code128B value for calculating the checksum
    """
    asciiValue = ord(character)
    code128BValue = asciiValue -32
    return code128BValue

def calculateCode128BChecksum(text: str) -> int:
    """Calculates a checksum for a given string

    Args:
        text (str): text string to use in a barcode

    Returns:
        int: Modulo 103 checksum of weighted values
    """
    text = text.strip()
    numberOfLetters = len(text)
    weightedSum = 0
    for number in range(numberOfLetters):
        letter = text[number]
        code128BValue = barCodeValue(letter)
        weightedValue = code128BValue * (number + 1) 
        weightedSum = weightedSum + weightedValue
    weightedSum = weightedSum + 104
    code128BChecksum = weightedSum % 103
    return code128BChecksum

# TODO: Tee tämä funktio loppuun ja testaa sitä Notepadissa
def createCode128B(text : str) -> str:
    """Creates a compelete code128B barcode to be printed using Libre Code 128 font

    Args:
        text (str): The text for a barcode without checksum

    Returns:
        str: String containing start, barcode, checksum and stop symbols
    """
    code128BarcodeString = ''
    return code128BarcodeString

if __name__ == "__main__":
    testString = '128B'
    print('painotetut arvot yhteensä:',calculateCode128BChecksum(testString))
    
    # Putsattu pois aiempi kokeilu if name on mainista sotkemasta merkitsemällä kommentiksi
    """ letter = 'C'
    letter_asciikoodi = ord(letter)

    print('Kirjaimen', letter, 'ASCII-koodi on', letter_asciikoodi)

    barcode_value = letter_asciikoodi -32

    print('Viivakoodissa sen arvo on', barcode_value)
  
    print('Kun viivakoodia tulostetaan merkki on ', letter) """ 