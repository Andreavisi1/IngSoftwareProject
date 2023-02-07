from builtins import super

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox
from PyQt5 import QtGui
from tesserato.controller.ControlloreTesserato import ControlloreTesserato
from tesserato.views.VistaModificaDatiSportiviTesserato import VistaModificaDatiSportiviTesserato
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
        self.label_da = QLabel("Dati anagrafici")

        #Impostazioni per il font
        font_nome = self.label_nome.font()
        font_nome.setPointSize(30)
        font_nome.setBold(True)
        self.label_nome.setFont(font_nome)
        font_dati = self.label_da.font()
        font_dati.setPointSize(20)
        font_dati.setUnderline(True)
        self.label_da.setFont(font_dati)
        v_layout.addWidget(self.label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.label_da)

        #Aggiunge tramite metodo get_label_info il titolo di una informazione e l'informazione stessa tramite controller
        self.label_id = self.get_label_info("Codice ID", self.controller.get_id_tesserato())
        self.label_cf = self.get_label_info("Codice Fiscale", self.controller.get_cf_tesserato())
        self.label_email = self.get_label_info("Email", self.controller.get_email_tesserato())
        self.label_telefono = self.get_label_info("Telefono", self.controller.get_telefono_tesserato())
        self.label_luogo_nascita = self.get_label_info("Luogo di nascita", self.controller.get_luogo_nascita_tesserato())
        self.label_eta = self.get_label_info("Età", self.controller.get_eta_tesserato())
        self.label_username = self.get_label_info("Username", self.controller.get_id_tesserato())
        self.label_password = self.get_label_info("Password", self.controller.get_password_tesserato())

        v_layout.addWidget(self.label_id)
        v_layout.addWidget(self.label_cf)
        v_layout.addWidget(self.label_email)
        v_layout.addWidget(self.label_telefono)
        v_layout.addWidget(self.label_luogo_nascita)
        v_layout.addWidget(self.label_eta)
        v_layout.addWidget(self.label_username)
        v_layout.addWidget(self.label_password)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Impostazioni per il font
        self.label_ds = QLabel("Dati sportivi")
        self.label_ds.setFont(font_dati)
        v_layout.addWidget(self.label_ds)

        self.label_categoria = self.get_label_info("Categoria", self.controller.get_categoria_tesserato())
        self.label_gare_partecipate = self.get_label_info("Gare partecipate", self.controller.get_gare_partecipate_tesserato())
        self.label_gare_vinte = self.get_label_info("Gare vinte", self.controller.get_gare_vinte_tesserato())

        v_layout.addWidget(self.label_categoria)
        v_layout.addWidget(self.label_gare_partecipate)
        v_layout.addWidget(self.label_gare_vinte)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.label_inizio_certificato = self.get_label_info("Certificato medico sportivo valido da", self.controller.get_inizio_certificato_tesserato())
        self.label_scadenza_certificato = self.get_label_info("Certificato medico sportivo valido fino a", self.controller.get_scadenza_certificato_tesserato())

        v_layout.addWidget(self.label_inizio_certificato)
        v_layout.addWidget(self.label_scadenza_certificato)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Bottone per modificare i dati di un tesserato
        btn_modify = QPushButton("Modifica dati anagrafici")
        btn_modify.clicked.connect(self.show_modifica_da_tesserato)
        v_layout.addWidget(btn_modify)

        # Bottone per modificare i dati di un tesserato
        btn_modify = QPushButton("Modifica dati sportivi")
        btn_modify.clicked.connect(self.show_modifica_ds_tesserato)
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
    def show_modifica_da_tesserato(self):
        self.vista_modifica_tesserato = VistaModificaTesserato(self.tesserato, self.update_tesserato)
        self.vista_modifica_tesserato.show()

# Metodo che si occupa di aprire la VistaModificaDatiSportiviTesserato
    def show_modifica_ds_tesserato(self):
        self.vista_modifica_ds_tesserato = VistaModificaDatiSportiviTesserato(self.tesserato, self.update_tesserato)
        self.vista_modifica_ds_tesserato.show()

#Metodo che si occupa di eliminare il tesserato
    def elimina_tesserato_click(self):
        reply = QMessageBox.question(self, "Conferma", "Sei sicuro di voler eliminare il tesserato dalla lista?", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.elimina_tesserato(self.controller.get_id_tesserato())
            self.elimina_callback()
            self.close()
        else:
            return

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
        self.label_categoria.setText("Categoria: {}".format(self.controller.get_categoria_tesserato()))
        self.label_gare_partecipate.setText("Gare partecipate: {}".format(self.controller.get_gare_partecipate_tesserato()))
        self.label_gare_vinte.setText("Gare vinte: {}".format(self.controller.get_gare_vinte_tesserato()))
        self.label_inizio_certificato.setText("Certificato medico sportivo valido da: {}".format(self.controller.get_inizio_certificato_tesserato()))
        self.label_scadenza_certificato.setText("Certificato medico sportivo valido fino a: {}".format(self.controller.get_scadenza_certificato_tesserato()))