from Funciones import *

def suma_o_resta_de_2_numeros_segun_usuario(numero_1:int,numero_2:int,operacion:str)->int:
    if operacion == "s":
        resultado = numero1 + numero2
    else:
        resultado = numero1 - numero2
    return resultado



numero1 = int(input("Ingrese el primer número (entre 10-100): "))
while numero1 < 10 or numero1 >100:
    numero1 = int(input("Error! Ingrese un número correcto (entre 10-100): "))

numero2 = int(input("Ingrese el segundo número (entre 10-100): "))
while numero2 < 10 or numero1 >100:
    numero2 = int(input("Error! Ingrese un número correcto (entre 10-100): "))

operacion = input("ingrese la accion que desea realizar (s-sumar/r-restar): ")
while operacion != "s" and operacion != "r":
    operacion = input("Error! Ingrese una acción correcta (s-sumar/r-restar): ")


if validar_numero_en_rango(numero1,10,100) and validar_numero_en_rango(numero2,10,100):
    if operacion == "s":
        print(f"La suma entre {numero1} y {numero2} es de {suma_o_resta_de_2_numeros_segun_usuario(numero1,numero2,"s")}")
    else:
        print(f"La resta entre {numero1} y {numero2} es de {suma_o_resta_de_2_numeros_segun_usuario(numero1,numero2,"r")}")