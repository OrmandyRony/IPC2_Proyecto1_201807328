from lista_simple_trayectorias import Lista_trayectorias
import xml.etree.ElementTree as ET

cantidad_combustible = 9999

def indent(elem, level=0):                                                                                         
    i = "\n" + level*"  "                                                                                          
    j = "\n" + (level-1)*"  "                                                                                      
    if len(elem):                                                                                                  
        if not elem.text or not elem.text.strip():                                                                 
            elem.text = i + "  "                                                                                   
        if not elem.tail or not elem.tail.strip():                                                                 
            elem.tail = i                                                                                          
        for subelem in elem:                                                                                       
            indent(subelem, level+1)                                                                               
        if not elem.tail or not elem.tail.strip():                                                                 
            elem.tail = j                                                                                          
    else:                                                                                                          
        if level and (not elem.tail or not elem.tail.strip()):                                                     
            elem.tail = j                                                                                          
    return elem     

def cargar_archivo(ruta, trayectorias):
    tree = ET.parse(ruta)
    root = tree.getroot()
    posicion_sin_usar = True

    for terrenos in root:
        posicion_final_x = 0
        posicion_final_y = 0
        posicion_inicio_x = 0
        posicion_inicio_y = 0
        dimensionx = 0
        dimensiony  = 0 

        print('Terreno ', terrenos.attrib['nombre'], 'ha sido ingresado.')
        nombre_terreno = terrenos.attrib['nombre']


        for posicion_inicio in terrenos.iter('posicioninicio'):
            for posicion_x in posicion_inicio.iter('x'):
                posicion_inicio_x = int(posicion_x.text)

            for posicion_y in posicion_inicio.iter('y'):
                posicion_inicio_y = int(posicion_y.text)

        
        for posicion_final in terrenos.iter('posicionfin'):
            for posicion_x in posicion_final.iter('x'):
                posicion_final_x = int(posicion_x.text)

            for posicion_y in posicion_final.iter('y'):
                posicion_final_y = int(posicion_y.text)

        for dimension in terrenos.iter('dimension'):
            for dimension_x in dimension.iter('m'):
                dimensionx = int(dimension_x.text)

            for dimension_y in dimension.iter('n'):
                dimensiony  = int(dimension_y.text)

        trayectorias.crear_terreno(nombre_terreno, posicion_inicio_x, posicion_inicio_y, posicion_final_x, posicion_final_y, dimensionx, dimensiony, 9999)

        for posiciones in terrenos.iter('posicion'):
            terreno = trayectorias.get_terreno(terrenos.attrib['nombre'])
            posicion_x = int(posiciones.attrib['x'])
            posicion_y = int(posiciones.attrib['y'])
            cantidad_combustible = int(posiciones.text)
            terreno.lista_posiciones.insertar(posicion_x, posicion_y, cantidad_combustible, posicion_sin_usar,"|0|")
            #print('Se le asigno al terreno ',terrenos.attrib['nombre'], ' las coordenadas ', posiciones.attrib['x'], posiciones.attrib['y'],' y el combustible', posiciones.text)


"""
def calculo_trayectoria(trayectorias):
    # Algoritmo Dijskstra
    terreno = trayectorias.inicio
    
    while terreno is not None:
            print("Nombre del terreno: ", terreno.nombre_terreno)
            cantidad_combustible = 0
            terreno.posicion_2D = "|1|"
            posicion_inicial_x = terreno.posicion_inicial_x
            posicion_inicial_y = terreno.posicion_inicial_y
                              
            posicion_final_x = terreno.posicion_final_x
            posicion_final_y = terreno.posicion_final_y

            # Algoritmo Dijskstra

            posicion_temporal_x = posicion_inicial_x
            posicion_temporal_y = posicion_inicial_y

            
            posicion_inicial = terreno.lista_posiciones.get_posicion(posicion_inicial_x, posicion_inicial_y)
            # 1 y 2
            cantidad_combustible = posicion_inicial.cantidad_combustible
            
            while terreno.lista_posiciones.recorrido:
                



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
            
                posicion_1 = terreno.lista_posiciones.get_posicion(posicion_temporal_x + x, posicion_temporal_y)
                posicion_2 = terreno.lista_posiciones.get_posicion(posicion_temporal_x, movimiento_y)
                
                #print("Posición inicial x: ", posicion.posicion_x , "Posición inicial y: ", posicion.posicion_y)
                if posicion_1.posicion_sin_usar and posicion_2.posicion_sin_usar:

                    if posicion_1.cantidad_combustible < posicion_2.cantidad_combustible:
                        print("Movimiento x: ", posicion_1.posicion_x, " y: ", posicion_1.posicion_y)
                        cantidad_combustible += posicion_1.cantidad_combustible
                        posicion_temporal_x = posicion_1.posicion_x
                        posicion_temporal_y = posicion_1.posicion_y
                        posicion_1.posicion_2D = "|1|"
                        posicion_1.posicion_sin_usar = False
                    
                    else: 
                        print("Movimiento x: ", posicion_2.posicion_x, " y: ", posicion_2.posicion_y)
                        cantidad_combustible += posicion_2.cantidad_combustible
                        posicion_temporal_x = posicion_2.posicion_x
                        posicion_temporal_y = posicion_2.posicion_y
                        posicion_2.posicion_2D = "|1|"
                        posicion_2.posicion_sin_usar = False
                
                elif posicion_1.posicion_sin_usar:
                    print("Movimiento x: ", posicion_1.posicion_x, " y: ", posicion_1.posicion_y)
                    cantidad_combustible += posicion_1.cantidad_combustible
                    posicion_temporal_x = posicion_1.posicion_x
                    posicion_temporal_y = posicion_1.posicion_y
                    posicion_1.posicion_2D = "|1|"
                    posicion_1.posicion_sin_usar = False

                elif posicion_2.posicion_sin_usar:
                    print("Movimiento x: ", posicion_2.posicion_x, " y: ", posicion_2.posicion_y)
                    cantidad_combustible += posicion_2.cantidad_combustible
                    posicion_temporal_x = posicion_2.posicion_x
                    posicion_temporal_y = posicion_2.posicion_y
                    posicion_2.posicion_2D = "|1|"
                    posicion_2.posicion_sin_usar = False

                llego_al_destino = (posicion_final_x == posicion_temporal_x and posicion_final_y == posicion_temporal_y)
                if(llego_al_destino):
                    

            terreno = terreno.siguiente
"""


