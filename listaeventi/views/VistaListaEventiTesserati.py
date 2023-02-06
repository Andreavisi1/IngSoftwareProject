from PyQt5.QtGui import QStandardItemModel, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel
from PyQt5 import QtCore

from listaeventi.controller.ControlloreListaEventi import ControlloreListaEventi
from PyQt5 import QtGui

"""
La VistaListaEventiTesserati si occupa di mostrare a schermo la lista degli eventi, ma senza le funzionalità specifiche degli amministratori
"""

class VistaListaEventiTesserati(QWidget):
    def __init__(self, tesserato, parent=None):
        super(VistaListaEventiTesserati, self).__init__(parent)
        self.setFixedSize(1000, 300)
        self.controller = ControlloreListaEventi()
        self.tesserato = tesserato
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))

        self.main_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.label_intro = QLabel("Lista delle attività per la categoria " + self.tesserato.categoria + ":")
        self.v_layout.addWidget(self.label_intro)

        self.table_widget = QTableWidget()
        self.table_total = QListView()
        self.update_ui()

        self.table_total.setMaximumHeight(self.table_total.sizeHintForRow(0))

        self.v_layout.addWidget(self.table_widget)
        self.v_layout.addWidget(self.table_total)
        self.main_layout.addLayout(self.v_layout)

        buttons_layout = QVBoxLayout()

        self.main_layout.addLayout(buttons_layout)

        self.setLayout(self.main_layout)
        self.setWindowTitle("Lista Attività")

# crea/aggiorna l' intera view
    def update_ui(self):
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(5)
        self.create_table(0, "Titolo")
        self.create_table(1, "Tipo")
        self.create_table(2, "Data")
        self.create_table(3, "Categoria")
        self.create_table(4, "Luogo")

        row = 0
        for evento in self.controller.get_lista_degli_eventi():
            if evento.categoria == self.tesserato.categoria:
                self.table_widget.insertRow(row)
                self.inserisci_elemento_in_tabella(evento.titolo, row, 0)
                self.inserisci_elemento_in_tabella(evento.tipo, row, 1)
                self.inserisci_elemento_in_tabella(evento.data, row, 2)
                self.inserisci_elemento_in_tabella(evento.categoria, row, 3)
                self.inserisci_elemento_in_tabella(evento.luogo, row, 4)
                row = row + 1
        self.table_total_model = QStandardItemModel(self.table_total)
        self.table_total.setModel(self.table_total_model)

# genera l' header della tabella degli eventi
    def create_table(self, index, label):
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        item.setFont(font)
        item.setText(label)
        self.table_widget.setHorizontalHeaderItem(index, item)
        self.table_widget.setColumnWidth(index, 200)

# sulla chiusura della view salva i dati dell'evento
    def closeEvent(self, event):
        self.controller.save_data()

# inserisce singoli elementi in singole celle della tabella dato un indice
    def inserisci_elemento_in_tabella(self, elemento, row, index):
        item = QTableWidgetItem()
        item.setText(str(elemento))
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.table_widget.setItem(row, index, item)
