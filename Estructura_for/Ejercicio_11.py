numero = int(input(f"Ingrese un número: "))
cantidad_primos = 0

for i in range (2, numero + 1):
    divisores = 0
    if numero > 1:
        for k in range(2, i):
            if i % k == 0:
                divisores += 1

        if divisores == 0:
            print(i)
            cantidad_primos += 1
                
print(f"la cantidad de primos entre 1 y {numero} es: {cantidad_primos}")