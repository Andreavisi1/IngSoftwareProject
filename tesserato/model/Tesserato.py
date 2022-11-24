"""
Gestisce i dati e le operazioni relative al tesserato
"""

class Tesserato:
       def __init__(self,id, nome, cognome, cf, indirizzo, email, telefono, eta, password):
        super(Tesserato, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.indirizzo = indirizzo
        self.email = email
        self.telefono = telefono
        self.eta = eta
        self.password = password







