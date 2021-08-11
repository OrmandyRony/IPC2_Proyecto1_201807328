def cargar_archivo():
    pass


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
            cargar_archivo()
        
        elif opcion == '2':
            procesar_archivo()
        
        elif opcion == '3':
            escribir_archivo()
        
        elif opcion == '4':
            mostrar_datos()
        
        elif opcion == '5':
            generar_grafica()
        
        elif opcion != 6:
            print("Opcion incorrecta\n")

if __name__ == '__main__':
    menu()