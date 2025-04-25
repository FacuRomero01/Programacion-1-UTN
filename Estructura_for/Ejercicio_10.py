numero = int(input(f"Ingrese un número: "))
es_primo = True
cantidad_divisores = 0


if numero <= 1:
    es_primo = False

for i in range(2, numero):
    if numero % i == 0:
        cantidad_divisores += 1

    es_primo = cantidad_divisores == 0 #Acá le asigna a la variable es_primo el resultado booleano de cantidad_divisores == 0 (true/false)
    
if es_primo:
    print(f"el número {numero} es primo")
else:
    print(f"el número {numero} NO es primo")