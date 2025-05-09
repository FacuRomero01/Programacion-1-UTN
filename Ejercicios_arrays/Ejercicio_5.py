# Importo la función que nos devuelve el menor de los números
from Funciones import devuelve_menor_de_los_numeros_lista

def chequea_y_retorna_menores_edad(edades: list) -> list:
    # Guardo en la variable 'edad_minima' la edad mínima de la lista de edades utilizando la función importada 'devuelve_menor_de_los_numeros'
    edad_minima = devuelve_menor_de_los_numeros_lista(edades)

    # Lista vacía para almacenar los nombres de las personas con la edad mínima
    lista_nombres_menores_edad = []

    # Recorro la lista de edades
    for i in range(len(edades)):
        # Si encontramos una persona con la edad mínima, agregamos su nombre a la lista
        if edades[i] == edad_minima:
            lista_nombres_menores_edad = lista_nombres_menores_edad + [nombres[i]]

    # Retorno la lista con los nombres de las personas de menor edad
    return lista_nombres_menores_edad


# Defino las listas de nombres y edades de las personas
nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]

# Llamo a la función para obtener los nombres de las personas con la edad mínima
nombres_menores = chequea_y_retorna_menores_edad(edades)

# Obtengo la edad mínima de la lista de edades
edad_menores = devuelve_menor_de_los_numeros_lista(edades)

# Inicializo una cadena vacía para almacenar los nombres de las personas con la edad mínima
nombres_menores_str = ""

# Recorro la lista de nombres de las personas con la edad mínima
for i in range(len(nombres_menores)):
    # Si es el último nombre de la lista, solo lo agregamos sin coma ni "y"
    if i == len(nombres_menores) - 1:
        nombres_menores_str += nombres_menores[i]
    # Si es el penúltimo nombre, agregamos "y" para que se lea correctamente
    elif i == len(nombres_menores) - 2:
        nombres_menores_str += nombres_menores[i] + " y "
    # Para todos los demás nombres, agregamos una coma
    else:
        nombres_menores_str += nombres_menores[i] + ", "

# Compruebo si solo hay una persona de menor edad, y mostramos un mensaje adecuado
if len(nombres_menores) == 1:
    print(f"{nombres_menores_str} es la persona de menor edad con {edad_menores} años")
else:
    # Si hay más de una persona, mostramos un mensaje en plural
    print(f"{nombres_menores_str} son las personas de menor edad con {edad_menores} años")
