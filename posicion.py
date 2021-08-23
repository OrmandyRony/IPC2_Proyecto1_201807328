class  Posicion():
    def __init__(self, posicion_x, posicion_y, cantidad_combustible, posicion_sin_usar, posicion_2D) -> None:
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.cantidad_combustible = cantidad_combustible
        self.posicion_sin_usar = posicion_sin_usar
        self.posicion_2D = posicion_2D
        self.siguiente = None
        self.anterior = None