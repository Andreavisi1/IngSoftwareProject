from datetime import datetime

from PyQt5.QtCore import QDate
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, QSpinBox, QDateEdit, QComboBox

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
        self.get_spin_box("Età")
        self.get_form_entry("Password")

        self.v_layout.addWidget(QLabel("Categoria"))
        self.combo_categoria = QComboBox()
        self.combo_categoria_model = QStandardItemModel(self.combo_categoria)
        self.add_combobox_item("Piccoli amici")
        self.add_combobox_item("Pulcini")
        self.add_combobox_item("Esordienti")
        self.add_combobox_item("Allievi")
        self.add_combobox_item("Juniores")
        self.add_combobox_item("Promesse")
        self.add_combobox_item("Seniores")
        self.combo_categoria.setModel(self.combo_categoria_model)
        self.v_layout.addWidget(self.combo_categoria)

        self.get_spin_box("Inizio validità certificato")
        self.get_spin_box("Scadenza validità certificato")

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
        if tipo == "Telefono":
            current_text_edit.setValidator(QtGui.QIntValidator(0, 1000000000))
        if tipo == "Password":
            current_text_edit.setEchoMode(QLineEdit.Password)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    # Metodo che crea uno spinbox per poter inserire correttamente l'età e i dati del certificato
    def get_spin_box(self, tipo):
        global current_text_edit
        self.v_layout.addWidget(QLabel(tipo))
        if tipo == "Età":
            current_text_edit = QSpinBox()
            current_text_edit.setRange(0, 113)
            current_text_edit.setValue(18)
        if tipo == "Inizio validità certificato" or tipo == "Scadenza validità certificato":
            current_text_edit = QDateEdit()
            current_text_edit.setDisplayFormat("dd/MM/yyyy")
            current_text_edit.setDate(datetime.now().date())
            current_text_edit.setCalendarPopup(True)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    # Metodo che crea un menù a tendina dove selezionare la tipologia dell'evento da inserire
    def add_combobox_item(self, tipo):
        item = QStandardItem()
        item.setText(tipo)
        item.setEditable(False)
        self.combo_categoria_model.appendRow(item)

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
        categoria = self.combo_categoria.currentText()
        inizio_certificato = self.info["Inizio validità certificato"].text()
        scadenza_certificato = self.info["Scadenza validità certificato"].text()
        if nome == "" or cognome == "" or cf == "" or email == "" or telefono == "" or luogo_nascita == "" or eta == "" or password == "" or categoria == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        elif QDate.fromString(inizio_certificato, "dd/MM/yyyy") > QDate.fromString(scadenza_certificato, "dd/MM/yyyy"):
            QMessageBox.critical(self, 'Errore', 'Il certificato è scaduto ancor prima di iniziare?', QMessageBox.Ok, QMessageBox.Ok)
        else:
            prova = (nome+cognome).lower()
            self.controller.aggiungi_tesserato(Tesserato(prova.replace(" ", ""), nome, cognome, cf, email, telefono, luogo_nascita, eta, password, categoria, inizio_certificato, scadenza_certificato))
            self.callback()
            self.close()
