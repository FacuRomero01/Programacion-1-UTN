def encuentra_maximo_de_3_numeros(num_1:int,num_2:int,num_3:int)->int:
    resultado = 0
    if num_1 >= num_2 and num_1 >= num_3:
        resultado = num_1
        return resultado
    elif num_2 >= num_1 and num_2 >= num_3:
        resultado = num_2
        return resultado
    else:
        resultado = num_3
        return resultado
    
print(encuentra_maximo_de_3_numeros(4,5,1))