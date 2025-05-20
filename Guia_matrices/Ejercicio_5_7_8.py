stock = [
    [["to12", 65],["to16", 86],["to20", 65],["to25", 45]],
    [["to30", 68],["to35", 73],["to40", 85],["to45", 89]],
    [["ta4", 58],["ta5", 48],["ta6", 64],["ta7", 96]],
    [["ta8", 36],["ta10",72],["ta12", 78],["ta14", 71]]
]

def repone_mercaderia(stock:list,articulo:str,cantidad:int):
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
    print("{:<20}{:<20}{:<20}{:<20}".format("\nProducto", "Cantidad", "Fila", "Columna\n"))
    
    for fila in range(len(stock)):
        for columna in range(len(stock[fila])):
            producto = stock[fila][columna][0]
            cantidad = stock[fila][columna][1]
            print("{:<20}{:<20}{:<20}{:<20}".format(producto,cantidad,fila+1,columna+1))

def mostrar_stock(stock):
    print("")
    for i in range(len(stock)):
        for j in range(len(stock[i])):
            print(stock[i][j], end=" ")
        print("")
