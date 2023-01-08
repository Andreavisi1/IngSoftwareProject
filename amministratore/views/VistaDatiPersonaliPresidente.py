from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from PyQt5 import QtGui
from amministratore.views.VistaModificaAmministratore import VistaModificaAmministratore

"""
La classe VistaDatiPersonaliPresidente si occupa di mostrare a schermo le informazioni relative al presidente.
"""
class VistaDatiPersonaliPresidente(QWidget):
    def __init__(self, parent=None):
        super(VistaDatiPersonaliPresidente, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        v_layout = QVBoxLayout()

        #Impostazioni generali per titolo finestra
        self.label_nome = QLabel("Francesca Ubertini")
        font_nome = self.label_nome.font()
        font_nome.setPointSize(30)
        self.label_nome.setFont(font_nome)
        v_layout.addWidget(self.label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.label_1 = QLabel("''Mi chiami il presidente''")
        self.label_2 = QLabel("''È lei il presidente''")
        self.label_3 = QLabel("''Bene, allora so già tutto''")

        v_layout.addWidget(self.label_1)
        v_layout.addWidget(self.label_2)
        v_layout.addWidget(self.label_3)


        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.label_ruolo = QLabel("Ruolo: Presidente della società")
        self.label_username = QLabel("Username: pres")
        self.label_password = QLabel("Password: pres")

        v_layout.addWidget(self.label_ruolo)
        v_layout.addWidget(self.label_username)
        v_layout.addWidget(self.label_password)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(v_layout)
        self.setWindowTitle("Benvenuto, presidente")

    # Metodo che prende come parametri il testo di una informazione e il valore assegnato come sopra tramite il controller
    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    # Metodo che si occupa di aprire la VistaModificaAmministratore
    def show_modifica_amministratore(self):
        self.vista_modifica_amministratore = VistaModificaAmministratore(self.amministratore, self.update_amministratore)
        self.vista_modifica_amministratore.show()

#Metodo che si occupa di aggiornare i dati modificati dell'amministratore
    def update_amministratore(self):
        self.label_nome.setText("{}".format(self.controller.get_nome_amministratore() + " " + self.controller.get_cognome_amministratore()))
        self.label_ruolo.setText("Ruolo: {}".format(self.controller.get_ruolo_amministratore()))
        self.label_cf.setText("Codice Fiscale: {}".format(self.controller.get_cf_amministratore()))
        self.label_email.setText("Email: {}".format(self.controller.get_email_amministratore()))
        self.label_telefono.setText("Telefono: {}".format(self.controller.get_telefono_amministratore()))
        self.label_eta.setText("Età: {}".format(self.controller.get_eta_amministratore()))
        self.label_username.setText("Username: {}".format(self.controller.get_id_amministratore()))
        self.label_password.setText("Password: {}".format(self.controller.get_password_amministratore()))

