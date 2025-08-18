from src.excepciones import PosOcupadaException

class Tablero:
    def __init__(self):
        self.contenedor = [["" for _ in range(3)] for _ in range(3)]

    def poner_la_ficha(self, fila, columna, ficha):
        if self.contenedor[fila][columna] == "":
            self.contenedor[fila][columna] = ficha
        else:
            raise PosOcupadaException("pos ocupada!")
