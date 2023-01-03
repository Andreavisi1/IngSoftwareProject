from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from PyQt5 import QtGui
from tesserato.controller.ControlloreTesserato import ControlloreTesserato
from tesserato.views.VistaModificaTesserato import VistaModificaTesserato

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
        self.tesserato = tesserato
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))

        v_layout = QVBoxLayout()

        #Vengono recuperate le informazioni da mostrare a schermo
        self.label_nome = QLabel(self.controller.get_nome_tesserato() + " " + self.controller.get_cognome_tesserato())

        #Impostazioni per il font
        font_nome = self.label_nome.font()
        font_nome.setPointSize(30)
        self.label_nome.setFont(font_nome)
        v_layout.addWidget(self.label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Aggiunge tramite metodo get_label_info il titolo di una informazione e l'informazione stessa tramite controller
        self.label_id = self.get_label_info("Codice ID", self.controller.get_id_tesserato())
        self.label_cf = self.get_label_info("Codice Fiscale", self.controller.get_cf_tesserato())
        self.label_email = self.get_label_info("Email", self.controller.get_email_tesserato())
        self.label_telefono = self.get_label_info("Telefono", self.controller.get_telefono_tesserato())
        self.label_luogo_nascita = self.get_label_info("Luogo di nascita", self.controller.get_luogo_nascita_tesserato())
        self.label_eta = self.get_label_info("Età", self.controller.get_eta_tesserato())
        self.label_username = self.get_label_info("Username", self.controller.get_id_tesserato())
        self.label_password = self.get_label_info("Password", self.controller.get_password_tesserato())

      #  self.label_gare_partecipate = self.get_label_info("Gare partecipate", self.controller.get_gare_partecipate_tesserato())


        v_layout.addWidget(self.label_id)
        v_layout.addWidget(self.label_cf)
        v_layout.addWidget(self.label_email)
        v_layout.addWidget(self.label_telefono)
        v_layout.addWidget(self.label_luogo_nascita)
        v_layout.addWidget(self.label_eta)
        v_layout.addWidget(self.label_username)
        v_layout.addWidget(self.label_password)
     #   v_layout.addWidget(self.label_gare_partecipate)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.label_inizio_certificato = self.get_label_info("Certificato medico sportivo valido da", self.controller.get_inizio_certificato_tesserato())
        self.label_scadenza_certificato = self.get_label_info("Certificato medico sportivo valido fino a", self.controller.get_scadenza_certificato_tesserato())

        v_layout.addWidget(self.label_inizio_certificato)
        v_layout.addWidget(self.label_scadenza_certificato)


        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Bottone per modificare i dati di un tesserato
        btn_modify = QPushButton("Modifica")
        btn_modify.clicked.connect(self.show_modifica_tesserato)
        v_layout.addWidget(btn_modify)

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

#Metodo che si occupa di aprire la VistaModificaTesserato
    def show_modifica_tesserato(self):
        self.vista_modifica_tesserato = VistaModificaTesserato(self.tesserato, self.update_tesserato)
        self.vista_modifica_tesserato.show()

#Metodo che si occupa di eliminare il tesserato
    def elimina_tesserato_click(self):
        self.elimina_tesserato(self.controller.get_id_tesserato())
        self.elimina_callback()
        self.close()

#Metodo che si occupa di aggiornare i dati modificati del tesserato
    def update_tesserato(self):
        self.label_nome.setText("{}".format(self.controller.get_nome_tesserato() + " " + self.controller.get_cognome_tesserato()))
        self.label_id.setText("Codice ID: {}".format(self.controller.get_id_tesserato()))
        self.label_cf.setText("Codice Fiscale: {}".format(self.controller.get_cf_tesserato()))
        self.label_email.setText("Email: {}".format(self.controller.get_email_tesserato()))
        self.label_telefono.setText("Telefono: {}".format(self.controller.get_telefono_tesserato()))
        self.label_luogo_nascita.setText("Luogo di nascita: {}".format(self.controller.get_luogo_nascita_tesserato()))
        self.label_eta.setText("Età: {}".format(self.controller.get_eta_tesserato()))
        self.label_username.setText("Username: {}".format(self.controller.get_id_tesserato()))
        self.label_password.setText("Password: {}".format(self.controller.get_password_tesserato()))
        self.label_inizio_certificato.setText("Certificato medico sportivo valido da: {}".format(self.controller.get_inizio_certificato_tesserato()))
        self.label_scadenza_certificato.setText("Certificato medico sportivo valido fino a: {}".format(self.controller.get_scadenza_certificato_tesserato()))

   #     self.label_gare_partecipate.setText("Gare partecipate: {}".format(self.controller.get_gare_partecipate_tesserato()))