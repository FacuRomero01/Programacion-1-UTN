def ordena_nombre_apellido_asc_y_si_nombre_igual_des(estudiantes:list,apellidos:list,nota:list)->list:

    for i in range(len(estudiantes) - 1):
        for j in range(i+1, len(estudiantes)):
            if apellidos[i] > apellidos[j]:

                temp_apellidos = apellidos[i]
                apellidos[i] = apellidos[j]
                apellidos[j] = temp_apellidos
                
                temp_nombre = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = temp_nombre

                temp_nota = nota[i]
                nota[i] = nota[j]
                nota[j] = temp_nota

            elif apellidos[i] == apellidos[j]:
                if estudiantes[i] > estudiantes[j]:

                    temp_nombre = estudiantes[i]
                    estudiantes[i] = estudiantes[j]
                    estudiantes[j] = temp_nombre
                
                elif estudiantes[i] == estudiantes[j]:
                    if nota[i] < nota[j]:
                        temp_nota = nota[i]
                        nota[i] = nota[j]
                        nota[j] = temp_nota

estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

ordena_nombre_apellido_asc_y_si_nombre_igual_des(estudiantes,apellidos,nota)
print("{:<20} {:<20} {:<15}".format("\nEstudiantes", "Apellidos", "Nota\n"))
for i in range(len(estudiantes)):
    print("{:<20} {:<20} {:<15}".format(estudiantes[i], apellidos[i], nota[i]))