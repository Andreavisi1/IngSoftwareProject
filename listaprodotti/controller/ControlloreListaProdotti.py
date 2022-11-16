from listaprodotti.model.ListaProdotti import ListaProdotti

"""
Gestisce e attua i comandi relativi alla lista dei prodotti
"""

class ControlloreListaProdotti():
    def __init__(self):
        super(ControlloreListaProdotti, self).__init__()
        self.model = ListaProdotti()

    def aggiungi_prodotto(self, prodotto):
        self.model.aggiungi_prodotto(prodotto)

    def get_lista_dei_prodotti(self):
        return self.model.get_lista_prodotti()

    def get_prodotto_by_index(self, index):
        return self.model.get_prodotto_by_index(index)

    def elimina_prodotto_by_id(self, id):
        self.model.rimuovi_prodotto_by_id(id)

    def save_data(self):
        self.model.save_data()

    def ritorna_quantita(self, id, quantita):
        self.model.ritorna_quantita(id, quantita)
