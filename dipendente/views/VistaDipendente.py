from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from PyQt5 import QtGui
from dipendente.controller.ControlloreDipendente import ControlloreDipendente
"""
La classe VistaDipendente si occupa di mostrare a schermo le informazioni relative al dipendente.
"""
class VistaDipendente(QWidget):
    def __init__(self, dipendente, elimina_dipendente, elimina_callback, parent=None):
        super(VistaDipendente, self).__init__(parent)
        self.controller = ControlloreDipendente(dipendente)
        self.elimina_dipendente = elimina_dipendente
        self.elimina_callback = elimina_callback
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))
        v_layout = QVBoxLayout()

        #Impostazioni generali per titolo finestra
        label_nome = QLabel(self.controller.get_nome_dipendente() + " " + self.controller.get_cognome_dipendente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Aggiunge tramite metodo get_label_info il titolo di una informazione e l'informazione stessa tramite controller
        v_layout.addWidget(self.get_label_info("Codice Fiscale", self.controller.get_cf_dipendente()))
        v_layout.addWidget(self.get_label_info("Indirizzo", self.controller.get_indirizzo_dipendente()))
        v_layout.addWidget(self.get_label_info("Email", self.controller.get_email_dipendente()))
        v_layout.addWidget(self.get_label_info("Telefono", self.controller.get_telefono_dipendente()))
        v_layout.addWidget(self.get_label_info("Età", self.controller.get_eta_dipendente()))
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        v_layout.addWidget(self.get_label_info("Username", self.controller.get_id_dipendente()))
        v_layout.addWidget(self.get_label_info("Password", self.controller.get_password_dipendente()))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Bottone per eliminare un dipendente
        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_dipendente_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_dipendente() + " " + self.controller.get_cognome_dipendente())

    # Metodo che prende come parametri il testo di una informazione e il valore assegnato come sopra tramite il controller
    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    # Metodo che si occupa di eliminare il dipendente
    def elimina_dipendente_click(self):
        self.elimina_dipendente(self.controller.get_id_dipendente())
        self.elimina_callback()
        self.close()


