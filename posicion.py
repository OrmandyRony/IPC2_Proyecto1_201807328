class  Posicion():
    def __init__(self, posicion_x, posicion_y) -> None:
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.siguiente = None
        self.anterior = None