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

    def get_email_tesserato(self):
        return self.model.email

    def get_telefono_tesserato(self):
        return self.model.telefono

    def get_luogo_nascita_tesserato(self):
        return self.model.luogo_nascita

    def get_eta_tesserato(self):
        return self.model.eta

    def get_password_tesserato(self):
        return self.model.password

    def get_inizio_certificato_tesserato(self):
        return self.model.inizio_certificato

    def get_scadenza_certificato_tesserato(self):
        return self.model.scadenza_certificato