def calculo(trayectorias):
    terreno = trayectorias.inicio

    while terreno is not None:
        if not terreno.procesado:
            print("Nombre del terreno: ", terreno.nombre_terreno)
            terreno.posicion_2D = "|1|"
            posicion_inicial_x = terreno.posicion_inicial_x
            posicion_inicial_y = terreno.posicion_inicial_y
                                
            posicion_final_x = terreno.posicion_final_x
            posicion_final_y = terreno.posicion_final_y

            dimencion_x = terreno.dimension_x
            dimencion_y = terreno.dimension_y

            terreno.lista_posiciones.dijkstra(posicion_inicial_x, posicion_inicial_y, dimencion_x, dimencion_y)
            terreno.lista_posiciones.camino(posicion_final_x, posicion_final_y, posicion_inicial_x, posicion_inicial_y)
            
            grafica = terreno.lista_posiciones.mostrar_posiciones()
            dimension = terreno.dimension_x
            longitud = 3 * terreno.dimension_y

            #print(grafica)

            for i in range(1, dimension + 1):
                print(grafica[(i-1)*longitud:(i)*longitud])
            """
            grafica = terreno.lista_posiciones.mostrar_posiciones()
            dimension = terreno.dimension_y
            longitud = 3 * terreno.dimension_x
            #print(grafica)
            for i in range(1, dimension + 1):
                print(grafica[(i-1)*longitud:i*longitud])
            """
            print("")
            terreno.procesado = True
        terreno = terreno.siguiente
    

def calculo_trayectorias(trayectorias):
    terreno = trayectorias.inicio

    while terreno is not None:
            print("Nombre del terreno: ", terreno.nombre_terreno)
            cantidad_combustible = 0
            terreno.posicion_2D = "|1|"
            posicion_inicial_x = terreno.posicion_inicial_x
            posicion_inicial_y = terreno.posicion_inicial_y
                              
            posicion_final_x = terreno.posicion_final_x
            posicion_final_y = terreno.posicion_final_y

            posicion_temporal_x = posicion_inicial_x
            posicion_temporal_y = posicion_inicial_y

            llego_al_destino = (posicion_final_x == posicion_temporal_x and posicion_final_y == posicion_temporal_y)
            posicion_inicial = terreno.lista_posiciones.get_posicion(posicion_inicial_x, posicion_inicial_y)
            cantidad_combustible = posicion_inicial.cantidad_combustible

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
            
                posicion_1 = terreno.lista_posiciones.get_posicion(posicion_temporal_x + x, posicion_temporal_y)
                posicion_2 = terreno.lista_posiciones.get_posicion(posicion_temporal_x, movimiento_y)
                
                #print("Posición inicial x: ", posicion.posicion_x , "Posición inicial y: ", posicion.posicion_y)
                if posicion_1.posicion_sin_usar and posicion_2.posicion_sin_usar:

                    if posicion_1.cantidad_combustible < posicion_2.cantidad_combustible:
                        print("Movimiento x: ", posicion_1.posicion_x, " y: ", posicion_1.posicion_y)
                        cantidad_combustible += posicion_1.cantidad_combustible
                        posicion_temporal_x = posicion_1.posicion_x
                        posicion_temporal_y = posicion_1.posicion_y
                        posicion_1.posicion_2D = "|1|"
                        posicion_1.posicion_sin_usar = False
                    
                    else: 
                        print("Movimiento x: ", posicion_2.posicion_x, " y: ", posicion_2.posicion_y)
                        cantidad_combustible += posicion_2.cantidad_combustible
                        posicion_temporal_x = posicion_2.posicion_x
                        posicion_temporal_y = posicion_2.posicion_y
                        posicion_2.posicion_2D = "|1|"
                        posicion_2.posicion_sin_usar = False
                
                elif posicion_1.posicion_sin_usar:
                    print("Movimiento x: ", posicion_1.posicion_x, " y: ", posicion_1.posicion_y)
                    cantidad_combustible += posicion_1.cantidad_combustible
                    posicion_temporal_x = posicion_1.posicion_x
                    posicion_temporal_y = posicion_1.posicion_y
                    posicion_1.posicion_2D = "|1|"
                    posicion_1.posicion_sin_usar = False

                elif posicion_2.posicion_sin_usar:
                    print("Movimiento x: ", posicion_2.posicion_x, " y: ", posicion_2.posicion_y)
                    cantidad_combustible += posicion_2.cantidad_combustible
                    posicion_temporal_x = posicion_2.posicion_x
                    posicion_temporal_y = posicion_2.posicion_y
                    posicion_2.posicion_2D = "|1|"
                    posicion_2.posicion_sin_usar = False

                llego_al_destino = (posicion_final_x == posicion_temporal_x and posicion_final_y == posicion_temporal_y)
                if(llego_al_destino):
                    grafica = terreno.lista_posiciones.mostrar_posiciones()
                    dimension = terreno.dimension_y
                    longitud = 3 * terreno.dimension_x
                    #print(grafica)
                    for i in range(1, dimension + 1):
                        print(grafica[(i-1)*longitud:i*longitud])
                    print(cantidad_combustible ,"\n")

            terreno = terreno.siguiente




