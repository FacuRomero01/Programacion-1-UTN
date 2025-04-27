def pide_10_nombres_y_los_retorna()->list:
    lista_nombres = []
    for i in range(1,11):
        nombre = str(input(f"Ingrese el nombre numero {i}: "))
        lista_nombres = lista_nombres + [nombre]
    return lista_nombres

print(pide_10_nombres_y_los_retorna())