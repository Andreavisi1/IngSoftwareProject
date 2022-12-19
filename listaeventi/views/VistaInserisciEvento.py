from PyQt5.QtGui import QStandardItemModel, QStandardItem, QRegExpValidator
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, \
    QComboBox, QDoubleSpinBox, QSpinBox
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
        self.v_layout.addWidget(QLabel("Categoria"))
        self.combo_categoria = QComboBox()
        self.combo_categoria_model = QStandardItemModel(self.combo_categoria)
        self.add_combobox_item("Telefonia")
        self.add_combobox_item("Informatica")
        self.add_combobox_item("Piccoli Elettrodomestici")
        self.add_combobox_item("Elettrodomestici")
        self.add_combobox_item("TV e Hi-Fi")
        self.combo_categoria.setModel(self.combo_categoria_model)
        self.v_layout.addWidget(self.combo_categoria)

        self.get_form_entry("Marca")
        self.get_form_entry("Nome")
        self.get_spin_box("Prezzo")
        self.get_spin_box("Quantità")

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
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def get_spin_box(self, tipo):
        global current_text_edit
        self.v_layout.addWidget(QLabel(tipo))
        if tipo == "Prezzo":
            current_text_edit = QDoubleSpinBox()
            current_text_edit.setRange(0, 10000000)
        if tipo == "Quantità":
            current_text_edit = QSpinBox()
            current_text_edit.setRange(0, 100)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    #Metodo che crea un menù a tendina dove selezionare la tipologia del evento da inserire
    def add_combobox_item(self, tipo):
        item = QStandardItem()
        item.setText(tipo)
        item.setEditable(False)
        self.combo_categoria_model.appendRow(item)

    #Metodo che genera un nuovo evento sfruttando le informazioni inserite dall'utente
    def add_evento(self):

        marca = self.info["Marca"].text()
        nome = self.info["Nome"].text()
        categoria = self.combo_categoria.currentText()
        prezzo = self.info["Prezzo"].text()
        prezzo = prezzo.replace(",", ".")
        quantita = self.info["Quantità"].text()

        if marca == "" or nome == "" or categoria == "" or prezzo == "" or quantita == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)


        else:
            self.controller.aggiungi_evento(Evento((marca + nome).lower(), marca, nome, categoria, prezzo, quantita, 0))
            self.controller.save_data()
            self.callback()
            self.close()

