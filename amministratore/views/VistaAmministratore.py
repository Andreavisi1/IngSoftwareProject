from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from PyQt5 import QtGui
from amministratore.controller.ControlloreAmministratore import ControlloreAmministratore
"""
La classe VistaAmministratore si occupa di mostrare a schermo le informazioni relative all' amministratore.
"""
class VistaAmministratore(QWidget):
    def __init__(self, amministratore, elimina_amministratore, elimina_callback, parent=None):
        super(VistaAmministratore, self).__init__(parent)
        self.controller = ControlloreAmministratore(amministratore)
        self.elimina_amministratore = elimina_amministratore
        self.elimina_callback = elimina_callback
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        v_layout = QVBoxLayout()

        #Impostazioni generali per titolo finestra
        label_nome = QLabel(self.controller.get_nome_amministratore() + " " + self.controller.get_cognome_amministratore())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Aggiunge tramite metodo get_label_info il titolo di una informazione e l'informazione stessa tramite controller
        v_layout.addWidget(self.get_label_info("Codice Fiscale", self.controller.get_cf_amministratore()))
        v_layout.addWidget(self.get_label_info("Indirizzo", self.controller.get_indirizzo_amministratore()))
        v_layout.addWidget(self.get_label_info("Email", self.controller.get_email_amministratore()))
        v_layout.addWidget(self.get_label_info("Telefono", self.controller.get_telefono_amministratore()))
        v_layout.addWidget(self.get_label_info("Età", self.controller.get_eta_amministratore()))
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        v_layout.addWidget(self.get_label_info("Username", self.controller.get_id_amministratore()))
        v_layout.addWidget(self.get_label_info("Password", self.controller.get_password_amministratore()))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Bottone per eliminare un amministratore
        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_amministratore_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_amministratore() + " " + self.controller.get_cognome_amministratore())

    # Metodo che prende come parametri il testo di una informazione e il valore assegnato come sopra tramite il controller
    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    # Metodo che si occupa di eliminare l'amministratore
    def elimina_amministratore_click(self):
        self.elimina_amministratore(self.controller.get_id_amministratore())
        self.elimina_callback()
        self.close()


