edad = int(input("Ingrese su edad: "))
estado_civil = input("Ingrese su estado civil: ")

if edad < 18 and estado_civil != "soltero":
    print("Es muy pequeño para NO ser soltero")