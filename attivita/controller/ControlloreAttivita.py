from attivita.model.Attivita import Attivita

"""
Classe che si occupa di interagire tra il model e le viste dell'attività
"""
class ControlloreAttivita():
    def __init__(self):
        super(ControlloreAttivita, self).__init__()
        self.model = Attivita()

    def aggiungi_alle_attivita(self, attivita):
        return self.model.aggiungi_alle_attivita(attivita)

    def rimuovi_acquisto_by_id(self, id):
        return self.model.rimuovi_acquisto_by_id(id)

    def get_acquisto_by_index(self, index):
        return self.model.get_acquisto_by_index(index)

    def get_lista_attivita(self):
        return self.model.get_lista_attivita()

    def save_data(self):
        self.model.save_data()

    def elimina_acquisto_by_id(self, id):
        self.model.rimuovi_acquisto_by_id(id)

    def verifica_quantita_evento(self, evento, quantita):
        return self.model.verifica_quantita_evento(evento, quantita)

    def verifica_presenza_evento_by_id(self, eventoscelto):
        return self.model.verifica_presenza_evento_by_id(eventoscelto)

    def clearall(self):
        self.model.clearall()
