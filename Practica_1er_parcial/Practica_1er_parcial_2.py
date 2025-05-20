matriz = [
    [5, 2, 3, 4],
    [5, 2, 7, 8],
    [2, 2, 3, 1],
    [1, 6, 7, 4]
]

def chequea_3_numeros_iguales_vertical(matriz:list):
    filas = len(matriz)
    columnas = len(matriz[0])
    res = None
    for columna in range(columnas):
        for fila in range(filas - 2):
            numero = matriz[fila][columna]
            if matriz[fila][columna] == matriz[fila+1][columna] == matriz[fila+2][columna]:
                res = numero
    return res
