from listas_personas import *
from Funciones import devuelve_menor_de_los_numeros_lista, promedia_lista_numeros, ordena_lista_asc

def importa_listas():
    from listas_personas import nombres,telefonos,mails,address,postalZip,region,country,edades
    print("\n¡Las listas fueron importadas con éxito!")
    return nombres,telefonos,mails,address,postalZip,region,country,edades

def lista_datos_usuarios_mexico(nombres:list,telefonos:list,mails:list,address:list,postalZip:list,region:list,country:list,edades:list):
    print("\nDatos de los usuarios de México:\n")
    print("{:<20} {:<20} {:<42} {:<40} {:<17} {:<32} {:<24} {:<20}".format("Nombre", "Teléfono", "Email", "Dirección", "Código postal", "Región", "País", "Edad\n"))
    for i in range(len(nombres)):
        if country[i].lower() == "mexico":
            print("{:<20} {:<20} {:<42} {:<40} {:<17} {:<32} {:<24} {:<20}".format(nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]))

def lista_nombre_mail_tel_usuarios_brasil(nombres:list,telefonos:list,mails:list,country:list):
    print("\nNombre, mail y teléfono de los usuarios de Brasil:\n")
    print("{:<20} {:<40} {:<20}".format("Nombre", "Email", "Teléfono\n"))
    for i in range(len(nombres)):
        if country[i].lower() == "brazil":
            print("{:<20} {:<40} {:<20}".format(nombres[i], mails[i], telefonos[i]))

def lista_datos_usuarios_mas_jovenes(nombres:list,telefonos:list,mails:list,address:list,postalZip:list,region:list,country:list,edades:list):
    menor_edad = devuelve_menor_de_los_numeros_lista(edades)
    print("\nDatos de los usuarios mas jovenes:\n")
    print("{:<20} {:<20} {:<42} {:<40} {:<17} {:<32} {:<24} {:<20}".format("Nombre", "Teléfono", "Email", "Dirección", "Código postal", "Región", "País", "Edad\n"))
    for i in range(len(nombres)):
        if edades[i] == menor_edad:
            print("{:<20} {:<20} {:<42} {:<40} {:<17} {:<32} {:<24} {:<20}".format(nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]))

def promedia_edades(edades):
    promedio_edades = int(promedia_lista_numeros(edades))
    print(f"\nEl promedio de edades de los usuarios es de {promedio_edades} años")

def lista_datos_mayor_edad_brasil(nombres:list,telefonos:list,mails:list,address:list,postalZip:list,region:list,country:list,edades:list):
    mayor_edad_brasil = -1
    indice_mayor_edad_brasil = -1
    for i in range(len(nombres)):
        if country[i].lower() == "brazil":
            if edades[i] > mayor_edad_brasil:
                mayor_edad_brasil = edades[i]
                indice_mayor_edad_brasil = i
    print("\nDatos del usuario de mayor edad de Brasíl:\n")
    print("{:<20} {:<20} {:<30} {:<40} {:<17} {:<12} {:<10} {:<17}".format("Nombre", "Teléfono", "Email", "Dirección", "Código postal", "Región", "País", "Edad\n"))
    if indice_mayor_edad_brasil != -1:
        print("{:<20} {:<20} {:<30} {:<40} {:<17} {:<12} {:<10} {:<17}".format(nombres[indice_mayor_edad_brasil], telefonos[indice_mayor_edad_brasil], mails[indice_mayor_edad_brasil], address[indice_mayor_edad_brasil], postalZip[indice_mayor_edad_brasil], region[indice_mayor_edad_brasil], country[indice_mayor_edad_brasil], edades[indice_mayor_edad_brasil]))

