from lista_doble_posiciones import Lista_posiciones

class Trayectoria_robot():
    def __init__(self, nombre_terreno, posicion_inicial, posicion_final) -> None:
        self.nombre_terreno = nombre_terreno
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final
        self.lista_posiciones = Lista_posiciones()
        self.siguiente = None