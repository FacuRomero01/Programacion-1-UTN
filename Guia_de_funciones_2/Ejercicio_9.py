def imprime_tabla_multiplicar(numero:int,inicio:int=1,fin:int=10):
    for i in range(inicio,fin+1):
        print(f"{numero} x {i} = {numero*i}")

imprime_tabla_multiplicar(5,0,15)