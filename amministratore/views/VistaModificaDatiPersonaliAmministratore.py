from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, QComboBox, QSpinBox
from PyQt5 import QtGui

from listaamministratori.controller.ControlloreListaAmministratori import ControlloreListaAmministratori

"""
La classe VistaModificaDatiPersonaliAmministratore apre una finestra a schermo in cui un amministratore puo modificare i propri dati personali
"""

class VistaModificaDatiPersonaliAmministratore(QWidget):
    def __init__(self, amministratore, update, parent=None):

        super(VistaModificaDatiPersonaliAmministratore, self).__init__(parent)
        self.amministratore = amministratore
        self.info = {}
        self.update = update

        self.controller = ControlloreListaAmministratori()

        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        self.setWindowTitle('Modifica Dati Amministratore')
        self.v_layout = QVBoxLayout()
        self.resize(300, 200)

        self.v_layout.addWidget(QLabel("Ruolo"))
        self.combo_ruolo = QComboBox()
        self.combo_ruolo_model = QStandardItemModel(self.combo_ruolo)
        self.add_combobox_item("Dirigente")
        self.add_combobox_item("Allenatore")
        self.add_combobox_item("Segretario/a")
        self.combo_ruolo.setModel(self.combo_ruolo_model)
        self.combo_ruolo.setCurrentText(self.amministratore.ruolo)
        self.v_layout.addWidget(self.combo_ruolo)

        self.get_form_entry("Codice Fiscale")
        self.get_form_entry("Indirizzo")
        self.get_form_entry("Email")
        self.get_form_entry("Telefono")
        self.get_spin_box("Età")
        self.get_form_entry("Password")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Bottone per confermare i cambiamenti
        btn_conferma = QPushButton("Conferma")
        self.v_layout.addWidget(btn_conferma)
        btn_conferma.clicked.connect(self.modifica_amministratore)
        self.setLayout(self.v_layout)

    # Metodo per titolare i parametri da inserire
    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        if tipo == "Codice Fiscale":
            current_text_edit.setText(self.amministratore.cf)
        if tipo == "Indirizzo":
            current_text_edit.setText(self.amministratore.indirizzo)
        if tipo == "Email":
            current_text_edit.setText(self.amministratore.email)
        if tipo == "Telefono":
            current_text_edit.setText(self.amministratore.telefono)
            current_text_edit.setValidator(QtGui.QIntValidator(0, 1000000000))
        if tipo == "Password":
            current_text_edit.setText(self.amministratore.password)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    # Metodo che crea uno spinbox per poter inserire correttamente l'età
    def get_spin_box(self, tipo):
        global current_text_edit
        self.v_layout.addWidget(QLabel(tipo))
        if tipo == "Età":
            current_text_edit = QSpinBox()
            current_text_edit.setValue(int(self.amministratore.eta))
            current_text_edit.setRange(0, 113)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    # Metodo che crea un menù a tendina dove selezionare il ruolo dell'amministratore tra quelli possibili
    def add_combobox_item(self, tipo):
        item = QStandardItem()
        item.setText(tipo)
        item.setEditable(False)
        self.combo_ruolo_model.appendRow(item)

    # Metodo per modificare i dati dell'amministratore
    def modifica_amministratore(self):

        nuovoruolo = self.combo_ruolo.currentText()
        nuovocf = self.info["Codice Fiscale"].text()
        nuovoindirizzo = self.info["Indirizzo"].text()
        nuovaemail = self.info["Email"].text()
        nuovotelefono = self.info["Telefono"].text()
        nuovaeta = self.info["Età"].text()
        nuovapassword = self.info["Password"].text()

        if nuovoruolo == "" or nuovocf == "" or nuovoindirizzo == "" or nuovaemail == "" or nuovotelefono == "" or nuovaeta == "" or nuovapassword == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste',
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.amministratore.ruolo = nuovoruolo
            self.amministratore.cf = nuovocf
            self.amministratore.indirizzo = nuovoindirizzo
            self.amministratore.email = nuovaemail
            self.amministratore.telefono = nuovotelefono
            self.amministratore.eta = nuovaeta
            self.amministratore.password = nuovapassword
            self.update()
            self.close()

    #salva i dati sul file pickle alla chiusura della view
    def closeEvent(self, event):
        self.controller.save_data()