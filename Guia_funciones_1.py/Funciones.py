def restar1(numero_1:int,numero_2:int)->int:
    resultado = numero_1 - numero_2
    return resultado

def restar2()->int:
    numero_1 = int(input("Ingrese el primer número (restar2): "))
    numero_2 = int(input("Ingrese el segundo número (restar2): "))
    resultado = numero_1-numero_2
    return resultado

def restar3(numero_1:int,numero_2:int):
    resultado = numero_1 - numero_2
    (print(f"Resultado de restar3 es: {resultado}"))

def restar4():
    numero_1 = int(input("Ingrese el primer número (restar4): "))
    numero_2 = int(input("Ingrese el segundo número (restar4): "))
    resultado = numero_1 - numero_2
    (print(f"Resultado de restar4 es: {resultado}"))

def mostar_numero(numero:float):
    """
    Función que imprime el número dado como parametro
    
    Arg:
        numero (float): recibe un numero real

    """
    print(numero)

def validar_numero_en_rango(numero:float, inicio_rango:float, fin_rango:float)-> bool:
    if numero >= inicio_rango and numero <= fin_rango:
        resultado = True
    else:
        resultado = False
    return resultado