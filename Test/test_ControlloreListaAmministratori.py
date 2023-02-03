from unittest import TestCase

from amministratore.model.Amministratore import Amministratore
from listaamministratori.controller.ControlloreListaAmministratori import ControlloreListaAmministratori

class TestControlloreListaAmministratori(TestCase):

    def test_aggiungi_amministratore(self):
        self.controller = ControlloreListaAmministratori()
        self.amministratore = Amministratore("giuseppeverdi", "Giuseppe", "Verdi", "Dirigente", "VRDGPP13R10G337A", "Via Roma 14",
                                             "giuseppeverdi@outlook.it", "3458256745", "77", "Nabucco88")
        self.controller.aggiungi_amministratore(self.amministratore)

    def test_get_lista_degli_amministratori(self):
        self.test_aggiungi_amministratore()
        self.assertNotEqual(self.controller.get_lista_degli_amministratori(), [])

    def test_get_amministratore_by_index(self):
        self.test_aggiungi_amministratore()
        self.assertTrue(self.controller.get_amministratore_by_index(0))



