from listas_personas import *
from Ejercicio_9 import *

def menu_startup():
    while True:
        print("\n~~~ MENU ~~~")
        print("1- Importar listas")
        print("2- Listar los datos de los usuarios de México")
        print("3- Listar los nombres, mails y teléfonos de los usuarios de Brasil")
        print("4- Listar los datos del/los usuario/s más joven/es")
        print("5- Obtener un promedio de edad de los usuarios")
        print("6- De los usuarios de Brasil, listar los datos del usuario de mayor edad")
        print("7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000")
        print("8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.")
        print("9- Cerrar programa")
        opcion = (input("\nIngrese una opción (1-9): "))

        if opcion == "1":
            importa_listas()
        elif opcion == "2":
            lista_datos_usuarios_mexico()
        elif opcion == "3":
            lista_nombre_mail_tel_usuarios_brasil()
        elif opcion == "4":
            lista_datos_usuarios_mas_jovenes()
        elif opcion == "5":
            promedia_edades()
        elif opcion == "6":
            lista_datos_mayor_edad_brasil()
        elif opcion == "7":
            lista_datos_brasil_mexico_con_postal_mayor_8000()
        elif opcion == "8":
            lista_datos_italianos_mayores_40()
        elif opcion == "9":
            print("\nSe cerró el menú\nFIN")
            break
        else:
            print("\nOpción inválida. Intentá de nuevo.")

        input("\nPresiona Enter para continuar...")

menu_startup()