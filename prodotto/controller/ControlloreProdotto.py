"""
Gestisce e attua i comandi relativi al prodotto
"""
class ControlloreProdotto:
    def __init__(self, prodotto):
        self.model = prodotto

    def get_id_prodotto(self):
        return self.model.id

    def get_marca_prodotto(self):
        return self.model.marca

    def get_nome_prodotto(self):
        return self.model.nome

    def get_prezzo_prodotto(self):
        return self.model.prezzo

    def get_categoria_prodotto(self):
        return self.model.categoria

    def get_quantita_disp(self):
        return self.model.quantita_magazzino

    def get_quantita_carrello(self):
        return self.model.quantita_carrello