def lista_datos_brasil_mexico_con_postal_mayor_8000(nombres:list,telefonos:list,mails:list,address:list,postalZip:list,region:list,country:list,edades:list):
    print("\nDatos de los usuarios de Brasíl y Mexico con código postal mayor a 8000:\n")
    print("{:<20} {:<20} {:<42} {:<40} {:<17} {:<32} {:<24} {:<20}".format("Nombre", "Teléfono", "Email", "Dirección", "Código postal", "Región", "País", "Edad\n"))
    for i in range(len(nombres)):
        if country[i].lower() == "brazil" or country[i].lower() == "mexico":
            if postalZip[i] > 8000:
                print("{:<20} {:<20} {:<42} {:<40} {:<17} {:<32} {:<24} {:<20}".format(nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]))


def lista_datos_italianos_mayores_40(nombres:list,telefonos:list,mails:list,address:list,postalZip:list,region:list,country:list,edades:list):
    print("\nDatos de los usuarios italianos mayores de 40 años:\n")
    print("{:<20} {:<20} {:<30} {:<40} {:<17} {:<12} {:<10} {:<17}".format("Nombre", "Teléfono", "Email", "Dirección", "Código postal", "Región", "País", "Edad\n"))
    for i in range(len(nombres)):
        if country[i].lower() == "italy":
            if edades[i] > 40:
                print("{:<20} {:<20} {:<30} {:<40} {:<17} {:<12} {:<10} {:<17}".format(nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]))


def lista_nombre_mexicanos_ascendente(nombres:list,country:list):
    lista_nombres_mexicanos = []
    for i in range(len(nombres)):
        if country[i].lower() == "mexico":
            lista_nombres_mexicanos = lista_nombres_mexicanos + [nombres[i]]
    ordena_lista_asc(lista_nombres_mexicanos)
    print("\nNombres de los usuarios mexicanos ordenados alfabeticamente:\n")
    print("{:<20}".format("Nombre\n"))
    for i in range(len(lista_nombres_mexicanos)):
        print("{:<20}".format(lista_nombres_mexicanos[i]))

def ordena_datos_edad_asc():
    for i in range(len(nombres)-1):
        for j in range(i+1, len(nombres)):
            if edades[i] > edades[j]:

                aux = edades[i]
                edades[i] = edades[j]
                edades[j] = aux

                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux

                aux = telefonos[i]
                telefonos[i] = telefonos[j]
                telefonos[j] = aux

                aux = mails[i]
                mails[i] = mails[j]
                mails[j] = aux

                aux = address[i]
                address[i] = address[j]
                address[j] = aux

                aux = postalZip[i]
                postalZip[i] = postalZip[j]
                postalZip[j] = aux

                aux = region[i]
                region[i] = region[j]
                region[j] = aux

                aux = country[i]
                country[i] = country[j]
                country[j] = aux

            elif edades[i] == edades[j]:
                if nombres[i] > nombres[j]:
                    
                    aux = nombres[i]
                    nombres[i] = nombres[j]
                    nombres[j] = aux

                    aux = telefonos[i]
                    telefonos[i] = telefonos[j]
                    telefonos[j] = aux

                    aux = mails[i]
                    mails[i] = mails[j]
                    mails[j] = aux

                    aux = address[i]
                    address[i] = address[j]
                    address[j] = aux

                    aux = postalZip[i]
                    postalZip[i] = postalZip[j]
                    postalZip[j] = aux

                    aux = region[i]
                    region[i] = region[j]
                    region[j] = aux

                    aux = country[i]
                    country[i] = country[j]
                    country[j] = aux
    
def lista_datos_mas_jovenes_asc(nombres:list,telefonos:list,mails:list,address:list,postalZip:list,region:list,country:list,edades:list):
    menor_edad = devuelve_menor_de_los_numeros_lista(edades)
    print("\nDatos de los usuarios mas jovenes ordenados ascendentemente:\n")
    print("{:<20} {:<20} {:<42} {:<40} {:<17} {:<32} {:<24} {:<20}".format("Nombre", "Teléfono", "Email", "Dirección", "Código postal", "Región", "País", "Edad\n"))
    for i in range(len(nombres)):
        if menor_edad == edades[i]:
            print("{:<20} {:<20} {:<42} {:<40} {:<17} {:<32} {:<24} {:<20}".format(nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]))

