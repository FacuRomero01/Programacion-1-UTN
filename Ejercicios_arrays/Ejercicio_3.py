from Funciones import validar_numero_en_rango

def pide_10_numeros_valida_rango_y_retorna_lista()->list:
    lista = [0]*10
    for i in range(len(lista)):
        numero = int(input(f"Ingrese el número N°{i+1} (entre 0-100): "))
        while not validar_numero_en_rango(numero,0,100):
            numero = int(input("ERROR! Ingrese un número correcto (entre 0-100): "))
        
        lista[i] = numero
    return lista

print(pide_10_numeros_valida_rango_y_retorna_lista())