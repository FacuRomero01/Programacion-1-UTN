def mostar_numero_en_rango(numero:float):
    """
    Función que imprime el número dado como parametro
    
    Arg:
        numero (float): recibe un numero real

    """
    if numero >= inicio_rango and numero <= fin_rango:
        resultado = f"El número {numero} se encuentra dentro del rango dado"
    else:
        resultado = f"el número {numero} no se encuentra dentro del rango dado"
    
    print(resultado)

numero = float(input("Ingrese un número: "))
inicio_rango = float(input("Ingrese el inicio del rango a comprobar: "))
fin_rango = float(input("Ingrese el fin del rango a comprobar: "))

mostar_numero_en_rango(numero)