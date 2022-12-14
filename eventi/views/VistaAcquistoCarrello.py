from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QGridLayout, \
    QHBoxLayout, QMessageBox

from prodotto.controller.ControlloreProdotto import ControlloreProdotto
from listaprodotti.controller.ControlloreListaProdotti import ControlloreListaProdotti
from eventi.controller.ControlloreEventi import ControlloreCarrello
from prodotto.views.VistaModificaProdotto import VistaModificaProdotto
from PyQt5 import QtGui

class VistaAcquistoCarrello(QWidget):
    def __init__(self, prodotto, elimina_prodotto, elimina_callback, parent=None):
        super(VistaAcquistoCarrello, self).__init__(parent)
        self.controller = ControlloreProdotto(prodotto)
        self.elimina_prodotto = elimina_prodotto
        self.elimina_callback = elimina_callback
        self.prodotto = prodotto
        self.controlloremagazzino = ControlloreListaProdotti()
        self.carrello = ControlloreCarrello()


        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        #Vengono recuperate le informazioni da mostrare a schermo
        label_nome = QLabel(self.controller.get_marca_prodotto() + " " + self.controller.get_nome_prodotto())
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome, )

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Aggiunge tramite metodo get_label_info il titolo di una informazione e l'informazione stessa tramite controller
        v_layout.addWidget(self.get_label_info("Categoria", self.controller.get_categoria_prodotto()))
        self.label_prezzo = self.get_label_info("Prezzo", self.controller.get_prezzo_prodotto() + " €")
        self.label_quantita = self.get_label_info("Quantità", self.controller.get_quantita_carrello())
        v_layout.addWidget(self.label_prezzo)
        v_layout.addWidget(self.label_quantita)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Genera un bottone per rimuovere il prodotto dal eventi
        btn_elimina = QPushButton(" RIMUOVI DAL CARRELLO ")
        btn_elimina.clicked.connect(self.elimina_acquisto_click)
        h_layout.addWidget(btn_elimina)

        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_marca_prodotto() + " " + self.controller.get_nome_prodotto())

    #Metodo che assegna come parametri un' informazione e il valore assegnato come sopra tramite il controller
    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    #Metodo richiamato dal bottone che elimina l' acquisto dal eventi
    def elimina_acquisto_click(self):
        reply = QMessageBox.question(self, "Conferma", "Sei sicuro di voler eliminare il prodotto dal eventi?", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.elimina_prodotto(self.controller.get_id_prodotto())
            self.controlloremagazzino.ritorna_quantita(self.prodotto.id, self.prodotto.quantita_carrello)
            self.carrello.save_data()
            self.elimina_callback()
            self.close()
        else:
            return




