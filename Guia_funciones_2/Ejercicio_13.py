def retorna_numero_ingresado()->int:
    numero = int(input("Ingrese un número: "))
    while numero != int:
        numero = int(input("Error! Ingrese un número: "))
    return numero

print(retorna_numero_ingresado())