def escribir_archivo(ruta, terreno):

    
    terreno_escribir = ET.Element("terreno")
    posicion_inicial_x = terreno.posicion_inicial_x
    posicion_inicial_y = terreno.posicion_inicial_y
    #posicion = terreno.lista_posiciones.get_posicion(posicion_inicial_x, posicion_inicial_y)
    posiciones = terreno.lista_posiciones

    posicion_inicio = ET.SubElement(terreno_escribir, "posicioninicio")
    ET.SubElement(posicion_inicio, "x").text = str(terreno.posicion_inicial_x)
    ET.SubElement(posicion_inicio, "y").text = str(terreno.posicion_inicial_y)

    posicion_fin = ET.SubElement(terreno_escribir, "posicionfin")
    ET.SubElement(posicion_fin, "x").text = str(terreno.posicion_final_x)
    ET.SubElement(posicion_fin, "y").text = str(terreno.posicion_final_y)

    ET.SubElement(terreno_escribir, "combustible").text = str(posiciones.consumo_combustible_terreno)
    
    posicion = posiciones.inicio

    while posicion is not None:
        if posicion.posicion_2D == "|1|":
            ET.SubElement(terreno_escribir, "posicion", x = str(posicion.posicion_x), y = str(posicion.posicion_y)).text = "1"
        posicion = posicion.siguiente


        
    archivo1 = ET.ElementTree(terreno_escribir)
    archivo1.write(ruta)

def generar_grafica():
    pass

def mostrar_datos():
    print("""Rony Ormandy Ortíz Alvarez
201807328
Introducción a la Programación y Computación 2 sección \"B\"
Ingenieria en Ciencias y Sistemas
4to Semestre \n""")


def menu():
    print("")
    
    opcion = ''
    lista_trayectorias = Lista_trayectorias()
    print("""------------------------------ ROBOT R2E2 ------------------------------""")
    while opcion != '6':
        print("")
        print("""Menú principal:
1. Cargar archivo
2. Procesar archivo
3. Escribir archivo XML de salida 
4. Mostrar datos del estudiante
5. Generar gráfica
6. Salida
        """)

        opcion = input("Ingrese una opcion: ")

        if opcion == '1':
            filename = input("Ingrese el archivo: ")
            file = './' + filename
            cargar_archivo(file, lista_trayectorias)
        
        elif opcion == '2':
            # calculo_trayectorias(lista_trayectorias)
            #lista_trayectorias.calcular_trayectoria(lista_trayectorias)
            #print("Ejecuto la posicion 2")
            #procesar_archivo(lista_trayectorias)
            calculo(lista_trayectorias)
            lista_trayectorias.combustible_existente()
            print("Combustible existente: "+ str(lista_trayectorias.combustible) + " unidades")
        
        elif opcion == '3':
            print("Los nombres de los terrenos son: ")
            lista_trayectorias.imprimir_terrenos()
            nombre_terreno = input("Ingrese el nombre de uno de los terrenos: ")
            terreno = lista_trayectorias.get_terreno(nombre_terreno)
            
            ruta = input("Escriba la ruta: ")

            escribir_archivo(ruta, terreno)
        
        elif opcion == '4':
            mostrar_datos()
        
        elif opcion == '5':
            generar_grafica()
        
        elif opcion != '6':
            print("Opcion incorrecta\n")

if __name__ == '__main__':
    menu()