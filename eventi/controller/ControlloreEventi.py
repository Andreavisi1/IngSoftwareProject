from eventi.model.Eventi import Eventi

"""
Classe che si occupa di interagire tra il model e le viste del eventi
"""
class ControlloreEventi():
    def __init__(self):
        super(ControlloreEventi, self).__init__()
        self.model = Carrello()

    def aggiungi_agli_eventi(self, evento):
        return self.model.aggiungi_al_carrello(evento)

    def rimuovi_acquisto_by_id(self, id):
        return self.model.rimuovi_acquisto_by_id(id)

    def get_acquisto_by_index(self, index):
        return self.model.get_acquisto_by_index(index)

    def get_lista_carrello(self):
        return self.model.get_lista_carrello()

    def save_data(self):
        self.model.save_data()

    def elimina_acquisto_by_id(self, id):
        self.model.rimuovi_acquisto_by_id(id)

    def verifica_quantita_prodotto(self, prodotto, quantita):
        return self.model.verifica_quantita_prodotto(prodotto, quantita)

    def verifica_presenza_prodotto_by_id(self, prodottoscelto):
        return self.model.verifica_presenza_prodotto_by_id(prodottoscelto)

    def clearall(self):
        self.model.clearall()
