def ordena_nombre_asc(nombres:list,edades:list):
    for i in range(len(nombres)-1):
        for j in range(i+1, len(nombres)):
            if nombres[i] > nombres[j]:

                temp_nombre = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = temp_nombre

                temp_edad = edades[i]
                edades[i] = edades[j]
                edades[j] = temp_edad


nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]


ordena_nombre_asc(nombres,edades)
print("{:<15} {:<20}".format("\nNombres", "Edades\n"))
for i in range(len(nombres)):
    print("{:<15} {:<20}".format(nombres[i], edades[i]))
