# Importo la función que nos devuelve el menor de los números
from Funciones import devuelve_menor_de_los_numeros_lista

# Defino las variables "nombres" y "edades"

nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]

# Utilizo la funcion "devuelve_menor_de_los_numeros_lista" para buscar la menor edad dentro de la lista "edades" y al valor le asigno la variable "edad_minima"
edad_minima = devuelve_menor_de_los_numeros_lista(edades)

# Inicializo la variable "lista_nombres_menores_edad" para almacenar los nombres de las personas con la menor edad
lista_nombres_menores_edad = []

# Uso un bucle for para ir buscando a las personas
for i in range(len(edades)):    
    if edades[i] == edad_minima:
        lista_nombres_menores_edad = lista_nombres_menores_edad + [nombres[i]]

# Inicializo una cadena vacía para almacenar los nombres de las personas con la edad mínima
nombres_menores_str = ""

# Recorro la lista de nombres de las personas con la edad mínima
for i in range(len(lista_nombres_menores_edad)):
    # Si es el último nombre de la lista, solo lo agregamos sin coma ni "y"
    if i == len(lista_nombres_menores_edad) - 1:
        nombres_menores_str += lista_nombres_menores_edad[i]
    # Si es el penúltimo nombre, agregamos "y" para que se lea correctamente
    elif i == len(lista_nombres_menores_edad) - 2:
        nombres_menores_str += lista_nombres_menores_edad[i] + " y "
    # Para todos los demás nombres, agregamos una coma
    else:
        nombres_menores_str += lista_nombres_menores_edad[i] + ", "

# Compruebo si solo hay una persona de menor edad, y mostramos un mensaje adecuado
if len(lista_nombres_menores_edad) == 1:
    print(f"{nombres_menores_str} es la persona de menor edad con {edad_minima} años")
else:
    # Si hay más de una persona, mostramos un mensaje en plural
    print(f"{nombres_menores_str} son las personas de menor edad con {edad_minima} años")