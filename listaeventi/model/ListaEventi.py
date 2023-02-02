import os
import pickle

"""
La classe ListaEventi gestisce i dati e le operazioni relative alla lista eventi
"""

class ListaEventi():
    def __init__(self):
        super(ListaEventi, self).__init__()
        self.lista_eventi = []
        if os.path.isfile('listaeventi/data/lista_eventi_salvata2.pickle'):
            with open('listaeventi/data/lista_eventi_salvata2.pickle', 'rb') as f:
                self.lista_eventi = pickle.load(f)

    # Metodo che aggiunge l'evento alla lista
    def aggiungi_evento(self, evento):
        self.lista_eventi.append(evento)

    #Metodo che rimuove l'evento dalla lista un volta effettuato il controllo sull'id
    def rimuovi_evento_by_id(self, id):
        def is_selected_evento(evento):
            if evento.id == id:
                return True
            return False
        self.lista_eventi.remove(list(filter(is_selected_evento, self.lista_eventi))[0])

    #Metodo che ritorna l'evento dato l'indice
    def get_evento_by_index(self, index):
        return self.lista_eventi[index]

    #Metodo che ritorna la lista_eventi
    def get_lista_degli_eventi(self):
        return self.lista_eventi

    #La funzione si occupa di salvare eventuali modifiche dei dati nella lista_eventi
    def save_data(self):
        with open('listaeventi/data/lista_eventi_salvata2.pickle', 'wb') as handle:
            pickle.dump(self.lista_eventi, handle, pickle.HIGHEST_PROTOCOL)






