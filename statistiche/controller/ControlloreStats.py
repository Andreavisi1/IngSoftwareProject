from statistiche.model.Stats import Stats

"""
gestisce e attua il model della classe statistiche
"""
class ControlloreStats():
    def __init__(self):
        super(ControlloreStats, self).__init__()
        self.model = Stats()

    def save_data(self):
        self.model.save_data()

    def aggiungi_stat(self, acquisto):
        self.model.aggiungi_stat(acquisto)

    def get_lista_delle_stats(self):
        return self.model.get_lista_delle_stats()