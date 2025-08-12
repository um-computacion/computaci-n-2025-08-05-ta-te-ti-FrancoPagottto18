import unittest
from src.tablero import Tablero, PosOcupadaException

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()

    def test_tablero_inicial_vacio(self):
        esperado = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]
        self.assertEqual(self.tablero.contenedor, esperado)

    def test_poner_ficha_correcta(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        self.assertEqual(self.tablero.contenedor[0][0], "X")

    def test_poner_ficha_ocupada(self):
        self.tablero.contenedor[1][1] = "O"
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(1, 1, "X")


if __name__ == "__main__":
    unittest.main()
