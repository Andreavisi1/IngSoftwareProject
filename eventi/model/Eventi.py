import os
import pickle

"""
Gestisce i dati e le operazioni relative al eventi
"""

class Carrello():
    def __init__(self):
        super(Carrello, self).__init__()

        self.carrello = []

        if os.path.isfile('eventi/data/evento_salvato.pickle'):
            with open('eventi/data/evento_salvato.pickle', 'rb') as f:
                self.carrello = pickle.load(f)

    def aggiungi_al_carrello(self, prodotto):
        if self.verifica_presenza_prodotto_by_id(prodotto) is False:
            self.carrello.append(prodotto)


    def rimuovi_acquisto_by_id(self, id):
        def is_selected_acquisto(acquisto):
            if acquisto.id == id:
                return True
            return False
        self.carrello.remove(list(filter(is_selected_acquisto, self.carrello))[0])

    def clearall(self):
        self.carrello.clear()

    def get_acquisto_by_index(self, index):
        return self.carrello[index]

    def get_lista_carrello(self):
        return self.carrello

    def save_data(self):
        with open('eventi/data/evento_salvato.pickle', 'wb') as handle:
            pickle.dump(self.carrello, handle, pickle.HIGHEST_PROTOCOL)

    def verifica_quantita_prodotto(self, prodotto, quantita):
        if quantita <= int(prodotto.quantita_magazzino):
            prodotto.quantita_carrello = quantita
            prodotto.quantita_magazzino = int(prodotto.quantita_magazzino) - prodotto.quantita_carrello
            return True
        return False

    def verifica_presenza_prodotto_by_id(self, prodottoscelto):

        for(i, prodotto) in enumerate(self.carrello):
            if prodotto.id == prodottoscelto.id:
                self.carrello[i].quantita_carrello = prodottoscelto.quantita_carrello + self.carrello[i].quantita_carrello
                return True
        return False


