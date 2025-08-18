import unittest
from src.jugador import Jugador
from src.excepciones import FichaInvalidaException

class TestJugador(unittest.TestCase):
    def test_creacion_jugador_valido_X(self):
        jugador = Jugador("colo", "X")
        self.assertEqual(jugador.obtener_nombre(), "colo")
        self.assertEqual(jugador.obtener_ficha(), "X")

    def test_creacion_jugador_valido_0(self):
        jugador = Jugador("Beto", "0")
        self.assertEqual(jugador.obtener_nombre(), "Beto")
        self.assertEqual(jugador.obtener_ficha(), "0")

    def test_creacion_jugador_invalido(self):
        with self.assertRaises(FichaInvalidaException):
            Jugador("manu", "O") 
        with self.assertRaises(FichaInvalidaException):
            Jugador("messi", "Z")  
        with self.assertRaises(FichaInvalidaException):
            Jugador("juampi", "")    

if __name__ == "__main__":
    unittest.main()
