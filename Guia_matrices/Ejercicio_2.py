from Ejercicio_1_3_4 import *

def menu_startup():
    flag_opcion_1 = False
    while True:
        print("\n~~~ MENU ~~~")
        print("1- Alta de productos (realice está opción primero, de lo contrario no funcionara el menú)")
        print("2- Baja de productos")
        print("3- Modificar productos")
        print("4- Listar productos")
        print("5- Lista de productos ordenados por nombre")
        print("6- Mostrar stock")
        print("7- Salir")
        opcion = (input("\nIngrese una opción (1-6): "))

        if opcion == "1":
            producto = input("Ingrese el producto que quiere dar de alta (en singular): ").capitalize()
            cantidad = int(input("Ingrese la cantidad de producto que ingresa: "))
            fila = int(input("Ingrese la fila en donde lo va a almacenar (entre 1 y 3 inclusives): "))
            while fila < 1 or fila > 4:
                fila = int(input("Ingrese una fila válida (entre 1 y 3 inclusives): "))
            columna = int(input("Ingrese la columna en donde lo va a almacenar (entre 1 y 5 inclusives): "))
            while columna < 1 or columna > 6:
                columna = int(input("ERROR! Ingrese una columna válida (entre 1 y 5 inclusives): "))
            agrega_nuevo_producto(stock,producto,cantidad,fila,columna)
            flag_opcion_1 = True
        
        elif opcion == "7":
            print("\nSe cerró el menú\nFIN")
            break

        elif not flag_opcion_1:
            print ("\nERROR! No hizo el alta de productos, ejecute la opción 1 del menú para continuar")
        elif opcion == "2":
            producto = input("Ingrese el producto que quiere dar de baja (en singular): ").capitalize()
            elimina_producto(stock, producto)
        elif opcion == "3":
            producto = input("Ingrese el producto que quiere modificar (en singular): ").capitalize()
            cantidad = int(input("Ingrese la cantidad del producto que modifica: "))
            fila = int(input("Ingrese la fila en donde lo va a mover (entre 1 y 3 inclusives): "))
            while fila < 1 or fila > 4:
                fila = int(input("Ingrese una fila válida (entre 1 y 3 inclusives): "))
            columna = int(input("Ingrese la columna en donde lo va a mover (entre 1 y 5 inclusives): "))
            while columna < 1 or columna > 6:
                columna = int(input("ERROR! Ingrese una columna válida (entre 1 y 5 inclusives): "))
            modifica_producto(stock,producto,cantidad,fila,columna)
        elif opcion == "4":
            lista_productos(stock)
        elif opcion == "5":
            lista_productos_por_nombre(stock)
        elif opcion == "6":
            mostrar_stock(stock)
        else:
            print("\nOpción inválida. Intentá de nuevo.")

        input("\nPresiona Enter para continuar...")

menu_startup()