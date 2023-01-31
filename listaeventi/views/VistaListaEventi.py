from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QStandardItemModel, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore

from listaeventi.controller.ControlloreListaEventi import ControlloreListaEventi
from listaeventi.views.VistaInserisciEvento import VistaInserisciEvento
from evento.views.VistaEvento import VistaEvento
from PyQt5 import QtGui

"""
La VistaListaEventi si occupa di mostrare a schermo la lista degli eventi
"""

class VistaListaEventi(QWidget):
    def __init__(self, parent=None):
        super(VistaListaEventi, self).__init__(parent)
        self.setFixedSize(1000, 300)
        self.controller = ControlloreListaEventi()
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))

        self.main_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.table_total = QListView()
        self.update_ui()

        self.table_total.setMaximumHeight(self.table_total.sizeHintForRow(0))

# Metodo Qt che ordina in maniera decrescente gli allenamenti e le gare in base alla data
        self.table_widget.sortItems(2, Qt.DescendingOrder)

        self.v_layout.addWidget(self.table_widget)
        self.v_layout.addWidget(self.table_total)
        self.main_layout.addLayout(self.v_layout)

        buttons_layout = QVBoxLayout()

        #Bottone per aprire un evento
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        #Bottone per creare un nuovo evento
        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_new_evento)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        self.main_layout.addLayout(buttons_layout)
        self.main_layout.addWidget(new_button)

        self.setLayout(self.main_layout)
        self.setWindowTitle("Lista Attività")

    #Metodo che mostra a schermo le informazioni dell'evento selezionato
    def show_selected_info(self):
        try:
            sourceindex = self.table_widget.selectedIndexes()[0].row()
            evento_selezionato = self.controller.get_evento_by_index(sourceindex)
            self.vista_evento = VistaEvento(evento_selezionato, self.controller.elimina_evento_by_id, self.update_ui)
            self.vista_evento.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Per favore, seleziona un evento', QMessageBox.Ok, QMessageBox.Ok)

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
            self.table_widget.insertRow(row)
            self.inserisci_elemento_in_tabella(evento.titolo, row, 0)
            self.inserisci_elemento_in_tabella(evento.tipo, row, 1)
            self.inserisci_elemento_in_tabella(evento.data, row, 2)
            self.inserisci_elemento_in_tabella(evento.categoria, row, 3)
            self.inserisci_elemento_in_tabella(evento.luogo, row, 4)
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

# sulla chiusura della view salva i dati del attivita
    def closeEvent(self, event):
        self.controller.save_data()

# inserisce singoli elementi in singole celle della tabella dato un indice
    def inserisci_elemento_in_tabella(self, elemento, row, index):
        item = QTableWidgetItem()
        item.setText(str(elemento))
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.table_widget.setItem(row, index, item)

    #Metodo aprire la vista di inserimento del nuovo evento
    def show_new_evento(self):
        self.vista_inserisci_evento = VistaInserisciEvento(self.controller, self.update_ui)
        self.vista_inserisci_evento.show()

    #Metodo per collegare l'indice selezionato all'elenco fittizio all'indice dell'elenco reale
    def toSourceIndex(self, index):
        return self.filter_proxy_model.mapToSource(index).row()


