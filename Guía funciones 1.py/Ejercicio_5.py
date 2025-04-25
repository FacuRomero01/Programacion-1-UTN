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

resultado_1 = restar1(5,3)
resultado_2 = restar2()

print(f"Resultado de restar1 es: {resultado_1}")
print(f"Resultado de restar2 es: {resultado_2}")
restar3(5,3)
restar4()
