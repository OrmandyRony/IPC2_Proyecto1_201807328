from trayectoria_robot import Trayectoria_robot

class Lista_trayectorias():
    def __init__(self) -> None:
        self.inicio = None
        self.fin = None
        self.size =0
        self.combustible = 9999
    

    def crear_terreno(self, nombre_terreno, posicion_inicial_x, posicion_inicial_y, posicion_final_x, posicion_final_y, dimension_x, dimension_y, cantidad_combustible):
        nueva_trayectoria = Trayectoria_robot(nombre_terreno, posicion_inicial_x, posicion_inicial_y, posicion_final_x, posicion_final_y, dimension_x, dimension_y, cantidad_combustible)
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
        terreno = self.inicio
        contador = 1
        while terreno is not None:
            print(str(contador) + ". " + terreno.nombre_terreno)
            contador += 1
            terreno = terreno.siguiente
        return None

    def combustible_existente(self):
        trayectoria_temporal = self.inicio
        while trayectoria_temporal is not None:
            combustible_gastado = trayectoria_temporal.lista_posiciones.cantidad_combustible(trayectoria_temporal.posicion_final_x, trayectoria_temporal.posicion_final_y)
            self.combustible -= combustible_gastado
            trayectoria_temporal = trayectoria_temporal.siguiente
        return None
        

        



            
