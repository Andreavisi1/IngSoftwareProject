"""
Gestisce e attua i comandi relativi al singolo evento
"""
class ControlloreEvento:
    def __init__(self, evento):
        self.model = evento

    def get_id_evento(self):
        return self.model.id

    def get_tipo_evento(self):
        return self.model.tipo

    def get_titolo_evento(self):
        return self.model.titolo

    def get_categoria_evento(self):
        return self.model.categoria

    def get_data_evento(self):
        return self.model.data

    def get_luogo_evento(self):
        return self.model.luogo



    def get_quantita_disp(self):
        return self.model.quantita_attivita

    def get_quantita_attivita(self):
        return self.model.quantita_attivita