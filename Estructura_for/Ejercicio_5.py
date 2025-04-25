cero_ingresado = False
suma = 0
promedio = 0
cantidad = 0

for i in range(10):
    if cero_ingresado == False:
        numero = int(input(f"Ingrese un número: "))
        if numero == 0:
            cero_ingresado = True
            print(f"Se cortó el ingreso de números")
        else:
            suma += numero
            cantidad += 1

if cantidad > 0:
    promedio = suma / cantidad #aca depende de si el 0 se cuenta para el promedio o no, en caso que si sería agregar (cantidad + 1) .
else:
    promedio = suma / 10

print(suma)
print(promedio)

