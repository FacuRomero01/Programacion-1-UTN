
pares = 0
impares = 0
menor_numero_ingresado = None
mayor_par_ingresado = None
suma_positivos = 0
producto_negativos = 1
hay_negativos = False
hay_pares = False


for i in range(5):
    numero = int(input(f"ingrese el número {i+1} (distinto de cero): "))

    while numero == 0:
        numero = int(input(f"Error! Ingrese un número válido: "))

    # a. cantidad de pares e impares
    if numero % 2 == 0:
        pares += 1
        #c. de los pares el mayor numero ingresado
        if mayor_par_ingresado == None or numero > mayor_par_ingresado:
            mayor_par_ingresado = numero
    else:
        impares += 1

    # b.  el menor numero ingresado
    if menor_numero_ingresado == None or numero < menor_numero_ingresado:
        menor_numero_ingresado = numero
    
    # d. suma de los positivos
    if numero > 0:
        suma_positivos += numero
    
    # e.
    if numero < 0:
        producto_negativos *= numero
        hay_negativos = True


    
print(f"Se ingresaron {pares} números pares")
print(f"Se ingresaron {impares} números pares")
print(f"El menor número ingresado fue {menor_numero_ingresado}")
if pares != None:
    print(f"No se han ingresado números pares")
else:
    print(f"La suma de los números positívos ingresados fue de {suma_positivos}")
if hay_negativos == True:
    print(f"El producto de los números negativos fue de {producto_negativos}")
else:
    print(f"No se han ingresado números negativos")