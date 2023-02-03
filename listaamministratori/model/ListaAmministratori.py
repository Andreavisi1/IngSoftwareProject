import os
import pickle

"""
La classe ListaAmministratori gestisce i dati e le operazioni relative alla lista amministratori
"""

class ListaAmministratori():
    def __init__(self):
        super(ListaAmministratori, self).__init__()
        self.lista_amministratori = []
        if os.path.isfile('listaamministratori/data/lista_amministratori_salvata.pickle'):
            with open('listaamministratori/data/lista_amministratori_salvata.pickle', 'rb') as f:
                self.lista_amministratori = pickle.load(f)

    #Metodo che aggiunge l'amministratore alla lista
    def aggiungi_amministratore(self, amministratore):
        self.lista_amministratori.append(amministratore)

    #Metodo che rimuove l'amministratore dalla lista un volta effettuato il controllo sull'id
    def rimuovi_amministratore_by_id(self, id):
        def is_selected_amministratore(amministratore):
            if amministratore.id == id:
                return True
            return False
        self.lista_amministratori.remove(list(filter(is_selected_amministratore, self.lista_amministratori))[0])

    #Metodo che ritorna l'amministratore dato l'indice
    def get_amministratore_by_index(self, index):
        return self.lista_amministratori[index]

    # Metodo che ritorna l'amministratore dato lo username
    def get_amministratore_by_username(self, username):
        for amministratore in self.get_lista_amministratori():
            if amministratore.id == username:
                return amministratore

    #Metodo che ritorna la lista_amministratori
    def get_lista_amministratori(self):
        return self.lista_amministratori

    #La funzione si occupa di salvare eventuali modifiche dei dati nella lista_amministratori
    def save_data(self):
        with open('listaamministratori/data/lista_amministratori_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_amministratori, handle, pickle.HIGHEST_PROTOCOL)

    #Metodo che serve per verificare se id e password che vengono passati alla funzione siano identici
    def verifica_id_amministratore(self, id, password):
        for amministratore in self.lista_amministratori:
            if amministratore.id == id and amministratore.password == password:
                return True
        return False
