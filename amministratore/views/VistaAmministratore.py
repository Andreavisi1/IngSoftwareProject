from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox
from PyQt5 import QtGui
from amministratore.controller.ControlloreAmministratore import ControlloreAmministratore
from amministratore.views.VistaModificaAmministratore import VistaModificaAmministratore

"""
La classe VistaAmministratore si occupa di mostrare a schermo le informazioni relative all' amministratore.
"""
class VistaAmministratore(QWidget):
    def __init__(self, amministratore, elimina_amministratore, elimina_callback, parent=None):
        super(VistaAmministratore, self).__init__(parent)
        self.controller = ControlloreAmministratore(amministratore)
        self.elimina_amministratore = elimina_amministratore
        self.elimina_callback = elimina_callback
        self.amministratore = amministratore
        self.setWindowIcon(QtGui.QIcon('logos/logo A.S.D.F..png'))
        v_layout = QVBoxLayout()

        #Impostazioni generali per titolo finestra
        self.label_nome = QLabel(self.controller.get_nome_amministratore() + " " + self.controller.get_cognome_amministratore())
        font_nome = self.label_nome.font()
        font_nome.setPointSize(30)
        self.label_nome.setFont(font_nome)
        v_layout.addWidget(self.label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Aggiunge tramite metodo get_label_info il titolo di una informazione e l'informazione stessa tramite controller
        self.label_ruolo = self.get_label_info("Ruolo", self.controller.get_ruolo_amministratore())
        self.label_cf = self.get_label_info("Codice Fiscale", self.controller.get_cf_amministratore())
        self.label_indirizzo = self.get_label_info("Indirizzo", self.controller.get_indirizzo_amministratore())
        self.label_email = self.get_label_info("Email", self.controller.get_email_amministratore())
        self.label_telefono = self.get_label_info("Telefono", self.controller.get_telefono_amministratore())
        self.label_eta = self.get_label_info("Età", self.controller.get_eta_amministratore())
        self.label_username = self.get_label_info("Username", self.controller.get_id_amministratore())
        self.label_password = self.get_label_info("Password", self.controller.get_password_amministratore())

        v_layout.addWidget(self.label_ruolo)
        v_layout.addWidget(self.label_cf)
        v_layout.addWidget(self.label_indirizzo)
        v_layout.addWidget(self.label_email)
        v_layout.addWidget(self.label_telefono)
        v_layout.addWidget(self.label_eta)
        v_layout.addWidget(self.label_username)
        v_layout.addWidget(self.label_password)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Bottone per modificare i dati di un amministratore
        btn_modify = QPushButton("Modifica")
        btn_modify.clicked.connect(self.show_modifica_amministratore)
        v_layout.addWidget(btn_modify)

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

    # Metodo che si occupa di aprire la VistaModificaAmministratore
    def show_modifica_amministratore(self):
        self.vista_modifica_amministratore = VistaModificaAmministratore(self.amministratore, self.update_amministratore)
        self.vista_modifica_amministratore.show()

    # Metodo che si occupa di eliminare l'amministratore
    def elimina_amministratore_click(self):
        reply = QMessageBox.question(self, "Conferma", "Sei sicuro di voler eliminare l'amministratore dalla lista?", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.elimina_amministratore(self.controller.get_id_amministratore())
            self.elimina_callback()
            self.close()
        else:
            return


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

