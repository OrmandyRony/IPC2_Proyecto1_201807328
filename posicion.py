class  Posicion():
    def __init__(self, posicion_x, posicion_y, cantidad_combustible, posicion_sin_usar) -> None:
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.cantidad_combustible = cantidad_combustible
        self.posicion_sin_usar = posicion_sin_usar
        self.siguiente = None
        self.anterior = None