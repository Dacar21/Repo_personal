#Lista de altitudes
altitudes = [120.3, 345.7, 890.1, 1450.2, 2100.5, 3089.3, 2800.1, 1900.4, 500.2, 48.6]

#Funcion para mostrar altitudes
def mostrar_altitudes(altitudes):
    for i in range(len(altitudes)):
        print("Paquete", "[", i+1, "]:", altitudes[i])

'''
def maximo(altitudes):
    x=0
    for i in range(1):
        for j in range(len(altitudes)):
            if altitudes[j]>altitudes[i]:
                x=altitudes[j]
            else:
                x=altitudes[i]
    return x

'''

#Funcion que encuntra el valor maximo
def calcular_maximo(altitudes):

    x=altitudes[0]

    for i in range(len(altitudes)):
        if x < altitudes[i]: #29 y 30: compara e iguala si es menor, comparando con todos los numeros
            x=altitudes[i]
    return x
        

#Funcion que encuntra el valor minimo
def calcular_minimo(altitudes):

    x=altitudes[0]

    for i in range(len(altitudes)):
        if x > altitudes[i]: #40 y 41: compara e iguala si es mayor, comparando con todos los numeros
            x=altitudes[i]
    return x

#Funcion que calcula el promedio
def calcular_promedio(altitudes):
    suma = 0
    for i in altitudes:
        suma = suma + i
    return (suma)/(len(altitudes))

            
mostrar_altitudes(altitudes)
maximo = calcular_maximo(altitudes)
print("\nMaximo:", maximo, " m")
minimo = calcular_minimo(altitudes)
print("\nMinimo:", minimo, "m")
promedio = calcular_promedio(altitudes)
print("\nPromedio:", promedio, "m\n")
