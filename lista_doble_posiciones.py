from posicion import Posicion

class Lista_posiciones():
    def __init__(self) -> None:
        self.inicio = None
    
    def insertar(self, posicion_x, posicion_y, cantidad_combustible, posicion_sin_usar):
        nueva_posicion = Posicion(posicion_x, posicion_y, cantidad_combustible, posicion_sin_usar)

        if self.inicio is None:
            self.inicio = nueva_posicion
        else:
            temporal = self.inicio

            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nueva_posicion
            nueva_posicion.anterior = temporal
    
    def mostrar_posiciones(self):
        temporal = self.inicio
        while temporal is not None:
            print('Posicion X: ', temporal.posicion_x, 'Posicion Y: ', temporal.posicion_y)
            temporal = temporal.siguiente


    def get_posicion(self, posicionx, posiciony):
        posicion = self.inicio
        while posicion is not None:
            if posicionx == posicion.posicion_x and posiciony == posicion.posicion_y:
                return posicion
            posicion = posicion.siguiente
        return None
