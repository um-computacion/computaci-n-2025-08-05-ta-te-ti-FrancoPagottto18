from src.tablero import Tablero
from src.jugador import Jugador
from src.excepciones import JuegoTerminadoException

class JuegoTaTeTi:
    def __init__(self, nombre_jugador1="Jugador 1", nombre_jugador2="Jugador 2"):
        self.jugador1 = Jugador(nombre_jugador1, "X")
        self.jugador2 = Jugador(nombre_jugador2, "0")
        self.turno = self.jugador1
        self.tablero = Tablero()
        self.terminado = False

    def ocupar_casilla(self, fila, columna):
        if self.terminado:
            raise JuegoTerminadoException("El juego ya finalizo")
        ficha = self.turno.ficha
        self.tablero.poner_la_ficha(fila, columna, ficha)
        if self.hay_ganador(ficha):
            self.terminado = True
            print(f"El jugador {self.turno.nombre} ha ganado!")
            return
        if self.tablero_lleno():
            self.terminado = True
            print("El juego ha terminado en empate") 
            return
        self.cambiar_turno()

    def cambiar_turno(self):
        self.turno = self.jugador2 if self.turno == self.jugador1 else self.jugador1

    def turno_de_jugador(self, jugador):
        return self.turno == jugador

    def obtener_ficha_jugador(self, jugador):
        return jugador.ficha

    def hay_ganador(self, ficha):
        c = self.tablero.contenedor
        for fila in c:
            if fila == [ficha, ficha, ficha]:
                return True
        for i in range(3):
            if [c[0][i], c[1][i], c[2][i]] == [ficha, ficha, ficha]:
                return True
        if c[0][0] == c[1][1] == c[2][2] == ficha:
            return True
        if c[0][2] == c[1][1] == c[2][0] == ficha:
            return True
        return False

    def tablero_lleno(self):
        return all(casilla != "" for fila in self.tablero.contenedor for casilla in fila)
       