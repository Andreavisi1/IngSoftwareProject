"""
Gestisce e attua i comandi relativi al dipendente
"""
class ControlloreDipendente:
    def __init__(self, dipendente):
        self.model = dipendente

    def get_id_dipendente(self):
        return self.model.id

    def get_nome_dipendente(self):
        return self.model.nome

    def get_cognome_dipendente(self):
        return self.model.cognome

    def get_cf_dipendente(self):
        return self.model.cf

    def get_indirizzo_dipendente(self):
        return self.model.indirizzo

    def get_email_dipendente(self):
        return self.model.email

    def get_telefono_dipendente(self):
        return self.model.telefono

    def get_eta_dipendente(self):
        return self.model.eta

    def get_password_dipendente(self):
        return self.model.password