import os
import pickle

"""
La classe ListaClienti gestisce i dati e le operazioni relative alla lista clienti
"""

class ListaClienti():
    def __init__(self):
        super(ListaClienti, self).__init__()
        self.lista_clienti = []
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti = pickle.load(f)

    #Metodo che aggiunge il cliente alla lista
    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)

    #Metodo che rimuove il cliente dalla lista un volta effettuato il controllo sull'id
    def rimuovi_cliente_by_id(self, id):
        def is_selected_cliente(cliente):
            if cliente.id == id:
                return True
            return False
        self.lista_clienti.remove(list(filter(is_selected_cliente, self.lista_clienti))[0])

    #Metodo che ritorna il cliente dato l'indice
    def get_cliente_by_index(self, index):
        return self.lista_clienti[index]

    #Metodo che ritorna la lista_clienti
    def get_lista_clienti(self):
        return self.lista_clienti

    #La funzione si occupa di salvare eventuali modifiche dei dati nella lista_clienti
    def save_data(self):
        with open('listaclienti/data/lista_clienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)