from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from tesserato.model.Tesserato import Tesserato
from PyQt5 import QtGui


"""
La classe VistaInserisciTesserato si occupa di mostrare all'utente il form per registrare i dati del tesserato
"""

class VistaInserisciTesserato(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciTesserato, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        self.v_layout = QVBoxLayout()
        self.resize(300, 200)

        self.get_form_entry("Nome")
        self.get_form_entry("Cognome")
        self.get_form_entry("Codice fiscale")
        self.get_form_entry("Email")
        self.get_form_entry("Telefono")
        self.get_form_entry("Luogo di nascita")
        self.get_form_entry("Età")
        self.get_form_entry("Password")

        self.get_form_entry("Inizio validità certificato")
        self.get_form_entry("Scadenza validità certificato")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_tesserato)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Tesserato")

    #Metodo per titolare i parametri da inserire
    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        if tipo == "Telefono" or tipo == "Età":
            current_text_edit.setValidator(QtGui.QIntValidator(0, 1000000000))
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    #Metodo che genera un nuovo tesserato sfruttando le informazioni inserite dall'utente
    def add_tesserato(self):
        nome = self.info["Nome"].text()
        cognome = self.info["Cognome"].text()
        cf = self.info["Codice fiscale"].text()
        email = self.info["Email"].text()
        telefono = self.info["Telefono"].text()
        luogo_nascita = self.info["Luogo di nascita"].text()
        eta = self.info["Età"].text()
        password = self.info["Password"].text()
        inizio_certificato = self.info["Inizio validità certificato"].text()
        scadenza_certificato = self.info["Scadenza validità certificato"].text()
        if nome == "" or cognome == "" or cf == "" or email == "" or telefono == "" or luogo_nascita == "" or eta == "" or password == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        else:
            prova = (nome+cognome).lower()
            self.controller.aggiungi_tesserato(Tesserato(prova.replace(" ", ""), nome, cognome, cf, email, telefono, luogo_nascita, eta, password, inizio_certificato, scadenza_certificato))
            self.callback()
            self.close()
