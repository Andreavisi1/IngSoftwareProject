"""
Gestisce i dati e le operazioni relative al singolo evento
"""

class Evento:
    def __init__(self, id, tipo, titolo, categoria, luogo, data):
        super(Evento, self).__init__()
        self.id = id
        self.tipo = tipo
        self.titolo = titolo
        self.categoria = categoria
        self.luogo = luogo
        self.data = data






