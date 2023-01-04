from statistichetesserati.model.StatsTesserati import StatsTesserati

"""
gestisce e attua il model della classe statistiche
"""
class ControlloreStatsTesserati():
    def __init__(self):
        super(ControlloreStatsTesserati, self).__init__()
        self.model = StatsTesserati()

    def save_data(self):
        self.model.save_data()

    def aggiungi_stat(self, acquisto):
        self.model.aggiungi_stat(acquisto)

    def get_lista_delle_stats(self):
        return self.model.get_lista_delle_stats()