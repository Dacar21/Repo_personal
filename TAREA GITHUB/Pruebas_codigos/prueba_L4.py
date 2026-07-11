altitudes = [500.2, 3089.3, 120.3, 1900.4, 890.1, 
             2100.5, 48.6, 345.7, 2800.1, 1450.2] 

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] > lista[j]:
                cambio = lista[i]
                lista[i] = lista[j]
                lista[j] = cambio
    return lista

print(bubble_sort(altitudes))