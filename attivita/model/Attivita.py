import os
import pickle

"""
Gestisce i dati e le operazioni relative all'attivita
"""

class Attivita():
    def __init__(self):
        super(Attivita, self).__init__()

        self.attivita = []

        if os.path.isfile('attivita/data/attivita_salvata.pickle'):
            with open('attivita/data/attivita_salvata.pickle', 'rb') as f:
                self.attivita = pickle.load(f)

    def aggiungi_alle_attivita(self, evento):
        if self.verifica_presenza_evento_by_id(evento) is False:
            self.attivita.append(evento)


    def rimuovi_acquisto_by_id(self, id):
        def is_selected_acquisto(acquisto):
            if acquisto.id == id:
                return True
            return False
        self.attivita.remove(list(filter(is_selected_acquisto, self.attivita))[0])

    def clearall(self):
        self.attivita.clear()

    def get_acquisto_by_index(self, index):
        return self.attivita[index]

    def get_lista_attivita(self):
        return self.attivita

    def save_data(self):
        with open('attivita/data/attivita_salvata.pickle', 'wb') as handle:
            pickle.dump(self.attivita, handle, pickle.HIGHEST_PROTOCOL)

    def verifica_quantita_evento(self, evento, quantita):
        if quantita <= int(evento.quantita_magazzino):
            evento.quantita_attivita = quantita
            evento.quantita_magazzino = int(evento.quantita_magazzino) - evento.quantita_attivita
            return True
        return False

    def verifica_presenza_evento_by_id(self, eventoscelto):
        for(i, evento) in enumerate(self.attivita):
            if evento.id == eventoscelto.id:
                self.attivita[i].quantita_attivita = eventoscelto.quantita_attivita + self.attivita[i].quantita_attivita
                return True
        return False


