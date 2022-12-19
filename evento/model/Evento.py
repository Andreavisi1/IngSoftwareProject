"""
Gestisce i dati e le operazioni relative al singolo evento
"""


class Evento:
    def __init__(self, id, tipo, titolo, categoria, data, luogo, quantita_attivita, data_acquisto= None):
        super(Evento, self).__init__()
        self.id = id
        self.tipo = tipo
        self.titolo = titolo
        self.categoria = categoria
        self.data = data
        self.luogo = luogo

        """note/avvisi?"""

        self.quantita_attivita = quantita_attivita
        self.data_acquisto = data_acquisto





