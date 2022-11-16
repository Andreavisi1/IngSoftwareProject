from PyQt5.QtCore import QSortFilterProxyModel, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from cliente.views.VistaCliente import VistaCliente
from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti
from listaclienti.views.VistaInserisciCliente import VistaInserisciCliente
from PyQt5 import QtGui
"""
La VistaListaClienti si occupa di mostrare a schermo la lista dei clienti
"""

class VistaListaClienti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaClienti, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))
        self.controller = ControlloreListaClienti()
        main_layout = QHBoxLayout()

        v_layout = QVBoxLayout()

        self.list_view = QListView()
        self.update_ui()

        #Crea un elenco fittizio sopra l'elenco reale per poter usare la barra di ricerca
        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.listview_model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(0)

        search_field = QLineEdit()
        search_field.setStyleSheet('font-size: 15px; height: 30px;')
        search_field.textChanged.connect(self.filter_proxy_model.setFilterRegExp)
        v_layout.addWidget(search_field)

        self.list_view.setModel(self.filter_proxy_model)

        v_layout.addWidget(self.list_view)
        main_layout.addLayout(v_layout)

        #Bottone per aprire un cliente
        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        #Bottone per creare un nuovo cliente
        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_new_cliente)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)
        self.resize(600,300)
        self.setWindowTitle("Lista Clienti")

    #Metodo che mostra a schermo le informazioni del cliente selezionato
    def show_selected_info(self):
        try:
            sourceindex = self.list_view.selectedIndexes()[0].row()
            cliente_selezionato = self.controller.get_cliente_by_index(sourceindex)
            self.vista_cliente = VistaCliente(cliente_selezionato, self.controller.rimuovi_cliente_by_id, self.update_ui)
            self.vista_cliente.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Per favore, seleziona un cliente', QMessageBox.Ok, QMessageBox.Ok)

    #Metodo aprire la vista di inserimento del nuovo cliente
    def show_new_cliente(self):
        self.vista_inserisci_cliente = VistaInserisciCliente(self.controller, self.update_ui)
        self.vista_inserisci_cliente.show()

    #Metodo che serve per generare e/o aggiornare la vista
    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.controller.get_lista_dei_clienti():
            item = QStandardItem()
            item.setText(cliente.nome + " " + cliente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    # salva i dati sul file pickle alla chiusura della view
    def closeEvent(self, event):
        self.controller.save_data()

    #Metodo per collegare l'indice selezionato all'elenco fittizio all'indice dell'elenco reale
    def toSourceIndex(self, index):
        return self.filter_proxy_model.mapToSource(index).row()