mapa = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0] 
]

def verificar_tesoro(mapa: list, x: int, y: int) -> int:
    if mapa[x][y] == 1:
        res = 0
    else:
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                if mapa[i][j] == 1:
                    res = abs(x-i)+(y-j)
    return res

seguir = "s"
while seguir == "s":
    coor_x = int(input("Ingrese la coordenada x (entre 1 y 5 inclusive): ")) -1
    while coor_x < 1 and coor_x > 5:
        coor_x = int(input("ERROR! Ingrese una coordenada x válida (entre 1 y 5 inclusive): ")) -1
    coor_y = int(input("Ingrese la coordenada y (entre 1 y 5 inclusive): ")) -1
    while coor_y < 1 and coor_y > 5:
        coor_y = int(input("ERROR! Ingrese una coordenada y válida (entre 1 y 5 inclusive): ")) -1
    res = verificar_tesoro(mapa,coor_x,coor_y)
    
    if res == 0:
        print("¡Encontraste el tesoro!")
        break
    else:
        print(f"Fallaste. El tesoro está a {res} casilleros de distancia.")
        seguir = input("Desea seguir buscando el tesoro? (s/n): ").lower()
