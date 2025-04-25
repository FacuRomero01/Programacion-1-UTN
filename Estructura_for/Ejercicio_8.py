numero = int(input(f"Ingrese un número: "))

for fila in range(1,numero+1): #El primer for es el encargado de la cantidad de filas de la piramide
    for num in range(1,fila+1): #El segundo for es el encargado de imprimir cada número correspondiente a la fila
        print(num, end="")
    print()


# Empieza con fila = 1. La primera iteración del segundo for va a ir desde 1 hasta 1 (por fila+1=2 pero es excluyente).
# entonces el for imprime la primera iteración de num que es 1.
# Como la primera iteración del segundo for iba de 1 a 1 el código regresa al primer for y realiza la segunda iteración.
# Ahora fila = 2 y la segunda iteración del segundo for va desde 1 hasta 2, por lo tanto el código imprime 1 y después 2
# Se realiza la tercera iteración del primer for con fila = 3 y así analógamente con el resto del codígo hasta que llega a-
#-fila = numero+1 que es donde el primer for termina, dando fin al código, en el caso de numero = 5 el código termina-
#-cuando fila sea = 5.
