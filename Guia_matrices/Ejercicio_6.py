from Ejercicio_5_7_8 import *

def menu_startup():
    while True:
        print("\n~~~ MENU ~~~")
        print("1- Reponer mercadería")
        print("2- Vender mercadería")
        print("3- Listar inventario")
        print("4- Mostrar stock")
        print("5- Salir")
        opcion = (input("\nIngrese una opción (1-5): "))

        if opcion == "1":
            articulo = input("Ingrese el artículo el cual quiere reponer: ")
            cantidad = int(input("Ingrese la cantidad del artículo que va a reponer: "))
            repone_mercaderia(stock,articulo,cantidad)
        elif opcion == "2":
            articulo = input("Ingrese el artículo que quiere vender: ")
            cantidad = int(input("Ingrese la cantidad del artículo que quiere vender: "))
            vende_mercaderia(stock,articulo,cantidad)
        elif opcion == "3":
            lista_inventario(stock)
        elif opcion == "4":
            mostrar_stock(stock)
        elif opcion == "5":
            print("\nSe cerró el menú\nFIN")
            break
        else:
            print("\nOpción inválida. Intentá de nuevo.")

        input("\nPresiona Enter para continuar...")

menu_startup()