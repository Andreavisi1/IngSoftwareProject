"""
Gestisce i dati e le operazioni relative al tesserato
"""

class Tesserato:
       def __init__(self, id, nome, cognome, cf, email, telefono, luogo_nascita, eta, password, inizio_certificato, scadenza_certificato):
        super(Tesserato, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.email = email
        self.telefono = telefono
        self.luogo_nascita = luogo_nascita
        self.eta = eta
        self.password = password
        self.inizio_certificato = inizio_certificato
        self.scadenza_certificato = scadenza_certificato







