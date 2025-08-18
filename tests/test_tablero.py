import unittest
from src.tablero import Tablero
from src.excepciones import PosOcupadaException

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()

    def test_tablero_vacio(self):
        for fila in self.tablero.contenedor:
            for casilla in fila:
                self.assertEqual(casilla, "")

    def test_poner_ficha(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        self.assertEqual(self.tablero.contenedor[0][0], "X")

    def test_pos_ocupada_exception(self):
        self.tablero.poner_la_ficha(1, 1, "X")
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(1, 1, "0")

if __name__ == "__main__":
    unittest.main()