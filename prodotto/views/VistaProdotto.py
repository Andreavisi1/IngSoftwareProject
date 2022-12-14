from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QGridLayout, \
    QHBoxLayout, QMessageBox
from prodotto.controller.ControlloreProdotto import ControlloreProdotto
from prodotto.views.VistaAggiungiQuantita import VistaAggiungiQuantita
from prodotto.views.VistaModificaProdotto import VistaModificaProdotto
from PyQt5 import QtGui

"""
La classe VistaProdotto apre una finestra a schermo che si occupa di mostrare all'utente le informazioni del prodotto.
La classe VistaProdotto estende la classe QWidget
"""

class VistaProdotto(QWidget):
    def __init__(self, prodotto, elimina_prodotto, elimina_callback, carrello, parent=None):
        super(VistaProdotto, self).__init__(parent)
        self.controller = ControlloreProdotto(prodotto)
        self.elimina_prodotto = elimina_prodotto
        self.elimina_callback = elimina_callback
        self.prodotto = prodotto
        self.carrello = carrello

        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        #Vengono recuperate le informazioni da mostrare a schermo
        label_nome = QLabel(self.controller.get_marca_prodotto() + " " + self.controller.get_nome_prodotto())
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        #Aggiunge tramite metodo get_label_info il titolo di una informazione e l'informazione stessa tramite controller
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        v_layout.addWidget(self.get_label_info("Categoria", self.controller.get_categoria_prodotto()))

        self.label_prezzo = self.get_label_info("Prezzo", self.controller.get_prezzo_prodotto() + " €")
        self.label_quantita = self.get_label_info("Quantità", self.controller.get_quantita_disp())

        v_layout.addWidget(self.label_prezzo)
        v_layout.addWidget(self.label_quantita)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Bottone per eliminare un prodotto dal magazzino
        btn_elimina = QPushButton(" RIMUOVI DAL MAGAZZINO ")
        btn_elimina.clicked.connect(self.elimina_prodotto_click)
        h_layout.addWidget(btn_elimina)

        #Bottone per aggiugnere un prodotto al eventi
        btn_carrello = QPushButton("Aggiungi al Carrello")
        btn_carrello.clicked.connect(self.aggiungi_al_carrello)
        h_layout.addWidget(btn_carrello)

        #Bottone per modificare quantià e prezzo di un prodotto
        btn_modify = QPushButton("Modifica Quantità e Prezzo")
        btn_modify.clicked.connect(self.show_modifica_prodotto)
        h_layout.addWidget(btn_modify)

        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_marca_prodotto() + " " + self.controller.get_nome_prodotto())

    #Metodo che prende come parametri il testo di una informazione e il valore assegnato come sopra tramite il controller
    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    #Metodo che si occupa di eliminare il prodotto
    def elimina_prodotto_click(self):
        reply = QMessageBox.question(self, "Conferma", "Sei sicuro di voler eliminare il prodotto dal magazzino?", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.elimina_prodotto(self.controller.get_id_prodotto())
            self.elimina_callback()
            self.close()
        else:
            return

    #Metodo che si occupa di aprire la VistaModificaProdotto
    def show_modifica_prodotto(self):
        self.vista_modifica_prodotto = VistaModificaProdotto(self.prodotto, self.update_prodotto)
        self.vista_modifica_prodotto.show()

    #Metodo che si occupa di aprire la VistaAggiungiQuantità
    def aggiungi_al_carrello(self):
        self.vista_aggiungi_quantita = VistaAggiungiQuantita(self.prodotto, self.carrello)
        self.vista_aggiungi_quantita.show()
        self.close()

    #Metodo che si occupa di aggiornare prezzo e quantità nella view del prodotto
    def update_prodotto(self):
        self.label_prezzo.setText("Prezzo: {}".format(self.controller.get_prezzo_prodotto() + " €"))
        self.label_quantita.setText("Quantità: {}".format(self.controller.get_quantita_disp()))





