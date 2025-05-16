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
                    res = valor_absoluto(x-i)+valor_absoluto(y-j)
    return res

def valor_absoluto(numero):
    if numero < 0:
        return -numero
    else:
        return numero

seguir = "s"
while seguir == "s":
    coor_x = int(input("Ingrese la coordenada x (entre 0 y 4 inclusive): "))
    while coor_x < 0 or coor_x > 4:
        coor_x = int(input("ERROR! Ingrese una coordenada x válida (entre 0 y 4 inclusive): "))
    coor_y = int(input("Ingrese la coordenada y (entre 0 y 4 inclusive): ")) 
    while coor_y < 0 or coor_y > 4:
        coor_y = int(input("ERROR! Ingrese una coordenada y válida (entre 1 y 5 inclusive): "))
    
    res = verificar_tesoro(mapa,coor_x,coor_y)
    
    if res == 0:
        print("¡Encontraste el tesoro!")
        break
    else:
        print(f"Fallaste. El tesoro está a {res} casilleros de distancia.")
        seguir = input("Desea seguir buscando el tesoro? (s/n): ").lower()
        while seguir != "s".lower() or seguir != "n".lower():
            seguir = input("ERROR! Ingrese una opcion válida. Desea seguir buscando el tesoro? (s/n): ").lower()

