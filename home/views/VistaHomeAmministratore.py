from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QMainWindow
from carrello.views.VistaListaCarrello import VistaListaCarrello
from listatesserati.views.VistaListaTesserati import VistaListaTesserati
from listaprodotti.views.VistaListaProdotti import VistaListaProdotti
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from statistiche.views.VistaSceltaStats import VistaSceltaStats

"""
La classe VistaHomeAmministratore si occupa di mostrare a schermo all'amministratore la home dove poter selezionare
la funzione da svolgere con il software.
"""


class VistaHomeAmministratore(QWidget):

    def __init__(self, parent=None):
        super(VistaHomeAmministratore, self).__init__(parent)

        #Impostazione generale della vista con loghi e bottoni
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_icon('logos/home logos/personal-data.png'), 0, 0)
        grid_layout.addWidget(self.get_icon('logos/home logos/team.png'), 0, 1)
        grid_layout.addWidget(self.get_icon('logos/home logos/calendar.png'), 0, 2)
        grid_layout.addWidget(self.get_icon('logos/home logos/analytics.png'), 0, 3)

        grid_layout.addWidget(self.get_generic_button("Sezione Dati Personali", self.go_lista_prodotti), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Tesserati", self.go_lista_tesserati), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Calendario Eventi", self.go_carrello), 1, 2)
        grid_layout.addWidget(self.get_generic_button("Statistiche", self.go_statistiche), 1, 3)

        self.setLayout(grid_layout)
        self.setFixedSize(800, 200)
        self.setWindowTitle("A. S. D. Filottrano - Sezione Amministratore")
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))


    #Questa funzione restituisce un bottone generico dato il titolo
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setFixedWidth(170)
        button.clicked.connect(on_click)
        return button

    #Questa funzione restituisce un logo dato il path
    def get_icon(self, path):
        label_logo = QLabel(self)
        pixmap = QPixmap(path)
        pixmap = pixmap.scaledToWidth(120)
        pixmap = pixmap.scaledToHeight(120)
        label_logo.setPixmap(pixmap)
        label_logo.setFixedSize(150, 120)
        label_logo.setAlignment(Qt.AlignCenter)
        return label_logo

    #Metodo che si occupa di aprire la VistaListaProdotti
    def go_lista_prodotti(self):
        self.vista_lista_prodotti = VistaListaProdotti()
        self.vista_lista_prodotti.show()

    #Metodo che si occupa di aprire la VistaListaTesserati
    def go_lista_tesserati(self):
        self.vista_lista_tesserati = VistaListaTesserati()
        self.vista_lista_tesserati.show()

    #Metodo che si occupa di aprire la VistaListaCarrello
    def go_carrello(self):
        self.vistacarrello = VistaListaCarrello()
        self.vistacarrello.show()

    #Metodo che si occupa di aprire la VistaSceltaStats
    def go_statistiche(self):
        self.vista_statistiche = VistaSceltaStats()
        self.vista_statistiche.show()





