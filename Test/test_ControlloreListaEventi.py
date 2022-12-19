from unittest import TestCase

from listaeventi.controller.ControlloreListaEventi import ControlloreListaEventi
from evento.model.Evento import Evento


class TestControlloreListaEventi(TestCase):

    def test_aggiungi_evento(self):
        self.controller = ControlloreListaEventi()
        self.evento = Evento("appleiphone", "Apple", "iPhone", "Telefonia", "699.99", "100", "01/01/2021")
        self.controller.aggiungi_evento(self.evento)

    def test_get_lista_degli_eventi(self):
        self.test_aggiungi_evento()
        self.assertNotEqual(self.controller.get_lista_degli_eventi(), [])

    def test_get_evento_by_index(self):
        self.test_aggiungi_evento()
        self.assertTrue(self.controller.get_evento_by_index(0))
