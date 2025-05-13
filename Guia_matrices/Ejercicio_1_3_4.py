from Funciones import ordena_lista_asc

stock = [
    [[None,None],["Botella", 3],[None, None],["Frasco", 8],[None, None]],
    [[None,None],[None, None],["Fideo", 4],[None, None],[None, None]],
    [[None,None],[None, None],[None, None],["Leche", 6],[None, None]]
]

def agrega_nuevo_producto(stock:list,producto:str,cantidad:int,fila:int,columna:int):
    fila -= 1
    columna -=1
    if stock[fila][columna] == [None, None]:
        stock[fila][columna] = [producto, cantidad]
        print(f"\nEl producto {producto} fue agregado exitosamente en fila: {fila+1}, columna: {columna+1}")
    else:
        print("Error! Ya hay un producto en esa ubicación")

def elimina_producto(stock:list,producto:str):
    encontrado = False
    for fila in range(len(stock)):
        for columna in range(len(stock[fila])):
            nombre = stock[fila][columna][0]
            if nombre == producto:
                stock[fila][columna] = [None, None]
                print(f"\nEl producto {producto} ha sido eliminado de fila {fila+1}, columna {columna+1} del stock ")
                encontrado = True
    if not encontrado:
        print(f"Error! {producto} no se encuentra actualmente en stock")
    
def modifica_producto(stock:list,producto:str,nueva_cantidad:int,nueva_fila:int,nueva_columna:int):
    encontrado = False
    nueva_fila -= 1
    nueva_columna -= 1

    for fila in range(len(stock)):
        for columna in range(len(stock[fila])):
            nombre = stock[fila][columna][0]
            if nombre == producto:
                if stock[nueva_fila][nueva_columna] == [None, None]:
                    stock[nueva_fila][nueva_columna] = [producto, nueva_cantidad] 
                    stock[fila][columna] = [None, None]
                    print(f"El producto {producto} se movió a la fila {nueva_fila+1}, columna {nueva_columna+1}. La cantidad se modificó a {nueva_cantidad}")
                    encontrado = True
    if not encontrado:
        print(f"Error! la ubicación ({nueva_fila}, {nueva_columna}) no está libre")

def lista_productos(stock:list):
    print("{:<20}{:<20}{:<20}{:<20}".format("\nProducto", "Cantidad", "Fila", "Columna\n"))
    
    for fila in range(len(stock)):
        for columna in range(len(stock[fila])):
            producto = stock[fila][columna][0]
            cantidad = stock[fila][columna][1]
            if stock[fila][columna] != [None, None]:
                print("{:<20}{:<20}{:<20}{:<20}".format(producto,cantidad,fila+1,columna+1))

def ordena_productos_por_nombre(stock:list)->list:
    lista_productos = []
    for fila in range(len(stock)):
        for columna in range(len(stock[fila])):
            producto = stock[fila][columna][0]
            cantidad = stock[fila][columna][1]
            if stock[fila][columna] != [None, None]:
                lista_productos.append((producto, cantidad, fila+1,columna+1))
    
    lista_ordenada = ordena_lista_asc(lista_productos)
    return lista_ordenada

def lista_productos_por_nombre(stock:list):
    lista_ordenada = ordena_productos_por_nombre(stock)
    print("{:<20}{:<20}{:<20}{:<20}".format("\nProducto", "Cantidad", "Fila", "Columna\n"))
    
    for i in range(len(lista_ordenada)):
        producto = lista_ordenada[i][0]
        cantidad = lista_ordenada[i][1]
        fila = lista_ordenada[i][2]
        columna = lista_ordenada[i][3]
        print("{:<20}{:<20}{:<20}{:<20}".format(producto,cantidad,fila,columna))

def mostrar_stock(stock):
    print("")
    for i in range(len(stock)):
        for j in range(len(stock[i])):
            print(stock[i][j], end=" ")
        print("")