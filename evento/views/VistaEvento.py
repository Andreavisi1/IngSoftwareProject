from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QGridLayout, \
    QHBoxLayout, QMessageBox
from evento.controller.ControlloreEvento import ControlloreEvento
from evento.views.VistaAggiungiQuantita import VistaAggiungiQuantita
from evento.views.VistaModificaEvento import VistaModificaEvento
from PyQt5 import QtGui

"""
La classe VistaEvento apre una finestra a schermo che si occupa di mostrare all'utente le informazioni dell'evento.
La classe VistaEvento estende la classe QWidget
"""

class VistaEvento(QWidget):
    def __init__(self, evento, elimina_evento, elimina_callback, attivita, parent=None):
        super(VistaEvento, self).__init__(parent)
        self.controller = ControlloreEvento(evento)
        self.elimina_evento = elimina_evento
        self.elimina_callback = elimina_callback
        self.evento = evento
        self.attivita = attivita

        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        #Vengono recuperate le informazioni da mostrare a schermo
        label_nome = QLabel(self.controller.get_tipo_evento() + " " + self.controller.get_data_evento())
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        #Aggiunge tramite metodo get_label_info il titolo di una informazione e l'informazione stessa tramite controller
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        v_layout.addWidget(self.get_label_info("Titolo", self.controller.get_titolo_evento()))
        v_layout.addWidget(self.get_label_info("Categoria", self.controller.get_categoria_evento()))
        v_layout.addWidget(self.get_label_info("Luogo", self.controller.get_luogo_evento()))

        self.label_quantita = self.get_label_info("Quantità", self.controller.get_quantita_disp())

        v_layout.addWidget(self.label_quantita)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Bottone per eliminare un evento dal calendario
        btn_elimina = QPushButton(" RIMUOVI DAL CALENDARIO ")
        btn_elimina.clicked.connect(self.elimina_evento_click)
        h_layout.addWidget(btn_elimina)

        #Bottone per aggiungere un evento alle attivita
        btn_attivita = QPushButton("Aggiungi alle attivita")
        btn_attivita.clicked.connect(self.aggiungi_alle_attivita)
        h_layout.addWidget(btn_attivita)

        #Bottone per modificare quantià e prezzo di un evento
        btn_modify = QPushButton("Modifica Quantità e Prezzo")
        btn_modify.clicked.connect(self.show_modifica_evento)
        h_layout.addWidget(btn_modify)

        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_tipo_evento() + " " + self.controller.get_data_evento())

    #Metodo che prende come parametri il testo di una informazione e il valore assegnato come sopra tramite il controller
    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    #Metodo che si occupa di eliminare l'evento
    def elimina_evento_click(self):
        reply = QMessageBox.question(self, "Conferma", "Sei sicuro di voler eliminare l'evento dal calendario?", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.elimina_evento(self.controller.get_id_evento())
            self.elimina_callback()
            self.close()
        else:
            return

    #Metodo che si occupa di aprire la VistaModificaEvento
    def show_modifica_evento(self):
        self.vista_modifica_evento = VistaModificaEvento(self.evento, self.update_evento)
        self.vista_modifica_evento.show()

    #Metodo che si occupa di aprire la VistaAggiungiQuantità
    def aggiungi_alle_attivita(self):
        self.vista_aggiungi_quantita = VistaAggiungiQuantita(self.evento, self.attivita)
        self.vista_aggiungi_quantita.show()
        self.close()

    #Metodo che si occupa di aggiornare prezzo e quantità nella view dell'evento
    def update_evento(self):

        self.label_quantita.setText("Quantità: {}".format(self.controller.get_quantita_disp()))




