from posicion import Posicion

class Lista_posiciones():
    def __init__(self) -> None:
        self.inicio = None
        self.tamano = 0
    
    def insertar(self, posicion_x, posicion_y, cantidad_combustible, posicion_sin_usar, posicion_2D):
        nueva_posicion = Posicion(posicion_x, posicion_y, cantidad_combustible, posicion_sin_usar, posicion_2D)
        self.tamano += 1

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
        grafica = ""
        while temporal is not None:
            grafica += temporal.posicion_2D
            temporal = temporal.siguiente
        grafica = grafica[::-1]
        return grafica


    def get_posicion(self, posicionx, posiciony):
        posicion = self.inicio
        while posicion is not None:
            if posicionx == posicion.posicion_x and posiciony == posicion.posicion_y:
                return posicion
            posicion = posicion.siguiente
        return None

    def recorrido(self):
        temporal = self.inicio
        contador = 0
        while temporal is not None:
            if not (temporal.posicion_sin_usar):
                contador += 1
            temporal = temporal.siguiente
        if contador == self.tamano:
            return False
        else: 
            return True

    def camino(self, posicion_final_x, posicion_final_y, posicion_inicial_x, posicion_inicial_y):
        posicion_final = self.get_posicion(posicion_final_x, posicion_final_y)
        posicion_inicial = self.get_posicion(posicion_inicial_x, posicion_inicial_y)
        posicion = posicion_final
        
        print(posicion_final.combutible)
        print(posicion_final.posicion_x, posicion_final.posicion_y)
        
        while posicion is not posicion_inicial:
            print(posicion.predecesor_x, posicion.predecesor_y)
            posicion = self.get_posicion(posicion.predecesor_x, posicion.predecesor_y)

        

    def costo_minimo(self):
        posicion = self.inicio
        minimo = float('inf')
        posicion_costo_menor = None
        while posicion is not None:
            if posicion.posicion_sin_usar:
                if minimo > posicion.combutible:
                    minimo = posicion.combutible
                    posicion_costo_menor = posicion
            posicion = posicion.siguiente
        return posicion_costo_menor
        

    def dijkstra(self, posicion_inicial_x, posicion_inicial_y, dimencion_x, dimencion_y):
        # 1 y 2
        posicion_inicial = self.get_posicion(posicion_inicial_x, posicion_inicial_y)
        posicion_inicial.combutible = posicion_inicial.cantidad_combustible
        posicion_actual = posicion_inicial

        while self.recorrido():
            # 3
            if posicion_actual != None:
            
                if posicion_actual.posicion_sin_usar:
                    # Nodos superiores
                    # 1, 1
                    if posicion_actual.posicion_x == 1 and posicion_actual.posicion_y == 1:
                        if posicion_actual.combutible + posicion_actual.siguiente.cantidad_combustible < posicion_actual.siguiente.combutible:
                            posicion_actual.siguiente.combutible = posicion_actual.combutible + posicion_actual.siguiente.cantidad_combustible
                            posicion_actual.siguiente.predecesor_x = posicion_actual.posicion_x
                            posicion_actual.siguiente.predecesor_y = posicion_actual.posicion_y
                        
                        posicion_abajo =self.get_posicion(posicion_actual.posicion_x + 1, posicion_actual.posicion_y)

                        if posicion_actual.combutible + posicion_abajo.cantidad_combustible < posicion_abajo.combutible:
                            posicion_abajo.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                            posicion_abajo.predecesor_x = posicion_actual.posicion_x
                            posicion_abajo.predecesor_y = posicion_actual.posicion_y
                    
                    
                    elif posicion_actual.posicion_x == 1 and posicion_actual.posicion_y == dimencion_y:
                        if posicion_actual.combutible + posicion_actual.anterior.cantidad_combustible < posicion_actual.anterior.combutible:
                            posicion_actual.anterior.combutible = posicion_actual.combutible + posicion_actual.anterior.cantidad_combustible
                            posicion_actual.anterior.predecesor_x = posicion_actual.posicion_x
                            posicion_actual.anterior.predecesor_y = posicion_actual.posicion_y
                        
                        posicion_abajo =self.get_posicion(posicion_actual.posicion_x + 1, posicion_actual.posicion_y)

                        if posicion_actual.combutible + posicion_abajo.cantidad_combustible < posicion_abajo.combutible:
                            posicion_abajo.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                            posicion_abajo.predecesor_x = posicion_actual.posicion_x
                            posicion_abajo.predecesor_y = posicion_actual.posicion_y


                    elif posicion_actual.posicion_x == dimencion_x and posicion_actual.posicion_y == 1:
                        if posicion_actual.combutible + posicion_actual.siguiente.cantidad_combustible < posicion_actual.siguiente.combutible:
                            posicion_actual.siguiente.combutible = posicion_actual.combutible + posicion_actual.siguiente.cantidad_combustible
                            posicion_actual.siguiente.predecesor_x = posicion_actual.posicion_x
                            posicion_actual.siguiente.predecesor_y = posicion_actual.posicion_y
                        
                        posicion_arriba =self.get_posicion(posicion_actual.posicion_x - 1, posicion_actual.posicion_y)

                        if posicion_actual.combutible + posicion_arriba.cantidad_combustible < posicion_arriba.combutible:
                            posicion_arriba.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                            posicion_arriba.predecesor_x = posicion_actual.posicion_x
                            posicion_arriba.predecesor_y = posicion_actual.posicion_y

                    elif posicion_actual.posicion_x == dimencion_x and posicion_actual.posicion_y == dimencion_y:
                        if posicion_actual.combutible + posicion_actual.anterior.cantidad_combustible < posicion_actual.anterior.combutible:
                            posicion_actual.anterior.combutible = posicion_actual.combutible + posicion_actual.anterior.cantidad_combustible
                            posicion_actual.anterior.predecesor_x = posicion_actual.posicion_x
                            posicion_actual.anterior.predecesor_y = posicion_actual.posicion_y

                        posicion_arriba =self.get_posicion(posicion_actual.posicion_x - 1, posicion_actual.posicion_y)

                        if posicion_actual.combutible + posicion_arriba.cantidad_combustible < posicion_arriba.combutible:
                            posicion_arriba.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                            posicion_arriba.predecesor_x = posicion_actual.posicion_x
                            posicion_arriba.predecesor_y = posicion_actual.posicion_y

                    # Nodo superior
                    elif (posicion_actual.posicion_x == 1 and (posicion_actual.posicion_y > 1 and posicion_actual.posicion_y < dimencion_y)):
                        if posicion_actual.combutible + posicion_actual.siguiente.cantidad_combustible < posicion_actual.siguiente.combutible:
                            posicion_actual.siguiente.combutible = posicion_actual.combutible + posicion_actual.siguiente.cantidad_combustible
                            posicion_actual.siguiente.predecesor_x = posicion_actual.posicion_x
                            posicion_actual.siguiente.predecesor_y = posicion_actual.posicion_y

                        posicion_abajo =self.get_posicion(posicion_actual.posicion_x + 1, posicion_actual.posicion_y)

                        if posicion_actual.combutible + posicion_abajo.cantidad_combustible < posicion_abajo.combutible:
                            posicion_abajo.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                            posicion_abajo.predecesor_x = posicion_actual.posicion_x
                            posicion_abajo.predecesor_y = posicion_actual.posicion_y

                        if posicion_actual.combutible + posicion_actual.anterior.cantidad_combustible < posicion_actual.anterior.combutible:
                            posicion_actual.anterior.combutible = posicion_actual.combutible + posicion_actual.anterior.cantidad_combustible
                            posicion_actual.anterior.predecesor_x = posicion_actual.posicion_x
                            posicion_actual.anterior.predecesor_y = posicion_actual.posicion_y

                    elif (posicion_actual.posicion_x == dimencion_x and (posicion_actual.posicion_y > 1 and posicion_actual.posicion_y < dimencion_y)):
                        if posicion_actual.combutible + posicion_actual.siguiente.cantidad_combustible < posicion_actual.siguiente.combutible:
                            posicion_actual.siguiente.combutible = posicion_actual.combutible + posicion_actual.siguiente.cantidad_combustible
                            posicion_actual.siguiente.predecesor_x = posicion_actual.posicion_x
                            posicion_actual.siguiente.predecesor_y = posicion_actual.posicion_y

                        posicion_arriba =self.get_posicion(posicion_actual.posicion_x - 1, posicion_actual.posicion_y)

                        if posicion_actual.combutible + posicion_arriba.cantidad_combustible < posicion_arriba.combutible:
                            posicion_arriba.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                            posicion_arriba.predecesor_x = posicion_actual.posicion_x
                            posicion_arriba.predecesor_y = posicion_actual.posicion_y

                        if posicion_actual.combutible + posicion_actual.anterior.cantidad_combustible < posicion_actual.anterior.combutible:
                            posicion_actual.anterior.combutible = posicion_actual.combutible + posicion_actual.anterior.cantidad_combustible
                            posicion_actual.anterior.predecesor_x = posicion_actual.posicion_x
                            posicion_actual.anterior.predecesor_y = posicion_actual.posicion_y
                    
                    elif (posicion_actual.posicion_y == 1 and (posicion_actual.posicion_x > 1 and posicion_actual.posicion_x < dimencion_x)):
                        if posicion_actual.combutible + posicion_actual.siguiente.cantidad_combustible < posicion_actual.siguiente.combutible:
                            posicion_actual.siguiente.combutible = posicion_actual.combutible + posicion_actual.siguiente.cantidad_combustible
                            posicion_actual.siguiente.predecesor_x = posicion_actual.posicion_x
                            posicion_actual.siguiente.predecesor_y = posicion_actual.posicion_y

                        posicion_abajo =self.get_posicion(posicion_actual.posicion_x + 1, posicion_actual.posicion_y)

                        if posicion_actual.combutible + posicion_abajo.cantidad_combustible < posicion_abajo.combutible:
                            posicion_abajo.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                            posicion_abajo.predecesor_x = posicion_actual.posicion_x
                            posicion_abajo.predecesor_y = posicion_actual.posicion_y

                        posicion_arriba =self.get_posicion(posicion_actual.posicion_x - 1, posicion_actual.posicion_y)

                        if posicion_actual.combutible + posicion_arriba.cantidad_combustible < posicion_arriba.combutible:
                            posicion_arriba.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                            posicion_arriba.predecesor_x = posicion_actual.posicion_x
                            posicion_arriba.predecesor_y = posicion_actual.posicion_y
                        
                    elif (posicion_actual.posicion_y == dimencion_y and (posicion_actual.posicion_x > 1 and posicion_actual.posicion_x < dimencion_x)):

                        posicion_abajo =self.get_posicion(posicion_actual.posicion_x + 1, posicion_actual.posicion_y)

                        if posicion_actual.combutible + posicion_abajo.cantidad_combustible < posicion_abajo.combutible:
                            posicion_abajo.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                            posicion_abajo.predecesor_x = posicion_actual.posicion_x
                            posicion_abajo.predecesor_y = posicion_actual.posicion_y

                        posicion_arriba =self.get_posicion(posicion_actual.posicion_x - 1, posicion_actual.posicion_y)

                        if posicion_actual.combutible + posicion_arriba.cantidad_combustible < posicion_arriba.combutible:
                            posicion_arriba.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                            posicion_arriba.predecesor_x = posicion_actual.posicion_x
                            posicion_arriba.predecesor_y = posicion_actual.posicion_y

                        if posicion_actual.combutible + posicion_actual.anterior.cantidad_combustible < posicion_actual.anterior.combutible:
                            posicion_actual.anterior.combutible = posicion_actual.combutible + posicion_actual.anterior.cantidad_combustible
                            posicion_actual.anterior.predecesor_x = posicion_actual.posicion_x
                            posicion_actual.anterior.predecesor_y = posicion_actual.posicion_y

                    else:
                        if posicion_actual.combutible + posicion_actual.siguiente.cantidad_combustible < posicion_actual.siguiente.combutible:
                            posicion_actual.siguiente.combutible = posicion_actual.combutible + posicion_actual.siguiente.cantidad_combustible
                            posicion_actual.siguiente.predecesor_x = posicion_actual.posicion_x
                            posicion_actual.siguiente.predecesor_y = posicion_actual.posicion_y

                        posicion_abajo =self.get_posicion(posicion_actual.posicion_x + 1, posicion_actual.posicion_y)

                        if posicion_actual.combutible + posicion_abajo.cantidad_combustible < posicion_abajo.combutible:
                            posicion_abajo.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                            posicion_abajo.predecesor_x = posicion_actual.posicion_x
                            posicion_abajo.predecesor_y = posicion_actual.posicion_y

                        posicion_arriba =self.get_posicion(posicion_actual.posicion_x - 1, posicion_actual.posicion_y)

                        if posicion_actual.combutible + posicion_arriba.cantidad_combustible < posicion_arriba.combutible:
                            posicion_arriba.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                            posicion_arriba.predecesor_x = posicion_actual.posicion_x
                            posicion_arriba.predecesor_y = posicion_actual.posicion_y

                        if posicion_actual.combutible + posicion_actual.anterior.cantidad_combustible < posicion_actual.anterior.combutible:
                            posicion_actual.anterior.combutible = posicion_actual.combutible + posicion_actual.anterior.cantidad_combustible
                            posicion_actual.anterior.predecesor_x = posicion_actual.posicion_x
                            posicion_actual.anterior.predecesor_y = posicion_actual.posicion_y

                    posicion_actual.posicion_sin_usar = False

                #5 y 6
                posicion_actual = self.costo_minimo()
                    
        """
                if posicion_actual.posicion_x == 1:
                    # 3.a
                    if posicion_actual.combutible + posicion_actual.siguiente.cantidad_combustible < posicion_actual.siguiente.combutible:
                        posicion_actual.siguiente.combutible = posicion_actual.combutible + posicion_actual.siguiente.cantidad_combustible
                        posicion_actual.siguiente.predecesor_x = posicion_actual.posicion_x
                        posicion_actual.siguiente.predecesor_y = posicion_actual.posicion_y
                    
                if posicion_actual.posicion_y == 1:
                    posicion_abajo =self.get_posicion(posicion_actual.posicion_x + 1, posicion_actual.posicion_y)

                    if posicion_actual.combutible + posicion_abajo.cantidad_combustible < posicion_abajo.combutible:
                        posicion_abajo.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                        posicion_abajo.predecesor_x = posicion_actual.posicion_x
                        posicion_abajo.predecesor_y = posicion_actual.posicion_y
                
                if posicion_actual.posicion_y == dimencion_y:
                    posicion_abajo =self.get_posicion(posicion_actual.posicion_x - 1, posicion_actual.posicion_y)

                    if posicion_actual.combutible + posicion_abajo.cantidad_combustible < posicion_abajo.combutible:
                        posicion_abajo.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                        posicion_abajo.predecesor_x = posicion_actual.posicion_x
                        posicion_abajo.predecesor_y = posicion_actual.posicion_y

                if posicion_actual.posicion_x == dimencion_x:
                    posicion_abajo =self.get_posicion(posicion_actual.posicion_x, posicion_actual.posicion_y -1 )

                    if posicion_actual.combutible + posicion_abajo.cantidad_combustible < posicion_abajo.combutible:
                        posicion_abajo.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                        posicion_abajo.predecesor_x = posicion_actual.posicion_x
                        posicion_abajo.predecesor_y = posicion_actual.posicion_y
                
                if (posicion_actual.posicion_x != dimencion_x and posicion_actual.posicion_y != dimencion_y and posicion_actual.posicion_y != 1 and posicion_actual.posicion_x != 1):
                    for i in range(0, 2):
                        for j in range(0,2):
                            posicion_abajo =self.get_posicion(posicion_actual.posicion_x + i, posicion_actual.posicion_y + j)

                            if posicion_actual.combutible + posicion_abajo.cantidad_combustible < posicion_abajo.combutible:
                                posicion_abajo.combutible = posicion_actual.combutible + posicion_abajo.cantidad_combustible
                                posicion_abajo.predecesor_x = posicion_actual.posicion_x
                                posicion_abajo.predecesor_y = posicion_actual.posicion_y
                    
            """
            #4

            
        
               
            