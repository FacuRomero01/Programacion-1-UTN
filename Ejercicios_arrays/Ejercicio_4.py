def chequea_numero_en_lista(numero:int,lista:list)->bool:
    for i in range(len(lista)):
        if lista[i] == numero:
            resultado = True
        else:
            resultado = False
    
    return resultado
    

print(chequea_numero_en_lista(5,[1,2,3,4,5]))