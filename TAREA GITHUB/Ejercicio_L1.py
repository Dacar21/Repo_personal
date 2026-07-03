paquetes_recibidos = [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 15]
                  #   1  2  3  4  5  6  7   8   9  10  11 

def encontrar_perdidos(lista):
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


def calcular_porcentaje_perdida(recibidos, perdidos):
    return  round((perdidos / (recibidos + perdidos)) * 100, 2)

# print(calcular_porcentaje_perdida(len(paquetes_recibidos), len(encontrar_perdidos(paquetes_recibidos))))


def mostrar_reporte():

    print("Lista de perdidos:",encontrar_perdidos(paquetes_recibidos))
    print("Paquetes recibidos:",len(paquetes_recibidos))
    print("Paquetes perdidos:",len(encontrar_perdidos(paquetes_recibidos)))
    print("Porcentaje de perdida: ",calcular_porcentaje_perdida(len(paquetes_recibidos), len(encontrar_perdidos(paquetes_recibidos))),"%")

mostrar_reporte()