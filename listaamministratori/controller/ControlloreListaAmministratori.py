from listaamministratori.model.ListaAmministratori import ListaAmministratori

"""
Gestisce e attua i comandi relativi alla lista degli amministratori
"""



class ControlloreListaAmministratori():
    def __init__(self):
        super(ControlloreListaAmministratori, self).__init__()
        self.model = ListaAmministratori()

    def aggiungi_amministratore(self, amministratore):
        self.model.aggiungi_amministratore(amministratore)

    def get_lista_degli_amministratori(self):
        return self.model.get_lista_amministratori()

    def get_amministratore_by_index(self, index):
        return self.model.get_amministratore_by_index(index)

    def elimina_amministratore_by_id(self, id):
        self.model.rimuovi_amministratore_by_id(id)

    def save_data(self):
        self.model.save_data()