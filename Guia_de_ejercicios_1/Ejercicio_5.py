
estadia_base = 15000
precio_final = 0

estacion = input("Ingrese la estación del año en la que desea viajar (verano/invierno/otoño/primavera): ").lower()

while(estacion != "verano" and estacion != "invierno" and estacion != "primavera" and estacion != "otoño"):
    estacion = input("Error! Ingrese una estación válida:" ).lower()

localidad = input("Ingrese la localidad de su viaje (bariloche/cataratas/cordoba/mar del plata): ").lower()

while (localidad != "bariloche" and localidad != "cordoba" and localidad != "cataratas" and localidad != "mar del plata"):
    localidad = input("Error! Ingrese una localidad válida:" ).lower()



if estacion == "invierno":
    if localidad == "bariloche":
        precio_final = estadia_base * 1.20
    elif localidad == "cataratas" or localidad == "cordoba":
        precio_final = estadia_base * 0.90
    else:
        precio_final = estadia_base * 0.80

elif estacion == "verano":
    if localidad == "bariloche":
        precio_final = estadia_base * 0.80
    elif localidad == "cataratas" or localidad == "cordoba":
        precio_final = estadia_base * 1.10
    else:
        precio_final = estadia_base * 1.20

else:
    if localidad == "bariloche" or localidad == "cataratas" or localidad == "mar del plata":
        precio_final = estadia_base * 1.10
    else:
        precio_final = estadia_base

print(precio_final)