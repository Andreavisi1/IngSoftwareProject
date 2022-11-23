from listatesserati.model.ListaTesserati import ListaTesserati

"""
Gestisce e attua i comandi relativi alla lista dei tesserati
"""

class ControlloreListaTesserati():
    def __init__(self):
        super(ControlloreListaTesserati, self).__init__()
        self.model = ListaTesserati()

    def aggiungi_tesserato(self, tesserato):
        self.model.aggiungi_tesserato(tesserato)

    def get_lista_dei_tesserati(self):
        return self.model.get_lista_tesserati()

    def get_tesserato_by_index(self, index):
        return self.model.get_tesserato_by_index(index)

    def rimuovi_tesserato_by_id(self, id):
        self.model.rimuovi_tesserato_by_id(id)

    def save_data(self):
        self.model.save_data()
