from unittest import TestCase

from attivita.controller.ControlloreAttivita import ControlloreAttivita
from evento.model.Evento import Evento


class TestControlloreAttivita(TestCase):
    def test_aggiungi_alle_attivita(self):
        self.controller = ControlloreAttivita()
        self.evento = Evento("appleiphone", "Apple", "iPhone", "Telefonia", "699.99", "100", "01/01/2021")
        self.controller.aggiungi_alle_attivita(self.evento)

    def test_get_lista_attivita(self):
        self.test_aggiungi_alle_attivita()
        self.assertNotEqual(self.controller.get_lista_attivita(), [])

    def test_get_acquisto_by_index(self):
        self.test_aggiungi_alle_attivita()
        self.assertTrue(self.controller.get_acquisto_by_index(0))



