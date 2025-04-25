cantidad_encuestados = 0
cantidad_empleados = 0
cant_promedio_empleados = 0
edad_mayor = None
nombre_mayor = ""
tecnologia_mayor = ""

for i in range(1,11):
    
    print(f"Encusta {i}: \n")
    nombre = input("Ingrese su nombre: ").lower()
    edad = int(input("Ingrese su edad (>18): "))
    while(edad < 18):
        edad = int(input("Error! Ingrese una edad válida (>18):" ))
    genero = input("Ingrese su género (Masculino - Femenino - Otro): ").lower()
    while(genero != "masculino" and genero != "femenino" and genero != "otro"):
        genero = input("Error! Ingrese un género válido: " ).lower()
    tecnologia = input("Ingrese la tecnología quiera trabajar (IA - RV/RA - IOT): ").lower()
    while(tecnologia != "ia" and tecnologia != "ra/rv" and tecnologia != "iot"):
        tecnologia = input("Error! Ingrese un género válido: " ).lower()
    print()

    if genero == "masculino":
        if (tecnologia == "iot" or tecnologia =="ia") and (edad > 25 and edad <= 50):
            cantidad_empleados += 1

        if edad_mayor == None or edad > edad_mayor:
            edad_mayor = edad
            nombre_mayor = nombre
            tecnologia_mayor = tecnologia

    if tecnologia != "ia":
        if genero != "femenino" or (edad > 33 and edad < 40):
            cant_promedio_empleados += 1
    
    cantidad_encuestados +=1

promedio = (cant_promedio_empleados/cantidad_encuestados)*100
print(f"La cantidad de empleados de género masculino que votaron por IOT o IA y estan dentro de los 25 a 50 años inclusive es de: {cantidad_empleados}")
print(f"El porcentaje de empleados que no votaron por IA y que no son ni femeninos o estén entre los 33 y 40 años es de: {promedio}%")
print(f"{nombre_mayor.capitalize()}, que votó por la tecnología {tecnologia_mayor.upper()} fue el mayor de los empleados masculinos en participar de la encuesta con la edad de {edad_mayor} año\n")