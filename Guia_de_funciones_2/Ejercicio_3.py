def chequea_par_impar():
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")

    
chequea_par_impar()