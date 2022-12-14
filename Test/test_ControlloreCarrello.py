from unittest import TestCase

from eventi.controller.ControlloreEventi import ControlloreCarrello
from prodotto.model.Prodotto import Prodotto


class TestControlloreCarrello(TestCase):
    def test_aggiungi_al_carrello(self):
        self.controller = ControlloreCarrello()
        self.prodotto = Prodotto("appleiphone", "Apple", "iPhone", "Telefonia", "699.99", "100", "01/01/2021")
        self.controller.aggiungi_al_carrello(self.prodotto)

    def test_get_lista_carrello(self):
        self.test_aggiungi_al_carrello()
        self.assertNotEqual(self.controller.get_lista_carrello(), [])

    def test_get_acquisto_by_index(self):
        self.test_aggiungi_al_carrello()
        self.assertTrue(self.controller.get_acquisto_by_index(0))



