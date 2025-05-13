def validar_numero_en_rango(numero:float, inicio_rango:float, fin_rango:float)-> bool:
    if numero >= inicio_rango and numero <= fin_rango:
        resultado = True
    else:
        resultado = False
    return resultado

def devuelve_menor_de_los_numeros_lista(lista_numeros:list)->int:
    menor_numero = lista_numeros[0]
    for i in range(len(lista_numeros)):
        if lista_numeros[i] < menor_numero:
            menor_numero = lista_numeros[i]

    return menor_numero

def promedia_lista_numeros(lista_numeros:list)->float:
    suma_numeros = 0
    for i in range(len(lista_numeros)):
        suma_numeros += lista_numeros[i]
    promedio = suma_numeros/len(lista_numeros)

    return promedio

def devuelve_mayor_de_los_numeros_lista(lista_numeros:list)->int:
    mayor_numero = lista_numeros[0]
    for i in range(len(lista_numeros)):
        if lista_numeros[i] > mayor_numero:
            mayor_numero = lista_numeros[i]

    return mayor_numero

def ordena_lista_asc(lista:list)->list:
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:

                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def ordena_lista_desc(lista:list)->list:
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] < lista[j]:

                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def encuentra_indice_entre_dos_listas_dado_parametro(lista:list,lista_2:list,parametro:str):
    indice_parametro = []
    for i in range(len(lista)):
        if lista_2[i].lower() == parametro.lower():
            indice_parametro.append(i)

    return indice_parametro