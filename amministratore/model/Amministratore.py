"""
Gestisce i dati e le operazioni relative all'amministratore
"""
class Amministratore:
    def __init__(self, id, nome, cognome, ruolo, cf, indirizzo, email, telefono, eta, password):
        super(Amministratore, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.ruolo = ruolo
        self.cf = cf
        self.indirizzo = indirizzo
        self.email = email
        self.telefono = telefono
        self.eta = eta
        self.password = password