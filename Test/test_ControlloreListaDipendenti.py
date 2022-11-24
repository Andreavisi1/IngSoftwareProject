from unittest import TestCase

from amministratore.model.Amministratore import Dipendente
from listaamministratori.controller.ControlloreListaAmministratori import ControlloreListaDipendenti


class TestControlloreListaDipendenti(TestCase):

    def test_aggiungi_dipendente(self):
        self.controller = ControlloreListaDipendenti()
        self.dipendente = Dipendente("paolobianchi", "Paolo", "Bianchi", "BNCPLO66A02A271R", "via Roma 14",
                               "paolobianchi@outlook.it", "3458256745", "45", "Paolino45")
        self.controller.aggiungi_dipendente(self.dipendente)


    def test_get_lista_dei_dipendenti(self):
        self.test_aggiungi_dipendente()
        self.assertNotEqual(self.controller.get_lista_dei_dipendenti(), [])

    def test_get_dipendente_by_index(self):
        self.test_aggiungi_dipendente()
        self.assertTrue(self.controller.get_dipendente_by_index(0))
