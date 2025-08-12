from src.tablero import Tablero
from src.jugador import Jugador
from src.exepciones import PosOcupadaException

class Tateti:
    def __init__(self):
        nombre1 = input("Nombre del jugador X: ")
        nombre2 = input("Nombre del jugador O: ")
        self.jugadores = [Jugador(nombre1, "X"), Jugador(nombre2, "O")]
        self.tablero = Tablero()
        self.turno = 0

    def mostrar_tablero(self):
        print("\nTablero:")
        for fila in self.tablero.contenedor:
            print(" | ".join([c if c else " " for c in fila]))
            print("-" * 9)

    def hay_ganador(self, simbolo):
        t = self.tablero.contenedor
        for i in range(3):
            if all([c == simbolo for c in t[i]]):
                return True
            if all([t[j][i] == simbolo for j in range(3)]):
                return True
        if all([t[i][i] == simbolo for i in range(3)]):
            return True
        if all([t[i][2 - i] == simbolo for i in range(3)]):
            return True
        return False

    def tablero_lleno(self):
        return all([c != "" for fila in self.tablero.contenedor for c in fila])

    def jugar(self):
        while True:
            self.mostrar_tablero()
            jugador = self.jugadores[self.turno % 2]
            print(f"Turno de {jugador}")
            try:
                fil = int(input("Ingrese fila (1-3): ")) - 1
                col = int(input("Ingrese columna (1-3): ")) - 1
                if not (0 <= fil < 3 and 0 <= col < 3):
                    print("¡Fila o columna fuera de rango! Deben ser valores entre 1 y 3.")
                    continue
                self.tablero.poner_la_ficha(fil, col, jugador.simbolo)
            except ValueError:
                print("Por favor, ingrese números válidos.")
                continue
            except PosOcupadaException as e:
                print(e)
                continue
            if self.hay_ganador(jugador.simbolo):
                self.mostrar_tablero()
                print(f"¡Felicidades! {jugador} ha ganado!")
                break
            if self.tablero_lleno():
                self.mostrar_tablero()
                print("¡Empate!")
                break
            self.turno += 1

if __name__ == "__main__":
    juego = Tateti()
    juego.jugar()