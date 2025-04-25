def calcular_potencia(base:int,exponente:int)->int:
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / calcular_potencia(base, -exponente)
    else:
        return base * calcular_potencia(base, exponente - 1)
    
