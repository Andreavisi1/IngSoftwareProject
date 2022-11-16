import os
import pickle

"""
La classe ListaClienti gestisce i dati e le operazioni relative alla lista clienti
"""

class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.lista_dipendenti = []
        if os.path.isfile('listadipendenti/data/lista_dipendenti_salvata.pickle'):
            with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'rb') as f:
                self.lista_dipendenti = pickle.load(f)

    #Metodo che aggiunge il dipendente alla lista
    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

    #Metodo che rimuove il dipendente dalla lista un volta effettuato il controllo sull'id
    def rimuovi_dipendente_by_id(self, id):
        def is_selected_dipendente(dipendente):
            if dipendente.id == id:
                return True
            return False
        self.lista_dipendenti.remove(list(filter(is_selected_dipendente, self.lista_dipendenti))[0])

    #Metodo che ritorna il dipendente dato l'indice
    def get_dipendente_by_index(self, index):
        return self.lista_dipendenti[index]

    #Metodo che ritorna la lista_dipendenti
    def get_lista_dipendenti(self):
        return self.lista_dipendenti

    #La funzione si occupa di salvare eventuali modifiche dei dati nella lista_dipendenti
    def save_data(self):
        with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_dipendenti, handle, pickle.HIGHEST_PROTOCOL)

    #Metodo che serve per verificare se id e password che vengono passati alla funzione siano identici
    def verifica_id_dipendente(self, id,password):
        for dipendente in self.lista_dipendenti:
            if dipendente.id == id and dipendente.password == password:
                return True
        return False
