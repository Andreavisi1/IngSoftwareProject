from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, \
    QDoubleSpinBox, QSpinBox
from PyQt5 import QtGui, QtCore

"""
La classe VistaModificaEvento apre una finestra a schermo dove l'utente può cambiare i valori di prezzo e quantità
"""

class VistaModificaEvento(QWidget):
    def __init__(self, evento, update, parent=None):
        super(VistaModificaEvento, self).__init__(parent)
        self.evento = evento
        self.info = {}
        self.update = update
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        self.setWindowTitle('Modifica Evento')
        self.v_layout = QVBoxLayout()
        self.resize(300, 200)


        self.get_form_entry("Nuova Quantità")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Bottone per confermare i cambiamenti
        btn_conferma = QPushButton("Conferma")
        self.v_layout.addWidget(btn_conferma)
        btn_conferma.clicked.connect(self.modifica_evento)
        self.setLayout(self.v_layout)

    #Metodo per titolare i parametri da inserire
    def get_form_entry(self, tipo):
        global current_text_edit
        self.v_layout.addWidget(QLabel(tipo))
        if tipo == "Nuovo Prezzo":
            current_text_edit = QDoubleSpinBox()
            current_text_edit.setRange(0, 1000000)
        if tipo == "Nuova Quantità":
            current_text_edit = QSpinBox()
            current_text_edit.setRange(0, 100)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    #Metodo per modificare i parametri di prezzo e quantità del evento
    def modifica_evento(self):

        nuovaquantita = self.info["Nuova Quantità"].text()

        if nuovaquantita == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)

        else:
            self.evento.quantita_magazzino = nuovaquantita
            self.update()
            self.close()
