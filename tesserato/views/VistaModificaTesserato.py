from datetime import datetime

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, \
    QSpinBox, QDateEdit
from PyQt5 import QtGui

"""
La classe VistaModificaTesserato apre una finestra a schermo in cui il presidente può modificare i dati di un tesserato
"""

class VistaModificaTesserato(QWidget):
    def __init__(self, tesserato, update, parent=None):
        super(VistaModificaTesserato, self).__init__(parent)
        self.tesserato = tesserato
        self.info = {}
        self.update = update
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        self.setWindowTitle('Modifica Dati Tesserato')
        self.v_layout = QVBoxLayout()
        self.resize(300, 200)

        self.get_form_entry("Nome")
        self.get_form_entry("Cognome")
        self.get_form_entry("Codice Fiscale")
        self.get_form_entry("Email")
        self.get_form_entry("Telefono")
        self.get_form_entry("Luogo di nascita")
        self.get_spin_box("Età")
        self.get_form_entry("Password")
        self.get_spin_box("Inizio validità certificato")
        self.get_spin_box("Scadenza validità certificato")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Bottone per confermare i cambiamenti
        btn_conferma = QPushButton("Conferma")
        self.v_layout.addWidget(btn_conferma)
        btn_conferma.clicked.connect(self.modifica_tesserato)
        self.setLayout(self.v_layout)

    #Metodo per titolare i parametri da inserire
    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        if tipo == "Nome":
            current_text_edit.setText(self.tesserato.nome)
        if tipo == "Cognome":
            current_text_edit.setText(self.tesserato.cognome)
        if tipo == "Codice Fiscale":
            current_text_edit.setText(self.tesserato.cf)
        if tipo == "Email":
            current_text_edit.setText(self.tesserato.email)
        if tipo == "Telefono":
            current_text_edit.setText(self.tesserato.telefono)
            current_text_edit.setValidator(QtGui.QIntValidator(0, 1000000000))
        if tipo == "Luogo di nascita":
            current_text_edit.setText(self.tesserato.luogo_nascita)
        if tipo == "Password":
            current_text_edit.setText(self.tesserato.password)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

# Metodo che crea uno spinbox per poter inserire correttamente l'età e i dati del certificato
    def get_spin_box(self, tipo):
        global current_text_edit
        self.v_layout.addWidget(QLabel(tipo))
        if tipo == "Età":
            current_text_edit = QSpinBox()
            current_text_edit.setValue(int(self.tesserato.eta))
            current_text_edit.setRange(0, 113)
        if tipo == "Inizio validità certificato" or tipo == "Scadenza validità certificato":
            current_text_edit = QDateEdit()
            current_text_edit.setDate(datetime.now().date())
            current_text_edit.setCalendarPopup(True)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    #Metodo per modificare i parametri di prezzo e quantità del evento
    def modifica_tesserato(self):

        nuovonome = self.info["Nome"].text()
        nuovocognome = self.info["Cognome"].text()
        nuovoid = nuovonome + nuovocognome
        nuovocf = self.info["Codice Fiscale"].text()
        nuovaemail = self.info["Email"].text()
        nuovotelefono = self.info["Telefono"].text()
        nuovoluogonascita = self.info["Luogo di nascita"].text()
        nuovaeta = self.info["Età"].text()
        nuovapassword = self.info["Password"].text()
        nuovoiniziocertificato = self.info["Inizio validità certificato"].text()
        nuovascadenzacertificato = self.info["Scadenza validità certificato"].text()

        if nuovonome == "" or nuovocognome == "" or nuovocf == "" or nuovaemail == "" or nuovotelefono == "" or nuovoluogonascita == "" or nuovaeta == "" or nuovapassword == "" or nuovoiniziocertificato == "" or nuovascadenzacertificato == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.tesserato.id = nuovoid
            self.tesserato.nome = nuovonome
            self.tesserato.cognome = nuovocognome
            self.tesserato.cf = nuovocf
            self.tesserato.email = nuovaemail
            self.tesserato.telefono = nuovotelefono
            self.tesserato.luogo_nascita = nuovoluogonascita
            self.tesserato.eta = nuovaeta
            self.tesserato.password = nuovapassword
            self.tesserato.inizio_certificato = nuovoiniziocertificato
            self.tesserato.scadenza_certificato = nuovascadenzacertificato
            self.update()
            self.close()