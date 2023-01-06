from PyQt5.QtCore import QDate
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, \
    QComboBox, QRadioButton, QCalendarWidget, QDateEdit
from datetime import datetime
from evento.model.Evento import Evento
from PyQt5 import QtGui

"""
La classe VistaInserisciEvento si occupa di mostrare all'utente il form per registrare i dati del nuovo evento
"""

class VistaInserisciEvento(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciEvento, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        self.resize(300, 200)

        self.v_layout = QVBoxLayout()

        self.v_layout.addWidget(QLabel("Stai inserendo:"))

        self.AButton = QRadioButton("Allenamento")
        self.AButton.setChecked(True)
        self.v_layout.addWidget(self.AButton)
        self.GButton = QRadioButton("Gara")
        self.v_layout.addWidget(self.GButton)


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
        self.v_layout.addWidget(self.combo_categoria)

        self.get_form_entry("Luogo")
        self.get_spin_box("Data")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_evento)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Evento")

#Metodo per titolare i parametri da inserire
    def get_form_entry(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        if tipo == "Luogo":
            current_text_edit.setText("Palestra comunale Filottrano")
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def get_spin_box(self, tipo):
        global current_text_edit
        self.v_layout.addWidget(QLabel(tipo))
        if tipo == "Data":
            current_text_edit = QDateEdit()
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

    def rb_on_selected(self):
        if self.AButton.isChecked():
            return "Allenamento"
        elif self.GButton.isChecked():
            return "Gara"

# Metodo che genera un nuovo evento sfruttando le informazioni inserite dall'utente
    def add_evento(self):
        tipo = self.rb_on_selected()
        titolo = self.info["Titolo (opzionale)"].text()
        categoria = self.combo_categoria.currentText()
        luogo = self.info["Luogo"].text()
        data = self.info["Data"].text()
        today = datetime.now().date()
        print(QDate.fromString(data, "dd/MM/yy"))
        print(QDate.fromString(str(today), "yyyy-MM-dd"))

        if tipo == "" or categoria == "" or luogo == "" or data == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        elif QDate.fromString(data, "dd/MM/yy") < QDate.fromString(str(today), "yyyy/MM/dd"):
            QMessageBox.critical(self, 'Errore', 'Il passato non può essere modificato, ma solo accettato... Per favore, inserire una data valida', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_evento(Evento((tipo + data).lower(), tipo, titolo, categoria, luogo, data))
            self.controller.save_data()
            self.callback()
            self.close()
