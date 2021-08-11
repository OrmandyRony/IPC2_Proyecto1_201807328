from trayectoria_robot import Trayectoria_robot

class Lista_terrenos():
    def __init__(self) -> None:
        self.inicio = None
        self.fin = None
        self.size =0
    

    def crear_terreno(self, nombre_terreno, posicion_inicial, posicion_final):
        nueva_trayectoria = Trayectoria_robot(nombre_terreno, posicion_inicial, posicion_final)
        self.size += 1

        if self.inicio is None:
            self.inicio = nueva_trayectoria
        
        else:
            trayectoria_temporal = self.inicio
            while trayectoria_temporal.siguiente is not None:
                trayectoria_temporal  = trayectoria_temporal.siguiente
            trayectoria_temporal.siguiente = nueva_trayectoria
             
            
