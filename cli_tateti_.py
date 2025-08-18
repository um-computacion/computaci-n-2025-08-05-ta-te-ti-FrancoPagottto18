from src.tateti import JuegoTaTeTi
from src.excepciones import JuegoTerminadoException
from src.tablero import PosOcupadaException

def mostrar_tablero(tablero):
    print("\nTablero:")
    for i, fila in enumerate(tablero.contenedor):
        print(" " + " | ".join(c if c != "" else " " for c in fila))
        if i < 2:
            print("---+---+---")

def pedir_coordenada(nombre, tipo):
    while True:
        try:
            valor = int(input(f"{nombre}, ingrese la {tipo} (1 a 3): "))
            if 1 <= valor <= 3:
                return valor - 1
            else:
                print("La coordenada debe estar entre 1 y 3.")
        except ValueError:
            print("Debes ingresar un número entero válido.")

def main():
    print("Bienvenidos al Ta Te Ti")
    nombre1 = input("Ingrese el nombre del jugador 1 (X): ")
    nombre2 = input("Ingrese el nombre del jugador 2 (O): ")
    juego = JuegoTaTeTi(nombre1, nombre2)

    while not juego.terminado:
        mostrar_tablero(juego.tablero)
        jugador = juego.turno
        print(f"Turno de {jugador.nombre} ({jugador.ficha})")
        fila = pedir_coordenada(jugador.nombre, "fila")
        columna = pedir_coordenada(jugador.nombre, "columna")
        try:
            juego.ocupar_casilla(fila, columna)
        except PosOcupadaException as e:
            print(e)
        except JuegoTerminadoException as e:
            print(e)
            break

    mostrar_tablero(juego.tablero)
    print("¡Gracias por jugar!")

if __name__ == "__main__":
    main() 