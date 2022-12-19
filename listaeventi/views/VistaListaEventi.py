from PyQt5.QtCore import QSortFilterProxyModel, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLineEdit, QSpacerItem, \
    QMessageBox
from attivita.controller.ControlloreAttivita import ControlloreAttivita
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
        self.attivita = ControlloreAttivita()
        self.controller = ControlloreListaEventi()
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
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

        #Bottone per aprire un evento
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        #Bottone per creare un nuovo evento
        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_new_evento)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)
        self.resize(600,300)
        self.setWindowTitle("Lista Eventi")

    #Metodo che mostra a schermo le informazioni dell'evento selezionato
    def show_selected_info(self):
        try:
            sourceindex = self.list_view.selectedIndexes()[0].row()
            evento_selezionato = self.controller.get_evento_by_index(sourceindex)
            self.vista_evento = VistaEvento(evento_selezionato, self.controller.elimina_evento_by_id, self.update_ui, self.attivita)
            self.vista_evento.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Per favore, seleziona un evento', QMessageBox.Ok, QMessageBox.Ok)

    #Metodo aprire la vista di inserimento del nuovo evento
    def show_new_evento(self):
        self.vista_inserisci_evento = VistaInserisciEvento(self.controller, self.update_ui)
        self.vista_inserisci_evento.show()

    #Metodo che serve per generare e/o aggiornare la vista
    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for evento in self.controller.get_lista_degli_eventi():
            item = QStandardItem()
            item.setText(evento.tipo + " " + evento.data)
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


