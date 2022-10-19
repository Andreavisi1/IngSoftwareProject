import os
import pickle

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QVBoxLayout
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from home.views.VistaHome import VistaHome
from home.views.VistaHomeDirettore import VistaHomeDirettore
from listadipendenti.model.ListaDipendenti import ListaDipendenti
import credenziali

"""
La classe VistaLogin si occupa di mostrare a schermo la finestra iniziale dove l'utente deve fare
l'accesso per poter entrare all'interno del programma
"""

class VistaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.resize(400, 120)
        self.setWindowIcon(QtGui.QIcon('logos/logo.png'))

        v_layout = QVBoxLayout()
        layout = QGridLayout()

        label_logo = QLabel(self)
        pixmap = QPixmap('logos/logo with text.png')
        label_logo.setPixmap(pixmap)
        label_logo.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(label_logo)

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Inserire Username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Inserire Password')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        v_layout.addLayout(layout)
        self.setLayout(v_layout)

    #Metodo che controlla se l'username e la password inserite siano corrette.
    #In seguito apre all'utente la relativa vista.
    def check_password(self):
        msg = QMessageBox()
        msg.setWindowTitle('Login')
        msg.setWindowIcon(QtGui.QIcon('logos/logo.png'))
        lista = ListaDipendenti()

        if lista.verifica_id_dipendente(self.lineEdit_username.text(), self.lineEdit_password.text()):
            self.dialog = VistaHome()
            msg.setText('Accesso alla pagina dei dipendenti')
            msg.exec_()
            self.dialog.show()
            self.close()

        elif self.lineEdit_username.text() == credenziali.username and self.lineEdit_password.text() == credenziali.password:
            self.dialog = VistaHomeDirettore()
            msg.setText('Accesso alla pagina del direttore')
            msg.exec_()
            self.dialog.show()
            self.close()

        else:
            msg.setText('ERRORE: Ricontrollare le credenziali')
            msg.exec_()

    #Metodo che rende possibile l'accesso sia tramite bottone che con "Invio" da tastiera
    def keyPressEvent(self, qKeyEvent):

        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            self.check_password()
        else:
            super().keyPressEvent(qKeyEvent)
