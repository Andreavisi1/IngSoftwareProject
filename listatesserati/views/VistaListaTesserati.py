from PyQt5.QtCore import QSortFilterProxyModel, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from tesserato.views.VistaTesserato import VistaTesserato
from listatesserati.controller.ControlloreListaTesserati import ControlloreListaTesserati
from listatesserati.views.VistaInserisciTesserato import VistaInserisciTesserato
from PyQt5 import QtGui
"""
La VistaListaTesserati si occupa di mostrare a schermo la lista dei tesserati
"""

class VistaListaTesserati(QWidget):
    def __init__(self, parent=None):
        super(VistaListaTesserati, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        self.controller = ControlloreListaTesserati()
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

        #Bottone per aprire un tesserato
        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        #Bottone per creare un nuovo tesserato
        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_new_tesserato)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)
        self.resize(600,300)
        self.setWindowTitle("Lista Tesserati")

    #Metodo che mostra a schermo le informazioni del tesserato selezionato
    def show_selected_info(self):
        try:
            sourceindex = self.list_view.selectedIndexes()[0].row()
            tesserato_selezionato = self.controller.get_tesserato_by_index(sourceindex)
            self.vista_tesserato = VistaTesserato(tesserato_selezionato, self.controller.rimuovi_tesserato_by_id, self.update_ui)
            self.vista_tesserato.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Per favore, seleziona un tesserato', QMessageBox.Ok, QMessageBox.Ok)

    #Metodo aprire la vista di inserimento del nuovo tesserato
    def show_new_tesserato(self):
        self.vista_inserisci_tesserato = VistaInserisciTesserato(self.controller, self.update_ui)
        self.vista_inserisci_tesserato.show()

    #Metodo che serve per generare e/o aggiornare la vista
    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for tesserato in self.controller.get_lista_dei_tesserati():
            item = QStandardItem()
            item.setText(tesserato.nome + " " + tesserato.cognome)
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