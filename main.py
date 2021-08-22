from lista_simple_trayectorias import Lista_trayectorias
import xml.etree.ElementTree as ET

def cargar_archivo(ruta, trayectorias):
    tree = ET.parse(ruta)
    root = tree.getroot()

    for terrenos in root:
        posicion_final_x = 0
        posicion_final_y = 0
        posicion_inicio_x = 0
        posicion_inicio_y = 0

        print('Terreno ', terrenos.attrib['nombre'], 'ha sido insertado.')
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


        trayectorias.crear_terreno(nombre_terreno, posicion_inicio_x, posicion_inicio_y, posicion_final_x, posicion_final_y, 9999)

        for posiciones in terrenos.iter('posicion'):
            terreno = trayectorias.get_terreno(terrenos.attrib['nombre'])
            terreno.lista_posiciones.insertar(int(posiciones.attrib['x']), int(posiciones.attrib['y']), int(posiciones.text))
            print('Se le asigno al terreno ',terrenos.attrib['nombre'], ' las coordenadas ', posiciones.attrib['x'], posiciones.attrib['y'],' y el combustible', posiciones.text)


def procesar_archivo():
    pass


def escribir_archivo():
    pass


def generar_grafica():
    pass

def mostrar_datos():
    print("""Rony Ormandy Ortíz Alvarez
201807328
Introducción a la Programación y Computación 2 sección \"B\"
Ingenieria en Ciencias y Sistemas
4to Semestre \n""")


def menu():
    opcion = ''
    lista_trayectorias = Lista_trayectorias()
    print("""------------------------------ ROBOT R2E2 ------------------------------""")
    while opcion != '6':
        print("""Menú principal:
1. Cargar archivo
2. Procesar archivo
3. Escribir archivo de salida
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
            lista_trayectorias.calcular_trayectoria()
            print("Ejecuto la posicion 2")
            #procesar_archivo()
        
        elif opcion == '3':
            escribir_archivo()
        
        elif opcion == '4':
            mostrar_datos()
        
        elif opcion == '5':
            generar_grafica()
        
        elif opcion != '6':
            print("Opcion incorrecta\n")

if __name__ == '__main__':
    menu()