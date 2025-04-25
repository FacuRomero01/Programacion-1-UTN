from Funciones import *

def realizarDescuento():
    resultado = numero_1 * 0.95
    print(f"El número con el descuento del 5% es: {resultado}")


numero_1 = int(input("Ingrese un número: "))

if validar_numero_en_rango(numero_1,10,100):
    realizarDescuento()
else:
    print("El número ingresado no se encuentra entre 10 y 100")