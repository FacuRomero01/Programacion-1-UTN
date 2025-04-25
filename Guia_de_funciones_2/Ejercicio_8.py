def muestra_cantidad_primos_hasta_parametro(numero:int)->int:
    cantidad_primos = 0
    if numero > 1:
        for i in range (2, numero + 1):
            divisores = 0
            for k in range(2, int(i**0.5) + 1):
                if i % k == 0:
                    divisores += 1

            if divisores == 0:
                print(i)
                cantidad_primos += 1
    return cantidad_primos

print(muestra_cantidad_primos_hasta_parametro(7))