def ordena_datos_edad_desc():
    for i in range(len(nombres)-1):
        for j in range(i+1, len(nombres)):
            if edades[i] < edades[j]:

                aux = edades[i]
                edades[i] = edades[j]
                edades[j] = aux

                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux

                aux = telefonos[i]
                telefonos[i] = telefonos[j]
                telefonos[j] = aux

                aux = mails[i]
                mails[i] = mails[j]
                mails[j] = aux

                aux = address[i]
                address[i] = address[j]
                address[j] = aux

                aux = postalZip[i]
                postalZip[i] = postalZip[j]
                postalZip[j] = aux

                aux = region[i]
                region[i] = region[j]
                region[j] = aux

                aux = country[i]
                country[i] = country[j]
                country[j] = aux

            elif edades[i] == edades[j]:
                if nombres[i] > nombres[j]:
                    
                    aux = nombres[i]
                    nombres[i] = nombres[j]
                    nombres[j] = aux

                    aux = telefonos[i]
                    telefonos[i] = telefonos[j]
                    telefonos[j] = aux

                    aux = mails[i]
                    mails[i] = mails[j]
                    mails[j] = aux

                    aux = address[i]
                    address[i] = address[j]
                    address[j] = aux

                    aux = postalZip[i]
                    postalZip[i] = postalZip[j]
                    postalZip[j] = aux

                    aux = region[i]
                    region[i] = region[j]
                    region[j] = aux

                    aux = country[i]
                    country[i] = country[j]
                    country[j] = aux

def ordena_datos_brasil_mexico_con_postal_mayor_8000_desc(nombres:list,telefonos:list,mails:list,address:list,postalZip:list,region:list,country:list,edades:list):
    for i in range(len(nombres)-1):
        for j in range(i+1, len(nombres)):
            if ((country[i].lower() == "brazil" or country[i].lower() == "mexico") and (country[j].lower() == "brazil" or country[j].lower() == "mexico") and postalZip[i] > 8000 and postalZip[j] > 8000):
                if nombres[i] < nombres[j] or (nombres[i] == nombres[j] and edades[i] < edades[j]):

                    aux = nombres[i]
                    nombres[i] = nombres[j]
                    nombres[j] = aux

                    aux = telefonos[i]
                    telefonos[i] = telefonos[j]
                    telefonos[j] = aux

                    aux = mails[i]
                    mails[i] = mails[j]
                    mails[j] = aux

                    aux = address[i]
                    address[i] = address[j]
                    address[j] = aux

                    aux = postalZip[i]
                    postalZip[i] = postalZip[j]
                    postalZip[j] = aux

                    aux = region[i]
                    region[i] = region[j]
                    region[j] = aux

                    aux = country[i]
                    country[i] = country[j]
                    country[j] = aux

                    aux = edades[i]
                    edades[i] = edades[j]
                    edades[j] = aux

def lista_datos_brasil_mexico_con_postal_mayor_8000_desc(nombres:list,telefonos:list,mails:list,address:list,postalZip:list,region:list,country:list,edades:list):
    ordena_datos_brasil_mexico_con_postal_mayor_8000_desc(nombres,telefonos,mails,address,postalZip,region,country,edades)
    print("\nDatos de los usuarios de Brasil y México con código postal mayor a 8000 ordenados descendentemente:\n")
    print("{:<20} {:<20} {:<42} {:<40} {:<17} {:<32} {:<24} {:<20}".format("Nombre", "Teléfono", "Email", "Dirección", "Código postal", "Región", "País", "Edad"))
    for i in range(len(nombres)):
        if (country[i].lower() == "brazil" or country[i].lower() == "mexico") and postalZip[i] > 8000:
            print("{:<20} {:<20} {:<42} {:<40} {:<17} {:<32} {:<24} {:<20}".format(nombres[i], telefonos[i], mails[i], address[i],postalZip[i], region[i], country[i], edades[i]))