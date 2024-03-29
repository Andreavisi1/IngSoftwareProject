from PyQt5.QtCore import QDate
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, QSpinBox, QDateEdit, QComboBox
from PyQt5 import QtGui

"""
La classe VistaModificaDatiSportiviTesserato apre una finestra a schermo in cui il presidente o un amministratore possono modificare i dati sportivi di un tesserato
"""

class VistaModificaDatiSportiviTesserato(QWidget):
    def __init__(self, tesserato, update, parent=None):
        super(VistaModificaDatiSportiviTesserato, self).__init__(parent)
        self.tesserato = tesserato
        self.info = {}
        self.update = update
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        self.setWindowTitle('Modifica Dati Sportivi Tesserato')
        self.v_layout = QVBoxLayout()
        self.resize(300, 200)

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
        self.combo_categoria.setCurrentText(self.tesserato.categoria)
        self.v_layout.addWidget(self.combo_categoria)

        self.get_spin_box("Numero di gare partecipate")
        self.get_spin_box("Numero di gare vinte")

        self.get_spin_box("Inizio validità certificato")
        self.get_spin_box("Scadenza validità certificato")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Bottone per confermare i cambiamenti
        btn_conferma = QPushButton("Conferma")
        self.v_layout.addWidget(btn_conferma)
        btn_conferma.clicked.connect(self.modifica_tesserato)
        self.setLayout(self.v_layout)

# Metodo che crea uno spinbox per poter modificare correttamente i dati riguardanti le gare e la validità del certificato
    def get_spin_box(self, tipo):
        global current_text_edit
        self.v_layout.addWidget(QLabel(tipo))
        if tipo == "Inizio validità certificato":
            current_text_edit = QDateEdit()
            current_text_edit.setDisplayFormat("dd/MM/yyyy")
            current_text_edit.setDate(QDate.fromString(self.tesserato.inizio_certificato, "dd/MM/yyyy"))
            current_text_edit.setCalendarPopup(True)
        if tipo == "Scadenza validità certificato":
            current_text_edit = QDateEdit()
            current_text_edit.setDisplayFormat("dd/MM/yyyy")
            current_text_edit.setDate(QDate.fromString(self.tesserato.scadenza_certificato, "dd/MM/yyyy"))
            current_text_edit.setCalendarPopup(True)
        if tipo == "Numero di gare partecipate":
            current_text_edit = QSpinBox()
            current_text_edit.setValue(int(self.tesserato.gare_partecipate))
            current_text_edit.setRange(0, 1000)
        if tipo == "Numero di gare vinte":
            current_text_edit = QSpinBox()
            current_text_edit.setValue(int(self.tesserato.gare_vinte))
            current_text_edit.setRange(0, 1000)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    # Metodo che crea un menù a tendina
    def add_combobox_item(self, tipo):
        item = QStandardItem()
        item.setText(tipo)
        item.setEditable(False)
        self.combo_categoria_model.appendRow(item)

    # Metodo per modificare i dati di un tesserato
    def modifica_tesserato(self):
        nuovacategoria = self.combo_categoria.currentText()
        nuovoiniziocertificato = self.info["Inizio validità certificato"].text()
        nuovascadenzacertificato = self.info["Scadenza validità certificato"].text()
        nuovegarepartecipate = int(self.info["Numero di gare partecipate"].text())
        nuovegarevinte = int(self.info["Numero di gare vinte"].text())

        if nuovacategoria == "" or nuovoiniziocertificato == "" or nuovascadenzacertificato == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        elif nuovegarevinte > nuovegarepartecipate:
            QMessageBox.critical(self, 'Errore', 'Questo ragazzo è un campione, ma non può vincere più gare di quante ne abbia fatte',
                                 QMessageBox.Ok, QMessageBox.Ok)
        elif QDate.fromString(nuovoiniziocertificato, "dd/MM/yyyy") > QDate.fromString(nuovascadenzacertificato, "dd/MM/yyyy"):
            QMessageBox.critical(self, 'Errore', 'Il certificato è scaduto ancor prima di iniziare?', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.tesserato.categoria = nuovacategoria
            self.tesserato.inizio_certificato = nuovoiniziocertificato
            self.tesserato.scadenza_certificato = nuovascadenzacertificato
            self.tesserato.gare_partecipate = nuovegarepartecipate
            self.tesserato.gare_vinte = nuovegarevinte
            self.update()
            self.close()
