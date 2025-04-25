def chequea_par_impar()->bool:
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        return True
    else:
        return False
    
resultado = chequea_par_impar()    
print(resultado)