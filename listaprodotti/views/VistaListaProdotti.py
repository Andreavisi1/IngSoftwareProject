from PyQt5.QtCore import QSortFilterProxyModel, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLineEdit, QSpacerItem, \
    QMessageBox
from attivita.controller.ControlloreAttivita import ControlloreAttivita
from listaprodotti.controller.ControlloreListaProdotti import ControlloreListaProdotti
from listaprodotti.views.VistaInserisciProdotto import VistaInserisciProdotto
from prodotto.views.VistaProdotto import VistaProdotto
from PyQt5 import QtGui

"""
La VistaListaProdotti si occupa di mostrare a schermo la lista dei prodotti
"""


class VistaListaProdotti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaProdotti, self).__init__(parent)
        self.attivita = ControlloreAttivita()
        self.controller = ControlloreListaProdotti()
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))
        main_layout = QHBoxLayout()

        v_layout = QVBoxLayout()

        self.list_view = QListView()
        self.update_ui()

        #Crea un elenco fittizio sopra l'elenco reale per poter usare la barra di ricerca
        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.listview_model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(0)

        self.list_view.setModel(self.filter_proxy_model)

        search_field = QLineEdit()
        search_field.setStyleSheet('font-size: 15px; height: 30px;')
        search_field.textChanged.connect(self.filter_proxy_model.setFilterRegExp)



        v_layout.addWidget(search_field)
        v_layout.addWidget(self.list_view)
        main_layout.addLayout(v_layout)

        buttons_layout = QVBoxLayout()

        buttons_layout.addItem(QSpacerItem(40, 40))

        #Bottone per aprire un prodotto
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        #Bottone per creare un nuovo prodotto
        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_new_prodotto)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)
        self.resize(600,300)
        self.setWindowTitle("Lista Prodotti")

    #Metodo che mostra a schermo le informazioni del prodotto selezionato
    def show_selected_info(self):
        try:
            sourceindex = self.list_view.selectedIndexes()[0].row()
            prodotto_selezionato = self.controller.get_prodotto_by_index(sourceindex)
            self.vista_prodotto = VistaProdotto(prodotto_selezionato, self.controller.elimina_prodotto_by_id, self.update_ui, self.attivita)
            self.vista_prodotto.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Per favore, seleziona un prodotto', QMessageBox.Ok, QMessageBox.Ok)

    #Metodo aprire la vista di inserimento del nuovo prodotto
    def show_new_prodotto(self):
        self.vista_inserisci_prodotto = VistaInserisciProdotto(self.controller, self.update_ui)
        self.vista_inserisci_prodotto.show()

    #Metodo che serve per generare e/o aggiornare la vista
    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for prodotto in self.controller.get_lista_dei_prodotti():
            item = QStandardItem()
            item.setText(prodotto.marca + " " + prodotto.nome)
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


