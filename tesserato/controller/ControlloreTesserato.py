"""
Gestisce e attua i comandi relativi al tesserato
"""
class ControlloreTesserato:
    def __init__(self, tesserato):
        self.model = tesserato

    def get_id_tesserato(self):
        return self.model.id

    def get_nome_tesserato(self):
        return self.model.nome

    def get_cognome_tesserato(self):
        return self.model.cognome

    def get_cf_tesserato(self):
        return self.model.cf

    def get_indirizzo_tesserato(self):
        return self.model.indirizzo

    def get_email_tesserato(self):
        return self.model.email

    def get_telefono_tesserato(self):
        return self.model.telefono

    def get_eta_tesserato(self):
        return self.model.eta

    def get_password_tesserato(self):
        return self.model.password