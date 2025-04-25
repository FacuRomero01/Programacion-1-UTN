def chequea_numero_primo(numero:int)->bool:
    resultado = True
    if numero == 1:
        resultado = False
    for divisor in range(2,int(numero**0.5) + 1):
        if numero % divisor == 0:
            resultado = False
    return resultado

print(chequea_numero_primo(55))