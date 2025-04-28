from listas_personas import *
from Funciones import devuelve_menor_de_los_numeros_lista, promedia_lista_numeros, devuelve_mayor_de_los_numeros_lista

def importa_listas():
    print("\n¡Las listas fueron importadas con éxito!")

def lista_datos_usuarios_mexico():
    print("\nDatos de los usuarios de México:\n")
    for i in range(len(nombres)):
        if country[i].lower() == "mexico":
            print(f"Nombre: {nombres[i]}")
            print(f"Teléfono: {telefonos[i]}")
            print(f"Email: {mails[i]}")
            print(f"Dirección: {address[i]}")
            print(f"Código Postal: {postalZip[i]}")
            print(f"Región: {region[i]}")
            print(f"País: {country[i]}")
            print(f"Edad: {edades[i]}")
            print("-" * 40)

def lista_nombre_mail_tel_usuarios_brasil():
    print("\nNombre, mail y teléfono de los usuarios de Brasil:\n")
    for i in range(len(nombres)):
        if country[i].lower() == "brazil":
            print(f"Nombre: {nombres[i]}")
            print(f"Teléfono: {telefonos[i]}")
            print(f"Email: {mails[i]}")
            print("-" * 40)

def lista_datos_usuarios_mas_jovenes():
    menor_edad = devuelve_menor_de_los_numeros_lista(edades)
    print("\nDatos de los usuarios mas jovenes:\n")
    for i in range(len(nombres)):
        if edades[i] == menor_edad:
            print(f"Nombre: {nombres[i]}")
            print(f"Teléfono: {telefonos[i]}")
            print(f"Email: {mails[i]}")
            print(f"Dirección: {address[i]}")
            print(f"Código Postal: {postalZip[i]}")
            print(f"Región: {region[i]}")
            print(f"País: {country[i]}")
            print(f"Edad: {edades[i]}")
            print("-" * 40)

def promedia_edades():
    promedio_edades = int(promedia_lista_numeros(edades))
    print(f"\nEl promedio de edades de los usuarios es de {promedio_edades} años")

def lista_datos_mayor_edad_brasil():
    print("\nDatos del usuario de mayor edad de Brasíl:\n")
    mayor_edad_brasil = -1
    indice_mayor_edad_brasil = -1
    for i in range(len(nombres)):
        if country[i].lower() == "brazil":
            if edades[i] > mayor_edad_brasil:
                mayor_edad_brasil = edades[i]
                indice_mayor_edad_brasil = i
    if indice_mayor_edad_brasil != -1:
        print(f"Nombre: {nombres[indice_mayor_edad_brasil]}")
        print(f"Teléfono: {telefonos[indice_mayor_edad_brasil]}")
        print(f"Email: {mails[indice_mayor_edad_brasil]}")
        print(f"Dirección: {address[indice_mayor_edad_brasil]}")
        print(f"Código Postal: {postalZip[indice_mayor_edad_brasil]}")
        print(f"Región: {region[indice_mayor_edad_brasil]}")
        print(f"País: {country[indice_mayor_edad_brasil]}")
        print(f"Edad: {edades[indice_mayor_edad_brasil]}")
        print("-" * 40)

def lista_datos_brasil_mexico_con_postal_mayor_8000():
    print("\nDatos de los usuarios de Brasíl y Mexico con código postal mayor a 8000:\n")
    for i in range(len(nombres)):
        if country[i].lower() == "brazil" or country[i].lower() == "mexico":
            if postalZip[i] > 8000:
                print(f"Nombre: {nombres[i]}")
                print(f"Teléfono: {telefonos[i]}")
                print(f"Email: {mails[i]}")
                print(f"Dirección: {address[i]}")
                print(f"Código Postal: {postalZip[i]}")
                print(f"Región: {region[i]}")
                print(f"País: {country[i]}")
                print(f"Edad: {edades[i]}")
                print("-" * 40)

def lista_datos_italianos_mayores_40():
    print("\nDatos de los usuarios italianos mayores de 40 años:\n")
    for i in range(len(nombres)):
        if country[i].lower() == "italy":
            if edades[i] > 40:
                print(f"Nombre: {nombres[i]}")
                print(f"Teléfono: {telefonos[i]}")
                print(f"Email: {mails[i]}")
                print(f"Dirección: {address[i]}")
                print(f"Código Postal: {postalZip[i]}")
                print(f"Región: {region[i]}")
                print(f"País: {country[i]}")
                print(f"Edad: {edades[i]}")
                print("-" * 40)

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