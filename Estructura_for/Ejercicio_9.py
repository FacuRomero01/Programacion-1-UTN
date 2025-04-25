numero = int(input(f"Ingrese un número: "))
cantidad_divisores = 0

for i in range(1, numero+1):
    if numero % i == 0:
        print(i)
        cantidad_divisores += 1
    
print(f"la cantidad de divisores encontrados fue de {cantidad_divisores}")
        
