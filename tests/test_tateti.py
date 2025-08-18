import unittest
from src.tateti import JuegoTaTeTi
from src.excepciones import JuegoTerminadoException

class TestJuegoTaTeTi(unittest.TestCase):
    def setUp(self):
        self.juego = JuegoTaTeTi("A", "B")

    def test_turno_inicial(self):
        self.assertEqual(self.juego.turno.nombre, "A")
        self.assertEqual(self.juego.turno.ficha, "X")

    def test_cambiar_turno(self):
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.turno.nombre, "B")
        self.assertEqual(self.juego.turno.ficha, "0")

    def test_ganador_fila(self):
        self.juego.tablero.contenedor = [
            ["X", "X", "X"],
            ["", "", ""],
            ["", "", ""]
        ]
        self.assertTrue(self.juego.hay_ganador("X"))

    def test_ganador_columna(self):
        self.juego.tablero.contenedor = [
            ["0", "", ""],
            ["0", "", ""],
            ["0", "", ""]
        ]
        self.assertTrue(self.juego.hay_ganador("0"))

    def test_ganador_diagonal(self):
        self.juego.tablero.contenedor = [
            ["X", "", ""],
            ["", "X", ""],
            ["", "", "X"]
        ]
        self.assertTrue(self.juego.hay_ganador("X"))

    def test_empate(self):
        self.juego.tablero.contenedor = [
            ["X", "0", "X"],
            ["X", "0", "0"],
            ["0", "X", "X"]
        ]
        self.assertTrue(self.juego.tablero_lleno())
        self.assertFalse(self.juego.hay_ganador("X"))
        self.assertFalse(self.juego.hay_ganador("0"))

    def test_juego_terminado_exception(self):
        self.juego.terminado = True
        with self.assertRaises(JuegoTerminadoException):
            self.juego.ocupar_casilla(0, 0)

if __name__ == "__main__":
    unittest.main()