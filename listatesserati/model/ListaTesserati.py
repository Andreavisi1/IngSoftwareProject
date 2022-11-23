import os
import pickle

"""
La classe ListaTesserati gestisce i dati e le operazioni relative alla lista clienti
"""

class ListaTesserati():
    def __init__(self):
        super(ListaTesserati, self).__init__()
        self.lista_tesserati = []
        if os.path.isfile('listatesserati/data/lista_tesserati_salvata.pickle'):
            with open('listatesserati/data/lista_tesserati_salvata.pickle', 'rb') as f:
                self.lista_tesserati = pickle.load(f)

    #Metodo che aggiunge il tesserato alla lista
    def aggiungi_tesserato(self, tesserato):
        self.lista_tesserati.append(tesserato)

    #Metodo che rimuove il tesserato dalla lista un volta effettuato il controllo sull'id
    def rimuovi_tesserato_by_id(self, id):
        def is_selected_tesserato(tesserato):
            if tesserato.id == id:
                return True
            return False
        self.lista_tesserati.remove(list(filter(is_selected_tesserato, self.lista_tesserati))[0])

    #Metodo che ritorna il tesserato dato l'indice
    def get_tesserato_by_index(self, index):
        return self.lista_tesserati[index]

    #Metodo che ritorna la lista_tesserati
    def get_lista_tesserati(self):
        return self.lista_tesserati

    #La funzione si occupa di salvare eventuali modifiche dei dati nella lista_tesserati
    def save_data(self):
        with open('listatesserati/data/lista_tesserati_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_tesserati, handle, pickle.HIGHEST_PROTOCOL)