def sumar_natulares(numero:int)->int:
    if numero == 1: 
        return 1
    
    else:
        return numero + sumar_natulares(numero - 1)
        

