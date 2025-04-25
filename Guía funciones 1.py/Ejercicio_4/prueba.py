def mostar_numero(numero:float):
    """
    Función que imprime el número dado como parametro
    
    Arg:
        numero (float): recibe un numero real

    """
    print(numero)

def validar_numero_en_rango(inicio_rango:float, fin_rango:float)-> bool:
    if numero >= inicio_rango and numero <= fin_rango:
        resultado = True
    else:
        resultado = False
    return resultado

numero = float(input("Ingrese un número: "))
inicio_rango = float(input("Ingrese el inicio del rango a comprobar: "))
fin_rango = float(input("Ingrese el fin del rango a comprobar: "))

print(numero)
if validar_numero_en_rango:
    print(f"el número {numero} se encuentra dentro del rango ingresado")
else:
        print(f"el número {numero} no se encuentra dentro del rango ingresado")