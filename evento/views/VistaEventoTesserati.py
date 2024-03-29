from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, \
    QHBoxLayout
from evento.controller.ControlloreEvento import ControlloreEvento
from PyQt5 import QtGui

"""
La classe VistaEventoTesserati apre una finestra a schermo che si occupa di mostrare all'utente le informazioni dell'evento, ma senza le funzionalità specifiche degli amministratori
La classe VistaEventoTesserati estende la classe QWidget
"""

class VistaEventoTesserati(QWidget):
    def __init__(self, evento, elimina_evento, elimina_callback, parent=None):
        super(VistaEventoTesserati, self).__init__(parent)
        self.controller = ControlloreEvento(evento)
        self.elimina_evento = elimina_evento
        self.elimina_callback = elimina_callback
        self.evento = evento

        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        #Vengono recuperate le informazioni da mostrare a schermo
        self.label_nome = QLabel(self.controller.get_tipo_evento() + " " + self.controller.get_data_evento())
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        font_nome = self.label_nome.font()
        font_nome.setPointSize(30)
        self.label_nome.setFont(font_nome)
        v_layout.addWidget(self.label_nome)

        #Aggiunge tramite metodo get_label_info il titolo di una informazione e l'informazione stessa tramite controller
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.label_titolo = self.get_label_info("Titolo (opzionale)", self.controller.get_titolo_evento())
        self.label_categoria = self.get_label_info("Categoria", self.controller.get_categoria_evento())
        self.label_luogo = self.get_label_info("Luogo", self.controller.get_luogo_evento())

        v_layout.addWidget(self.label_titolo)
        v_layout.addWidget(self.label_luogo)
        v_layout.addWidget(self.label_categoria)


        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

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

