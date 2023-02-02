from unittest import TestCase

from evento.model.Evento import Evento
from listaeventi.controller.ControlloreListaEventi import ControlloreListaEventi

class TestControlloreListaEventi(TestCase):
    def test_aggiungi_alle_attivita(self):
        self.controller = ControlloreListaEventi()
        self.evento = Evento("eventotest", "Gara", "Finale regionale maschile", "Juniores", "Palaprometeo Ancona", "20/03/2023")
        self.controller.aggiungi_evento(self.evento)

    def test_get_lista_attivita(self):
        self.test_aggiungi_alle_attivita()
        self.assertNotEqual(self.controller.get_lista_degli_eventi(), [])

    def test_get_evento_by_index(self):
        self.test_aggiungi_alle_attivita()
        self.assertTrue(self.controller.get_evento_by_index(0))

