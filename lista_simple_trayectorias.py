from posicion import Posicion
from trayectoria_robot import Trayectoria_robot

class Lista_trayectorias():
    def __init__(self) -> None:
        self.inicio = None
        self.fin = None
        self.size =0
    

    def crear_terreno(self, nombre_terreno, posicion_inicial_x, posicion_inicial_y, posicion_final_x, posicion_final_y, cantidad_combustible):
        nueva_trayectoria = Trayectoria_robot(nombre_terreno, posicion_inicial_x, posicion_inicial_y, posicion_final_x, posicion_final_y, cantidad_combustible)
        self.size += 1

        if self.inicio is None:
            self.inicio = nueva_trayectoria
        
        else:
            trayectoria_temporal = self.inicio
            while trayectoria_temporal.siguiente is not None:
                trayectoria_temporal  = trayectoria_temporal.siguiente
            trayectoria_temporal.siguiente = nueva_trayectoria

    
    def get_terreno(self, nombre_terreno):
        trayectoria_temporal = self.inicio
        while trayectoria_temporal is not None:
            if trayectoria_temporal.nombre_terreno == nombre_terreno:
                return trayectoria_temporal
            trayectoria_temporal = trayectoria_temporal.siguiente
        return None


    def imprimir_terrenos(self):
        terreno_inicio = self.inicio
        while terreno_inicio is not None:
            print(terreno_inicio.nombre_terreno)
            terreno_inicio = terreno_inicio.siguiente
        return None


    def calcular_trayectoria(self):
        terreno_inicial = self.inicio
        while terreno_inicial is not None:
            print("Nombre del terreno: ", terreno_inicial.nombre_terreno)
            posicion_inicial_x = terreno_inicial.posicion_inicial_x
            posicion_inicial_y = terreno_inicial.posicion_inicial_y

            posicion_final_x = terreno_inicial.posicion_final_x
            posicion_final_y = terreno_inicial.posicion_final_y

            direccion_x = posicion_final_x - posicion_inicial_x
            direccion_y = posicion_final_y - posicion_inicial_y
            x = 0
            y = 0


            if (direccion_x < 0 or direccion_y < 0):
                x = -1
                y = -1

            elif (direccion_x > 0 or direccion_y > 0):
                x = 1
                y = 1

            elif (direccion_x < 0 or direccion_y > 0):
                x = -1
                y = 1
            
            elif (direccion_x > 0 or direccion_y < 0):
                x = 1
                y = -1

            elif (direccion_x < 0 or direccion_y == 0):
                x = -1
                y = 0
            
            elif (direccion_x == 0 or direccion_y < 0):
                x = 0
                y = -1
            
            elif (direccion_x == 0 or direccion_y > 0):
                x = 0
                y = 1
            
            elif (direccion_x == 0 or direccion_y == 0):
                x = 0
                y = 0



            posicion = terreno_inicial.lista_posiciones.get_posicion(posicion_inicial_x, posicion_inicial_y)
            posicion1 = posicion.siguiente
            posicion2 = terreno_inicial.lista_posiciones.get_posicion(posicion_inicial_x + x, posicion_inicial_y)

            print("Posición inicial x: ", posicion.posicion_x , "Posición inicial y: ", posicion.posicion_y)


            
            if posicion1.cantidad_combustible < posicion2.cantidad_combustible:
                print("Movimiento 1, x: ", posicion1.posicion_x, " y:", posicion1.posicion_y)
            terreno_inicial = terreno_inicial.siguiente
        return None

            
