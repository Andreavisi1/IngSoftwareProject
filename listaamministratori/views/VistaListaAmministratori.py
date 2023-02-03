from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QMessageBox
from amministratore.views.VistaAmministratore import VistaAmministratore
from listaamministratori.controller.ControlloreListaAmministratori import ControlloreListaAmministratori
from listaamministratori.views.VistaInserisciAmministratore import VistaInserisciAmministratore
from PyQt5 import QtGui

"""
La VistaListaAmministratori si occupa di mostrare a schermo la lista degli amministratori
"""

class VistaListaAmministratori(QWidget):
    def __init__(self, parent=None):
        super(VistaListaAmministratori, self).__init__(parent)

        self.controller = ControlloreListaAmministratori()
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        #Bottone per aprire un amministratore
        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        #Bottone per creare un nuovo amministratore
        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_new_amministratore)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle("Lista Amministratori")

    #Metodo che mostra a schermo le informazioni dell'amministratore selezionato
    def show_selected_info(self):
        try:
            sourceindex = self.list_view.selectedIndexes()[0].row()
            amministratore_selezionato = self.controller.get_amministratore_by_index(sourceindex)
            self.vista_amministratore = VistaAmministratore(amministratore_selezionato, self.controller.elimina_amministratore_by_id, self.update_ui)
            self.vista_amministratore.show()
        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Per favore, seleziona un amministratore', QMessageBox.Ok, QMessageBox.Ok)

    #Metodo aprire la vista di inserimento del nuovo amministratore
    def show_new_amministratore(self):
        self.vista_inserisci_amministratore = VistaInserisciAmministratore(self.controller, self.update_ui)
        self.vista_inserisci_amministratore.show()

    #Metodo che serve per generare e/o aggiornare la vista
    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for amministratore in self.controller.get_lista_degli_amministratori():
            item = QStandardItem()
            item.setText(amministratore.nome + " " + amministratore.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listview_model.sort(0, )
        self.list_view.setModel(self.listview_model)

    #salva i dati sul file pickle alla chiusura della view
    def closeEvent(self, event):
        self.controller.save_data()