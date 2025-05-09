def ordena_nombre_asc_y_puntos_des(nombres:list,puntos:list)->list:

    for i in range(len(nombres) - 1):
        for j in range(i+1, len(nombres)):
            if nombres[i] > nombres[j]:

                temp_nombre = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = temp_nombre

                temp_puntos = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = temp_puntos

            elif nombres[i] == nombres[j]:
                if puntos[i] < puntos[j]:

                    temp_puntos = puntos[i]
                    puntos[i] = puntos[j]
                    puntos[j] = temp_puntos

    return nombres, puntos

nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos","Base de Datos", "Ergonomia", "Naturaleza"]
puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57]

print(ordena_nombre_asc_y_puntos_des(nombres,puntos))

