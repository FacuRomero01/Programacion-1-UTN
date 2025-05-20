def chequea_3_numeros_iguales_vertical(matriz:list) -> any:
    res = None
    for columna in range(len(matriz[0])):
        for fila in range(len(matriz) - 2):
            numero = matriz[fila][columna]
            if matriz[fila][columna] == matriz[fila+1][columna] == matriz[fila+2][columna]:
                res = numero
    return res

matriz = [
    [5, 2, 3, 4],
    [5, 1, 7, 8],
    [2, 2, 3, 1],
    [1, 6, 7, 4]
]

resultado = chequea_3_numeros_iguales_vertical(matriz)
if resultado is not None:
    print(f"Se encontró un valor que cumple con la condición, el número es: {resultado}")
else:
    print(f"No se encontró un número que cumpla con la condición")
