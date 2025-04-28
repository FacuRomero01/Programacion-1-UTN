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

def devuelve_menor_de_los_numeros_lista(lista_numeros:list)->int:
    menor_numero = lista_numeros[0]
    for i in range(len(lista_numeros)):
        if lista_numeros[i] < menor_numero:
            menor_numero = lista_numeros[i]

    return menor_numero

def promedia_lista_numeros(lista_numeros:list)->float:
    suma_numeros = 0
    for i in range(len(lista_numeros)):
        suma_numeros += lista_numeros[i]
    promedio = suma_numeros/len(lista_numeros)

    return promedio

def devuelve_mayor_de_los_numeros_lista(lista_numeros:list)->int:
    mayor_numero = lista_numeros[0]
    for i in range(len(lista_numeros)):
        if lista_numeros[i] > mayor_numero:
            mayor_numero = lista_numeros[i]

    return mayor_numero
