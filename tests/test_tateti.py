import unittest
from unittest.mock import patch
from src.tateti import Tateti
from src.tablero import PosOcupadaException

class TestTateti(unittest.TestCase):

    @patch("builtins.input", side_effect=["Alice", "Bob"])
    def setUp(self, mock_input):
        # Simulamos que los nombres ingresados son "Alice" y "Bob"
        self.juego = Tateti()

    def test_hay_ganador_fila(self):
        self.juego.tablero.contenedor = [
            ["X", "X", "X"],
            ["", "", ""],
            ["", "", ""]
        ]
        self.assertTrue(self.juego.hay_ganador("X"))

    def test_hay_ganador_columna(self):
        self.juego.tablero.contenedor = [
            ["O", "", ""],
            ["O", "", ""],
            ["O", "", ""]
        ]
        self.assertTrue(self.juego.hay_ganador("O"))

    def test_hay_ganador_diagonal(self):
        self.juego.tablero.contenedor = [
            ["X", "", ""],
            ["", "X", ""],
            ["", "", "X"]
        ]
        self.assertTrue(self.juego.hay_ganador("X"))

    def test_tablero_lleno_true(self):
        self.juego.tablero.contenedor = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"]
        ]
        self.assertTrue(self.juego.tablero_lleno())

    def test_tablero_lleno_false(self):
        self.juego.tablero.contenedor = [
            ["X", "O", "X"],
            ["O", "", "O"],
            ["O", "X", "O"]
        ]
        self.assertFalse(self.juego.tablero_lleno())

    def test_poner_ficha_correcta(self):
        self.juego.tablero.poner_la_ficha(0, 0, "X")
        self.assertEqual(self.juego.tablero.contenedor[0][0], "X")

    def test_poner_ficha_ocupada(self):
        self.juego.tablero.contenedor[0][0] = "X"
        with self.assertRaises(PosOcupadaException):
            self.juego.tablero.poner_la_ficha(0, 0, "O")


if __name__ == "__main__":
    unittest.main()
