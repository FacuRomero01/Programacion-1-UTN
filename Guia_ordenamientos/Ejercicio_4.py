from Biblioteca_menu import *

def menu_startup():
    nombres = telefonos = mails = address = postalZip = region = country = edades = []
    flag_opcion_1 = False
    while True:
        print("\n~~~ MENU ~~~")
        print("1- Importar listas (realice está opción primero, de lo contrario no funcionara el menú)")
        print("2- Listar los datos de los usuarios de México")
        print("3- Listar los nombres, mails y teléfonos de los usuarios de Brasil")
        print("4- Listar los datos del/los usuario/s más joven/es")
        print("5- Obtener un promedio de edad de los usuarios")
        print("6- De los usuarios de Brasil, listar los datos del usuario de mayor edad")
        print("7- Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000")
        print("8- Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.")
        print("9- Listar los datos de los usuarios de México ordenados por nombre")
        print("10- Listar los datos del/los usuario/s más joven/es ordenados por edad de manera ascendente (Si la edad se repite, ordenar por nombre de manera ascendente")
        print("11- Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 ordenado por nombre y edad de manera descendente")
        print("12- Cerrar programa")
        opcion = (input("\nIngrese una opción (1-12): "))

        if opcion == "1":
            nombres,telefonos,mails,address,postalZip,region,country,edades = importa_listas()
            flag_opcion_1 = True
        
        elif opcion == "12":
            print("\nSe cerró el menú\nFIN")
            break

        elif not flag_opcion_1:
            print ("\nERROR! No importo las listas, ejecute la opción 1 del menú para continuar")
        elif opcion == "2":
            lista_datos_usuarios_mexico(nombres,telefonos,mails,address,postalZip,region,country,edades)
        elif opcion == "3":
            lista_nombre_mail_tel_usuarios_brasil(nombres,telefonos,mails,country)
        elif opcion == "4":
            lista_datos_usuarios_mas_jovenes(nombres,telefonos,mails,address,postalZip,region,country,edades)
        elif opcion == "5":
            promedia_edades(edades)
        elif opcion == "6":
            lista_datos_mayor_edad_brasil(nombres,telefonos,mails,address,postalZip,region,country,edades)
        elif opcion == "7":
            lista_datos_brasil_mexico_con_postal_mayor_8000(nombres,telefonos,mails,address,postalZip,region,country,edades)
        elif opcion == "8":
            lista_datos_italianos_mayores_40(nombres,telefonos,mails,address,postalZip,region,country,edades)
        elif opcion == "9":
            lista_nombre_mexicanos_ascendente(nombres,country)
        elif opcion == "10":
            lista_datos_mas_jovenes_asc(nombres,telefonos,mails,address,postalZip,region,country,edades)
        elif opcion == "11":
            lista_datos_brasil_mexico_con_postal_mayor_8000_desc(nombres,telefonos,mails,address,postalZip,region,country,edades)
        else:
            print("\nOpción inválida. Intentá de nuevo.")

        input("\nPresiona Enter para continuar...")

menu_startup()