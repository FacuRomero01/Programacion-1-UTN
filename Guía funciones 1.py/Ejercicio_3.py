def comprobar_par(numero:int)->bool:
    """
    Función que comprueba si un número es par o impar

    Args:
        numero (int): número a comprobar

    Returns:
        bool: Devuelve True si es par y False si es impar

    """
    if numero % 2 == 0:
        return True
    
numero = int(input("Ingrese un número: "))
if comprobar_par(numero):
    print(f"El número {numero} es par ")
else:
    print(f"El número {numero} es impar ")
