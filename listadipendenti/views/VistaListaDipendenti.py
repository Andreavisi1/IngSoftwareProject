from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QMessageBox
from dipendente.views.VistaDipendente import VistaDipendente
from listadipendenti.controller.ControlloreListaDipendenti import ControlloreListaDipendenti
from listadipendenti.views.VistaInserisciDipendente import VistaInserisciDipendente
from PyQt5 import QtGui
"""
La VistaListaDipendenti si occupa di mostrare a schermo la lista dei dipendenti
"""


class VistaListaDipendenti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaDipendenti, self).__init__(parent)

        self.controller = ControlloreListaDipendenti()
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        #Bottone per aprire un dipendente
        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        #Bottone per creare un nuovo dipendente
        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_new_dipendente)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle("Lista Dipendenti")

    #Metodo che mostra a schermo le informazioni del dipendente selezionato
    def show_selected_info(self):
        try:
            sourceindex = self.list_view.selectedIndexes()[0].row()
            dipendente_selezionato = self.controller.get_dipendente_by_index(sourceindex)
            self.vista_dipendente = VistaDipendente(dipendente_selezionato, self.controller.elimina_dipendente_by_id, self.update_ui)
            self.vista_dipendente.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Per favore, seleziona un dipendente', QMessageBox.Ok, QMessageBox.Ok)

    #Metodo aprire la vista di inserimento del nuovo tesserato
    def show_new_dipendente(self):
        self.vista_inserisci_dipendente = VistaInserisciDipendente(self.controller, self.update_ui)
        self.vista_inserisci_dipendente.show()

    #Metodo che serve per generare e/o aggiornare la vista
    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for dipendente in self.controller.get_lista_dei_dipendenti():
            item = QStandardItem()
            item.setText(dipendente.nome + " " + dipendente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    #salva i dati sul file pickle alla chiusura della view
    def closeEvent(self, event):
        self.controller.save_data()