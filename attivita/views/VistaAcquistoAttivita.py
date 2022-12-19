from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QGridLayout, \
    QHBoxLayout, QMessageBox

from evento.controller.ControlloreEvento import ControlloreEvento
from listaeventi.controller.ControlloreListaEventi import ControlloreListaEventi
from attivita.controller.ControlloreAttivita import ControlloreAttivita
from evento.views.VistaModificaEvento import VistaModificaEvento
from PyQt5 import QtGui

class VistaAcquistoAttivita(QWidget):
    def __init__(self, evento, elimina_evento, elimina_callback, parent=None):
        super(VistaAcquistoAttivita, self).__init__(parent)
        self.controller = ControlloreEvento(evento)
        self.elimina_evento = elimina_evento
        self.elimina_callback = elimina_callback
        self.evento = evento
        self.controlloremagazzino = ControlloreListaEventi()
        self.attivita = ControlloreAttivita()


        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        #Vengono recuperate le informazioni da mostrare a schermo
        label_nome = QLabel(self.controller.get_tipo_evento() + " " + self.controller.get_data_evento())
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome, )

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Aggiunge tramite metodo get_label_info il titolo di una informazione e l'informazione stessa tramite controller
        v_layout.addWidget(self.get_label_info("Categoria", self.controller.get_categoria_evento()))
        self.label_quantita = self.get_label_info("Quantità", self.controller.get_quantita_attivita())
        v_layout.addWidget(self.label_prezzo)
        v_layout.addWidget(self.label_quantita)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Genera un bottone per rimuovere il evento dal attivita
        btn_elimina = QPushButton(" RIMUOVI DALLE ATTIVITA' ")
        btn_elimina.clicked.connect(self.elimina_acquisto_click)
        h_layout.addWidget(btn_elimina)

        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_tipo_evento() + " " + self.controller.get_data_evento())

    #Metodo che assegna come parametri un' informazione e il valore assegnato come sopra tramite il controller
    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    #Metodo richiamato dal bottone che elimina l' acquisto dal attivita
    def elimina_acquisto_click(self):
        reply = QMessageBox.question(self, "Conferma", "Sei sicuro di voler eliminare il evento dalle attivita", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.elimina_evento(self.controller.get_id_evento())
            self.controlloremagazzino.ritorna_quantita(self.evento.id, self.evento.quantita_attivita)
            self.attivita.save_data()
            self.elimina_callback()
            self.close()
        else:
            return




