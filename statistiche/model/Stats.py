import os
import pickle

"""
gestisce i dati e le operazioni relative alle statistiche
"""

class Stats():
    def __init__(self):
        super(Stats, self).__init__()
        self.stats = []
        if os.path.isfile('statistiche/data/stats_salvate.pickle'):
            with open('statistiche/data/stats_salvate.pickle', 'rb') as f:
                self.stats = pickle.load(f)

    def save_data(self):
        with open('statistiche/data/stats_salvate.pickle', 'wb') as handle:
            pickle.dump(self.stats, handle, pickle.HIGHEST_PROTOCOL)

    def aggiungi_stat(self, acquisto):
        self.stats.append(acquisto)

    def get_lista_delle_stats(self):
        return self.stats
