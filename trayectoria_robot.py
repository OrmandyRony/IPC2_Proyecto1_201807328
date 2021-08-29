from lista_doble_posiciones import Lista_posiciones

class Trayectoria_robot():
    def __init__(self, nombre_terreno, posicion_inicial_x, posicion_inicial_y, posicion_final_x, posicion_final_y, dimension_x, dimension_y, cantidad_combustible) -> None:
        self.nombre_terreno = nombre_terreno

        self.posicion_inicial_x = posicion_inicial_x
        self.posicion_inicial_y = posicion_inicial_y

        self.posicion_final_y = posicion_final_y
        self.posicion_final_x = posicion_final_x

        self.dimension_x = dimension_x
        self.dimension_y = dimension_y
        self.cantidad_combustible = cantidad_combustible

        self.procesado = False
        
        self.lista_posiciones = Lista_posiciones()
        self.siguiente = None

    
    