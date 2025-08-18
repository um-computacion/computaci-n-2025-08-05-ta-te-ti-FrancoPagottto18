from src.excepciones import FichaInvalidaException
class Jugador:
    def __init__(self, nombre, ficha):
        if ficha not in ["X", "0"]:
            raise FichaInvalidaException("Ficha inválida. Debe ser 'X' o '0'")
        self.nombre = nombre
        self.ficha = ficha

    def obtener_nombre(self):
        return self.nombre

    def obtener_ficha(self):
        return self.ficha