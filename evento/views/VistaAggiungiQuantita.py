from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpinBox, QPushButton, QMessageBox
from PyQt5 import QtGui

"""
La classe VistaInserisciEvento si occupa di mostrare all'utente il form per registrare i dati del nuovo evento
"""

class VistaAggiungiQuantita(QWidget):
    def __init__(self, evento, attivita, parent=None):
        super(VistaAggiungiQuantita, self).__init__(parent)
        self.evento = evento
        self.msg = QMessageBox()

        self.attivita = attivita
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        self.setWindowTitle("Aggiungi alle attivita")
        self.resize(300, 100)

        self.v_layout = QVBoxLayout()

        label = QLabel("Quantità da acquistare")
        self.v_layout.addWidget(label)

        self.spin = QSpinBox(self)
        self.spin.setGeometry(100, 100, 250, 40)
        self.spin.setRange(1, 99)
        self.spin.setSizeIncrement(1, 1)
        self.v_layout.addWidget(self.spin)

        #Bottone per per confermare il passaggio del evento dal magazzino al attivita
        btn_conferma = QPushButton("Conferma")
        self.v_layout.addWidget(btn_conferma)
        btn_conferma.clicked.connect(self.aggiungi_alle_attivita)
        self.setLayout(self.v_layout)
        self.close()
    """
    Metodo che aggiunge il evento al attivita.
    Al metodo verifica_quantita_evento viene passato il evento e la quantità, e se risulta True aggiunge
    il evento alle attivita.
    """
    def aggiungi_alle_attivita(self):
        if self.attivita.verifica_quantita_evento(self.evento, int(self.spin.text())) is True:
            self.attivita.aggiungi_alle_attivita(self.evento)
            self.attivita.save_data()
            self.close()
        else:
            self.msg.setText("ERRORE: la quantità selezionata non è presente in magazzino")
            self.msg.exec_()


















