altitudes = [500.2, 3089.3, 120.3, 1900.4, 890.1, 
             2100.5, 48.6, 345.7, 2800.1, 1450.2] 

def bubble_sort(lista):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[j] > lista[i]:
                cambio = lista[i]
                lista[i] = lista[j]
                lista[j] = cambio
    return lista

#print(bubble_sort(altitudes))

def mostrar_ordenado(lista):
    for i in range(len(lista)):
        print(f"Posición {i+1}: {lista[i]}m")

mostrar_ordenado(bubble_sort(altitudes))