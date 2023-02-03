from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel

from amministratore.views.VistaDatiPersonaliPresidente import VistaDatiPersonaliPresidente
from listatesserati.views.VistaListaTesserati import VistaListaTesserati
from listaamministratori.views.VistaListaAmministratori import VistaListaAmministratori
from listaeventi.views.VistaListaEventi import VistaListaEventi
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

from statistiche.views.VistaStats import VistaStats

"""
La classe VistaHomePresidente si occupa di mostrare a schermo al presidente la home dove poter selezionare
la funzione da svolgere con il software.
"""

class VistaHomePresidente(QWidget):

    def __init__(self, parent=None):
        super(VistaHomePresidente, self).__init__(parent)

        #Impostazione generale della vista con loghi e bottoni
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_icon('logos/home logos/personal-data.png'), 0, 0)
        grid_layout.addWidget(self.get_icon('logos/home logos/team.png'), 0, 1)
        grid_layout.addWidget(self.get_icon('logos/home logos/management.png'), 0, 2)
        grid_layout.addWidget(self.get_icon('logos/home logos/calendar.png'), 0, 3)
        grid_layout.addWidget(self.get_icon('logos/home logos/analytics.png'), 0, 4)

        grid_layout.addWidget(self.get_generic_button("Sezione Dati Personali", self.show_personal_info), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Gestione Tesserati", self.go_lista_tesserati), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Gestione Amministratori", self.go_lista_amministratori), 1, 2)
        grid_layout.addWidget(self.get_generic_button("Calendario Attività", self.go_lista_eventi), 1, 3)
        grid_layout.addWidget(self.get_generic_button("Statistiche", self.go_statistiche), 1, 4)

        self.setLayout(grid_layout)
        self.setFixedSize(1000, 200)
        self.setWindowTitle("A. S. D. Filottrano - Sezione Presidente")
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

    #Metodo che si occupa di aprire la VistaListaEventi
    def go_lista_eventi(self):
        self.vista_lista_eventi = VistaListaEventi()
        self.vista_lista_eventi.show()

    #Metodo che si occupa di aprire la VistaListaTesserati
    def go_lista_tesserati(self):
        self.vista_lista_tesserati = VistaListaTesserati()
        self.vista_lista_tesserati.show()

    #Metodo che si occupa di aprire la VistaListaAmministratori
    def go_lista_amministratori(self):
        self.vista_lista_amministratori = VistaListaAmministratori()
        self.vista_lista_amministratori.show()

    def show_personal_info(self):
        self.vista_presidente= VistaDatiPersonaliPresidente()
        self.vista_presidente.show()

    #Metodo che si occupa di aprire la VistaSceltaStats
    def go_statistiche(self):
        self.vista_statistiche = VistaStats()
        self.vista_statistiche.show()

