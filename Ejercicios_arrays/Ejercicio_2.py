def retorna_numero_y_posicion_pedida_por_el_usuario()->list:
    lista = [0]*10
    posicion = int(input("Ingrese el indice del valor que quiera modificar (0-11): "))
    numero = int(input("Ingrese un número: "))
    lista[posicion] = numero
    return lista

print(retorna_numero_y_posicion_pedida_por_el_usuario())