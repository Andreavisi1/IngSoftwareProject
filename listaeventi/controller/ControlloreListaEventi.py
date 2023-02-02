from listaeventi.model.ListaEventi import ListaEventi

"""
Gestisce e attua i comandi relativi alla lista degli eventi
"""

class ControlloreListaEventi():
    def __init__(self):
        super(ControlloreListaEventi, self).__init__()
        self.model = ListaEventi()

    def aggiungi_evento(self, evento):
        self.model.aggiungi_evento(evento)

    def get_lista_degli_eventi(self):
        return self.model.get_lista_degli_eventi()

    def get_evento_by_index(self, index):
        return self.model.get_evento_by_index(index)

    def elimina_evento_by_id(self, id):
        self.model.rimuovi_evento_by_id(id)

    def save_data(self):
        self.model.save_data()
