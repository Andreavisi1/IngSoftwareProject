import os
import pickle

"""
La classe ListaProdotti gestisce i dati e le operazioni relative alla lista prodotti
"""

class ListaProdotti():
    def __init__(self):
        super(ListaProdotti, self).__init__()
        self.lista_prodotti = []
        if os.path.isfile('listaprodotti/data/lista_prodotti_salvata2.pickle'):
            with open('listaprodotti/data/lista_prodotti_salvata2.pickle', 'rb') as f:
                self.lista_prodotti = pickle.load(f)

    # Metodo che aggiunge il prodotto alla lista
    def aggiungi_prodotto(self, prodotto):
        self.lista_prodotti.append(prodotto)

    #Metodo che rimuove il prodotto dalla lista un volta effettuato il controllo sull'id
    def rimuovi_prodotto_by_id(self, id):
        def is_selected_prodotto(prodotto):
            if prodotto.id == id:
                return True
            return False
        self.lista_prodotti.remove(list(filter(is_selected_prodotto, self.lista_prodotti))[0])

    #Metodo che ritorna il prodotto dato l'indice
    def get_prodotto_by_index(self, index):
        return self.lista_prodotti[index]

    #Metodo che ritorna la lista_clienti
    def get_lista_prodotti(self):
        return self.lista_prodotti

    #La funzione si occupa di salvare eventuali modifiche dei dati nella lista_clienti
    def save_data(self):
        with open('listaprodotti/data/lista_prodotti_salvata2.pickle', 'wb') as handle:
            pickle.dump(self.lista_prodotti, handle, pickle.HIGHEST_PROTOCOL)

    #Metodo che fa ritornare la quantità di un singolo prodotto dal carrello al magazzino
    def ritorna_quantita(self, id, quantita):

        for prodotto in self.lista_prodotti:
            if prodotto.id == id:
                prodotto.quantita_magazzino += quantita
                prodotto.quantita_carrello = 0

        self.save_data()





