from unittest import TestCase

from listatesserati.controller.ControlloreListaTesserati import ControlloreListaTesserati
from tesserato.model.Tesserato import Tesserato


class TestControlloreListaTesserati(TestCase):

    def test_aggiungi_tesserato(self):
        self.controller = ControlloreListaTesserati()
        self.tesserato = Tesserato("mariorossi", "Mario", "Rossi", "RSSMRA66A02A271R", "mariorossi@outlook.it", "3458256745",
                                   "Ancona", "18", "rossirossi00", "Juniores", "15", "5", "01/01/2023", "01/01/2024")
        self.controller.aggiungi_tesserato(self.tesserato)

    def test_get_lista_dei_tesserati(self):
        self.test_aggiungi_tesserato()
        self.assertNotEqual(self.controller.get_lista_dei_tesserati(), [])

    def test_get_tesserato_by_index(self):
        self.test_aggiungi_tesserato()
        self.assertTrue(self.controller.get_tesserato_by_index(0))

