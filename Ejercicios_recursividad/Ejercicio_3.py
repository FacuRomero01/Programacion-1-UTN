def sumar_digitos(numero:int)->int:
    if numero < 0:
        numero = -numero
    
    if numero < 10:
        return numero
    else:
        return numero % 10 + sumar_digitos(numero // 10)

print(sumar_digitos(-158))