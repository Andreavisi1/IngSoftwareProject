from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QMessageBox
from attivita.views.VistaListaAttivita import VistaListaAttivita
from listatesserati.controller.ControlloreListaTesserati import ControlloreListaTesserati
from listaeventi.views.VistaListaEventiTesserati import VistaListaEventiTesserati
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from statistiche.views.VistaSceltaStats import VistaSceltaStats
from tesserato.views.VistaDatiPersonaliTesserato import VistaDatiPersonaliTesserato

"""
La classe VistaHomeTesserato si occupa di mostrare a schermo al tesserato la home dove poter selezionare
la funzione da svolgere con il software.
"""

class VistaHomeTesserato(QWidget):

    def __init__(self, username, parent=None):
        super(VistaHomeTesserato, self).__init__(parent)
        self.username = username

        self.controller = ControlloreListaTesserati()

        #Impostazione generale della vista con loghi e bottoni
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_icon('logos/home logos/personal-data.png'), 0, 0)
        grid_layout.addWidget(self.get_icon('logos/home logos/calendar.png'), 0, 1)
        grid_layout.addWidget(self.get_icon('logos/home logos/analytics.png'), 0, 2)

        grid_layout.addWidget(self.get_generic_button("Sezione Dati Personali", self.show_personal_info), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Calendario Attività", self.go_lista_eventi), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Statistiche", self.go_statistiche), 1, 2)


        self.setLayout(grid_layout)
        self.setFixedSize(600, 200)
        self.setWindowTitle("A. S. D. Filottrano - Sezione Tesserato")
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

    #Metodo che si occupa di aprire la VistaListaEventiTesserati
    def go_lista_eventi(self):
        tesserato_selezionato = self.controller.get_tesserato_by_username(self.username)
        self.vista_lista_eventi = VistaListaEventiTesserati(tesserato_selezionato)
        self.vista_lista_eventi.show()

    #Metodo che si occupa di aprire la VistaSceltaStats
    def go_statistiche(self):
        self.vista_statistiche = VistaSceltaStats()
        self.vista_statistiche.show()

       # Metodo che mostra a schermo le informazioni del tesserato selezionato
    def show_personal_info(self):
        tesserato_selezionato = self.controller.get_tesserato_by_username(self.username)
        self.vista_tesserato = VistaDatiPersonaliTesserato(tesserato_selezionato)
        self.vista_tesserato.show()