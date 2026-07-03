paquetes_recibidos = [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 15, 16, 17, 19]
                  #   1  2  3  4  5  6  7   8   9  10  11 

def encontrar_perdidos(lista):
    perdidos = []
    x = 0
    for i in range(len(lista)):
        x = x + 1
        if x != lista[i]:
            perdidos.append(x)
            x = x + 1
    return perdidos

print(encontrar_perdidos(paquetes_recibidos))


def Encontrar_Perdidos(lista):
    perdidos = []
    x = 0
    for i in range(len(lista)):
        x = x + 1
        if (lista[i] - x) > 0:
            for f in range(0,lista[i] - x):
             perdidos.append(x)
             x = x + 1
             #x = x + (lista[i] - x)
    return perdidos

print(Encontrar_Perdidos(paquetes_recibidos))

# print(paquetes_recibidos[-1])