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

            posicion_temporal_x = posicion_inicial_x
            posicion_temporal_y = posicion_inicial_y

            llego_al_destino = (posicion_final_x == posicion_temporal_x and posicion_final_y == posicion_temporal_y)
            
            


            while not llego_al_destino:
                direccion_x = posicion_final_x - posicion_temporal_x
                direccion_y = posicion_final_y - posicion_temporal_y
                x = 0
                y = 0

                # Derecha, Arriba
                if (direccion_x > 0 and direccion_y > 0):
                    x = 1
                    y = 1

                # Izquierda, Arriba
                elif (direccion_x < 0 and direccion_y > 0):
                    x = -1
                    y = 1
                
                # Derecha, Abajo
                elif (direccion_x > 0 and direccion_y < 0):
                    x = 1
                    y = -1
                
                # Izquierda, Abajo
                elif (direccion_x < 0 and direccion_y > 0):
                    x = -1
                    y = -1

                # Derecha, Neutro
                elif (direccion_x > 0 and direccion_y == 0):
                    x = 1
                    y = 0

                # Izquierda, Neutro
                elif (direccion_x < 0 and direccion_y == 0):
                    x = -1
                    y = 0
                
                # Neutro, Arriba
                elif (direccion_x == 0 and direccion_y > 0):
                    x = 0
                    y = 1

                # Neutro, Abajo
                elif (direccion_x == 0 and direccion_y < 0):
                    x = 0
                    y = -1

                movimiento_y = posicion_temporal_y + y
            
                posicion_1 = terreno_inicial.lista_posiciones.get_posicion(posicion_temporal_x + x, posicion_temporal_y)
                posicion_2 = terreno_inicial.lista_posiciones.get_posicion(posicion_temporal_x, movimiento_y)
                
                #print("Posición inicial x: ", posicion.posicion_x , "Posición inicial y: ", posicion.posicion_y)
                if posicion_1.posicion_sin_usar and posicion_2.posicion_sin_usar:

                    if posicion_1.cantidad_combustible < posicion_2.cantidad_combustible:
                        print("Movimiento x: ", posicion_1.posicion_x, " y: ", posicion_1.posicion_y)
                        posicion_temporal_x = posicion_1.posicion_x
                        posicion_temporal_y = posicion_1.posicion_y
                        posicion_1.posicion_sin_usar = False
                    
                    else: 
                        print("Movimiento x: ", posicion_2.posicion_x, " y: ", posicion_2.posicion_y)
                        posicion_temporal_x = posicion_2.posicion_x
                        posicion_temporal_y = posicion_2.posicion_y
                        posicion_2.posicion_sin_usar = False
                
                elif posicion_1.posicion_sin_usar:
                    print("Movimiento x: ", posicion_1.posicion_x, " y: ", posicion_1.posicion_y)
                    posicion_temporal_x = posicion_1.posicion_x
                    posicion_temporal_y = posicion_1.posicion_y
                    posicion_1.posicion_sin_usar = False

                elif posicion_2.posicion_sin_usar:
                    print("Movimiento x: ", posicion_2.posicion_x, " y: ", posicion_2.posicion_y)
                    posicion_temporal_x = posicion_2.posicion_x
                    posicion_temporal_y = posicion_2.posicion_y
                    posicion_2.posicion_sin_usar = False

                
                llego_al_destino = (posicion_final_x == posicion_temporal_x and posicion_final_y == posicion_temporal_y)

            terreno_inicial = terreno_inicial.siguiente

        return None

            
