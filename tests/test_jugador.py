import unittest
from src.jugador import Jugador

class TestJugador(unittest.TestCase):

    def test_atributos(self):
        jugador = Jugador("Alice", "X")
        self.assertEqual(jugador.nombre, "Alice")
        self.assertEqual(jugador.simbolo, "X")

    def test_str(self):
        jugador = Jugador("Bob", "O")
        self.assertEqual(str(jugador), "Bob (O)")


if __name__ == "__main__":
    unittest.main()
