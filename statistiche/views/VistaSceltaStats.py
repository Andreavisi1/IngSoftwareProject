import datetime

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PyQt5 import QtGui


from statistiche.views.VistaStats import VistaStats


class VistaSceltaStats(QWidget):
    def __init__(self):
        super(VistaSceltaStats, self).__init__()

        #Inizializzate tre variabili per ospitare la data di oggi, una settimana fa e un mese fa.
        self.today = datetime.date.today()
        self.week = datetime.date.today() - datetime.timedelta(weeks = 1)
        self.month = datetime.date.today() - datetime.timedelta(days = 30)

        grid_layout = QGridLayout()

        #Vengono aggiungi al layout tre bottoni diversi in base al periodo di cui si vogliono visualizzare le statistiche.
        grid_layout.addWidget(self.get_generic_button("Vendite Giornaliere", self.go_daily_stats), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Vendite Settimanali", self.go_weekly_stats), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Vendite Mensili", self.go_monthly_stats), 1, 2)

        self.setLayout(grid_layout)
        self.setFixedSize(400, 100)
        self.setWindowTitle("Vincere non è importante... È l'unica cosa che conta!")
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        #Questa funzione restituisce un bottone generico dato il titolo
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

        #Porta l' utente a visualizzare le statistiche giornaliere
    def go_daily_stats(self):
        self.vista_statistiche = VistaStats(self.today)
        self.vista_statistiche.show()

        #Porta l' utente a visualizzare le statistiche settimanali
    def go_weekly_stats(self):
        self.vista_statistiche = VistaStats(self.week)
        self.vista_statistiche.show()

        #Porta l' utente a visualizzare le statistiche mensili
    def go_monthly_stats(self):
        self.vista_statistiche = VistaStats(self.month)
        self.vista_statistiche.show()