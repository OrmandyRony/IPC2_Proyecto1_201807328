class  Posicion():
    def __init__(self, posicion_x, posicion_y, cantidad_combustible) -> None:
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.cantidad_combustible = cantidad_combustible
        self.siguiente = None
        self.anterior = None