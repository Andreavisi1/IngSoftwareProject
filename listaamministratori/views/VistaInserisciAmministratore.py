from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, \
    QComboBox
from amministratore.model.Amministratore import Amministratore
from PyQt5 import QtGui

"""
La classe VistaInserisciAmministratore si occupa di mostrare all'utente il form per registrare i dati dell'amministratore
"""

class VistaInserisciAmministratore(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciAmministratore, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        self.resize(300, 200)

        self.v_layout = QVBoxLayout()

        self.get_form_entry("Nome")
        self.get_form_entry("Cognome")
        self.get_form_entry("Ruolo")

        self.get_form_entry("Codice Fiscale")
        self.get_form_entry("Indirizzo")
        self.get_form_entry("Email")
        self.get_form_entry("Telefono")
        self.get_form_entry("Età")
        self.get_form_entry("Password")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_amministratore)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Amministratore")

    #Metodo per titolare i parametri da inserire
    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        if tipo == "Telefono" or tipo == "Età":
            current_text_edit.setValidator(QtGui.QIntValidator(0, 1000000000))
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    #Metodo che genera un nuovo amministratore sfruttando le informazioni inserite dall'utente
    def add_amministratore(self):
        nome = self.info["Nome"].text()
        cognome = self.info["Cognome"].text()
        ruolo = self.info["Ruolo"].text()
        cf = self.info["Codice Fiscale"].text()
        indirizzo = self.info["Indirizzo"].text()
        email = self.info["Email"].text()
        telefono = self.info["Telefono"].text()
        eta = self.info["Età"].text()
        password = self.info["Password"].text()
        if nome == "" or cognome == "" or ruolo == "" or cf == "" or indirizzo == "" or email == "" or telefono == "" or eta == "" or password == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        else:
            prova = (nome+cognome).lower()
            self.controller.aggiungi_amministratore(Amministratore(prova.replace(" ", ""), nome, cognome, ruolo, cf, indirizzo, email, telefono, eta, password))
            self.callback()
            self.close()
