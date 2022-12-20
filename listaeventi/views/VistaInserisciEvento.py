from PyQt5.QtGui import QStandardItemModel, QStandardItem, QRegExpValidator
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, \
    QComboBox, QDoubleSpinBox, QSpinBox, QRadioButton, QCalendarWidget
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
        self.add_radio_button("Allenamento")
        self.add_radio_button("Gara")

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
        self.get_calendar("Data")

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

    def get_calendar(self, tipo):
        global current_text_edit
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QCalendarWidget()
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    #Metodo che crea un menù a tendina dove selezionare la tipologia dell'evento da inserire
    def add_combobox_item(self, tipo):
        item = QStandardItem()
        item.setText(tipo)
        item.setEditable(False)
        self.combo_categoria_model.appendRow(item)

    def add_radio_button(self, tipo):
        item = QRadioButton()
        item.setText(tipo)
        if tipo == "Allenamento":
            item.setChecked(True)
        item.toggled.connect(self.update)
        self.v_layout.addWidget(item)

    def on_selected(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            if radio_button.text() == "Allenamento":
                return "Allenamento"
            else:
                return "Gara"

    #Metodo che genera un nuovo evento sfruttando le informazioni inserite dall'utente
    def add_evento(self):
        tipo = self.info["Stai inserendo:"].text()
        titolo = self.info["Titolo (opzionale)"].text()
        categoria = self.combo_categoria.currentText()
        luogo = self.info["Luogo"].text()
        data = self.info["Data"].text()

        if tipo == "" or categoria == "" or luogo == "" or data == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)


        else:
            self.controller.aggiungi_evento(Evento((tipo + data).lower(), tipo, titolo, categoria, luogo, data))
            self.controller.save_data()
            self.callback()
            self.close()

