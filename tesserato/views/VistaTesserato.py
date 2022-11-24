from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from PyQt5 import QtGui
from tesserato.controller.ControlloreTesserato import ControlloreTesserato

"""
La classe VistaTesserato apre una finestra a schermo che si occupa di mostrare all'utente le informazioni del tesserato.
La classe VistaTesserato estende la classe QWidget
"""


class VistaTesserato(QWidget):
    def __init__(self, tesserato, elimina_tesserato, elimina_callback, parent=None):
        super(VistaTesserato, self).__init__(parent)
        self.controller = ControlloreTesserato(tesserato)
        self.elimina_tesserato = elimina_tesserato
        self.elimina_callback = elimina_callback
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))

        v_layout = QVBoxLayout()

        #Vengono recuperate le informazioni da mostrare a schermo
        label_nome = QLabel(self.controller.get_nome_tesserato() + " " + self.controller.get_cognome_tesserato())

        #impostazioni per il font
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Aggiunge tramite metodo get_label_info il titolo di una informazione e l'informazione stessa tramite controller
        v_layout.addWidget(self.get_label_info("Codice ID", self.controller.get_id_tesserato()))
        v_layout.addWidget(self.get_label_info("Codice Fiscale", self.controller.get_cf_tesserato()))
        v_layout.addWidget(self.get_label_info("Indirizzo", self.controller.get_indirizzo_tesserato()))
        v_layout.addWidget(self.get_label_info("Email", self.controller.get_email_tesserato()))
        v_layout.addWidget(self.get_label_info("Telefono", self.controller.get_telefono_tesserato()))
        v_layout.addWidget(self.get_label_info("Età", self.controller.get_eta_tesserato()))
        v_layout.addWidget(self.get_label_info("Username", self.controller.get_id_tesserato()))
        v_layout.addWidget(self.get_label_info("Password", self.controller.get_password_tesserato()))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Bottone per eliminare un tesserato
        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_tesserato_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_tesserato() + " " + self.controller.get_cognome_tesserato())

    #Metodo che prende come parametri il testo di una informazione e il valore assegnato come sopra tramite il controller
    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    #Metodo che si occupa di eliminare il tesserato
    def elimina_tesserato_click(self):
        self.elimina_tesserato(self.controller.get_id_tesserato())
        self.elimina_callback()
        self.close()
