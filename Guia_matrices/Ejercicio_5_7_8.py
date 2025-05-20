stock = [
    [["to12", 65],["to16", 86],["to20", 65],["to25", 45]],
    [["to30", 68],["to35", 73],["to40", 85],["to45", 89]],
    [["ta4", 58],["ta5", 48],["ta6", 64],["ta7", 96]],
    [["ta8", 36],["ta10",72],["ta12", 78],["ta14", 71]]
]

def repone_mercaderia(stock:list,articulo:str,cantidad:int):
    
    """
    Repone la cantidad especificada de un artículo en el inventario.

    Parámetros:
    - stock (list): Matriz que representa el inventario. Cada celda contiene una lista con el nombre del artículo y su cantidad.
    - articulo (str): Nombre del artículo que se desea reponer.
    - cantidad (int): Cantidad que se desea agregar al stock del artículo.

    Funcionamiento:
    - Busca el artículo en todo el inventario.
    - Si lo encuentra, suma la cantidad dada a la cantidad actual y actualiza el inventario.
    - Si no lo encuentra, muestra un mensaje de error.
    """

    encontrado = False
    for fila in range(len(stock)):
        for columna in range(len(stock[fila])):
            nombre_articulo = stock[fila][columna][0]
            cantidad_nueva = stock[fila][columna][1]
            if nombre_articulo == articulo:
                cantidad_nueva = cantidad_nueva + cantidad
                stock[fila][columna] = [articulo, cantidad_nueva]
                print(f"\nEl stock del artículo {articulo} se ha repuesto a {cantidad_nueva} unidades")
                encontrado = True
    if not encontrado:
        print(f"\nError! {articulo} no se encuentra actualmente en stock")

def vende_mercaderia(stock:list,articulo:str,cantidad:int):
    
    """
    Vende la cantidad especificada de un artículo del inventario.

    Parámetros:
    - stock (list): Matriz que representa el inventario. Cada celda contiene una lista con el nombre del artículo y su cantidad.
    - articulo (str): Nombre del artículo que se desea vender.
    - cantidad (int): Cantidad que se desea vender del artículo.

    Funcionamiento:
    - Busca el artículo en todo el inventario.
    - Si lo encuentra y hay suficiente cantidad, descuenta la cantidad vendida y actualiza el inventario.
    - Si la cantidad en stock es menor a la solicitada, muestra un mensaje de error.
    - Si el artículo no se encuentra, también muestra un mensaje de error.
    """

    encontrado = False
    for fila in range(len(stock)):
        for columna in range(len(stock[fila])):
            nombre_articulo = stock[fila][columna][0]
            cantidad_articulo = stock[fila][columna][1]
            if nombre_articulo == articulo:
                if cantidad <= cantidad_articulo:
                    cantidad_restante = cantidad_articulo-cantidad
                    stock[fila][columna] = [articulo, cantidad_restante]
                    print(f"\nSe han vendido {cantidad} unidades del artículo {articulo}. Quedan restantes {cantidad_restante} unidades")
                    encontrado = True
                else:
                    print(f"\nError! Tiene solo {cantidad_articulo} unidades de {articulo} y usted quiere vender {cantidad}")
                    encontrado = True
    if not encontrado:
        print(f"\nError! {articulo} no se encuentra actualmente en stock")

def lista_inventario(stock:list):

    """
    Lista todos los artículos del inventario con su cantidad y posición (fila y columna).

    Parámetros:
    - stock (list): Matriz que representa el inventario. Cada celda contiene una lista con el nombre del artículo y su cantidad.

    Funcionamiento:
    - Recorre toda la matriz e imprime el nombre del producto, su cantidad y su posición en el inventario (en índices humanos, es decir, a partir del 1).
    """

    print("{:<20}{:<20}{:<20}{:<20}".format("\nProducto", "Cantidad", "Fila", "Columna\n"))
    
    for fila in range(len(stock)):
        for columna in range(len(stock[fila])):
            producto = stock[fila][columna][0]
            cantidad = stock[fila][columna][1]
            print("{:<20}{:<20}{:<20}{:<20}".format(producto,cantidad,fila+1,columna+1))

def mostrar_stock(stock):

    """
    Muestra visualmente el contenido del inventario en forma de matriz.

    Parámetros:
    - stock (list): Matriz que representa el inventario. Cada celda contiene una lista con el nombre del artículo y su cantidad.

    Funcionamiento:
    - Recorre la matriz e imprime cada fila, mostrando el nombre y la cantidad de cada artículo.
    - No da formato tabular, solo muestra los datos tal como están en cada celda.
    """

    print("")
    for i in range(len(stock)):
        for j in range(len(stock[i])):
            print(stock[i][j], end=" ")
        print("")
