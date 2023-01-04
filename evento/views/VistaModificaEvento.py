from datetime import datetime

from PyQt5.QtCore import QDate
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, \
    QRadioButton, QComboBox, QCalendarWidget, QDateEdit
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

        self.AButton = QRadioButton("Allenamento")
        self.v_layout.addWidget(self.AButton)
        self.GButton = QRadioButton("Gara")
        self.v_layout.addWidget(self.GButton)
        if self.evento.tipo == "Allenamento":
            self.AButton.setChecked(True)
        elif self.evento.tipo == "Gara":
            self.GButton.setChecked(True)

        self.get_form_entry("Titolo (opzionale)")

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
        self.combo_categoria.setCurrentText(self.evento.categoria)
        self.v_layout.addWidget(self.combo_categoria)

        self.get_form_entry("Luogo")
        self.get_spin_box("Data")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Bottone per confermare i cambiamenti
        btn_conferma = QPushButton("Conferma")
        self.v_layout.addWidget(btn_conferma)
        btn_conferma.clicked.connect(self.modifica_evento)
        self.setLayout(self.v_layout)

    #Metodo per titolare i parametri da inserire
    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        if tipo == "Titolo (opzionale)":
            current_text_edit.setText(self.evento.titolo)
        if tipo == "Luogo":
            current_text_edit.setText(self.evento.luogo)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def get_calendar(self, tipo):
        global current_text_edit
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QCalendarWidget(gridVisible=True)
        date = QDate()
        date.fromString(self.evento.data, "dd/MM/yyyy")
        current_text_edit.setSelectedDate(date)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit.selectedDate()

    def get_spin_box(self, tipo):
        global current_text_edit
        self.v_layout.addWidget(QLabel(tipo))
        if tipo == "Data":
            current_text_edit = QDateEdit()
            current_text_edit.setDate(QDate.fromString(self.evento.data, "dd/MM/yy"))
            current_text_edit.setCalendarPopup(True)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

# Metodo che crea un menù a tendina dove selezionare la tipologia dell'evento da inserire
    def add_combobox_item(self, tipo):
        item = QStandardItem()
        item.setText(tipo)
        item.setEditable(False)
        self.combo_categoria_model.appendRow(item)

    def rb_on_selected(self):
        if self.AButton.isChecked():
            return "Allenamento"
        elif self.GButton.isChecked():
            return "Gara"

#Metodo per modificare i parametri di prezzo e quantità del evento
    def modifica_evento(self):
        nuovotipo = self.rb_on_selected()
        nuovotitolo = self.info["Titolo (opzionale)"].text()
        nuovacategoria = self.combo_categoria.currentText()
        nuovoluogo = self.info["Luogo"].text()
        nuovadata = self.info["Data"].text()

        if nuovotipo == "" or nuovacategoria == "" or nuovoluogo == "" or nuovadata == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)

        else:
            self.evento.tipo = nuovotipo
            self.evento.titolo = nuovotitolo
            self.evento.categoria = nuovacategoria
            self.evento.luogo = nuovoluogo
            self.evento.data = nuovadata
            self.update()
            self.close()
