from unittest import TestCase

from cliente.model.Cliente import Cliente
from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti


class TestControlloreListaClienti(TestCase):

    def test_aggiungi_cliente(self):
        self.controller = ControlloreListaClienti()
        self.cliente = Cliente("mariorossi", "Mario", "Rossi", "RSSMRA66A02A271R", "via Roma 14", "mariorossi@outlook.it", "3458256745", "45")
        self.controller.aggiungi_cliente(self.cliente)

    def test_get_lista_dei_clienti(self):
        self.test_aggiungi_cliente()
        self.assertNotEqual(self.controller.get_lista_dei_clienti(), [])

    def test_get_cliente_by_index(self):
        self.test_aggiungi_cliente()
        self.assertTrue(self.controller.get_cliente_by_index(0))
