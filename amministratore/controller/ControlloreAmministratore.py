"""
Gestisce e attua i comandi relativi all' amministratore
"""
class ControlloreAmministratore:
    def __init__(self, amministratore):
        self.model = amministratore

    def get_id_amministratore(self):
        return self.model.id

    def get_nome_amministratore(self):
        return self.model.nome

    def get_cognome_amministratore(self):
        return self.model.cognome

    def get_ruolo_amministratore(self):
        return self.model.ruolo

    def get_cf_amministratore(self):
        return self.model.cf

    def get_indirizzo_amministratore(self):
        return self.model.indirizzo

    def get_email_amministratore(self):
        return self.model.email

    def get_telefono_amministratore(self):
        return self.model.telefono

    def get_eta_amministratore(self):
        return self.model.eta

    def get_password_amministratore(self):
        return self.model.password