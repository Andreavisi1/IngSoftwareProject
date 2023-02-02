from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PyQt5 import QtGui

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
        self.label_1.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel("''È lei il presidente''")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel("''Bene, allora so già tutto''")
        self.label_3.setAlignment(Qt.AlignCenter)

        v_layout.addWidget(self.label_1)
        v_layout.addWidget(self.label_2)
        v_layout.addWidget(self.label_3)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        font_nome.setPointSize(20)
        self.label_ruolo = QLabel("Ruolo: Presidente della società")
        self.label_ruolo.setFont(font_nome)
        self.label_username = QLabel("Username: pres")
        self.label_username.setFont(font_nome)
        self.label_password = QLabel("Password: pres")
        self.label_password.setFont(font_nome)

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


