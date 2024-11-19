# MALLIPOHJA QT-SOVELLUSTEN RAKENTAMISEEN
# =======================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------

# Järjestelmäkomentojen kirjasto
import sys

# Qt:n kirjastot
import PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QApplication  # Käyttöliittymän elementit (kaikki), korvaa listalla
from PyQt6.uic import Loader

# LUOKKAMÄÄRITYKSET
# -----------------

# Pääikkunan luokka, joka perii QMainWindow-luokan
class MainWindow(QMainWindow):

    # Kostruktori
    def __init__(self):
        QMainWindow.__init__(self)

        # Ladataan käyttöliittymätiedosto
        Loader.__loader__('mainWindow.ui', self)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec())

