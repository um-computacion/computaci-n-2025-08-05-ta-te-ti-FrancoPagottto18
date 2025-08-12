class Jugador:
    def __init__(self, nombre, simbolo):
        self.nombre = nombre
        self.simbolo = simbolo  # 'X' u 'O'

    def __str__(self):
        return f"{self.nombre} ({self.simbolo})" 