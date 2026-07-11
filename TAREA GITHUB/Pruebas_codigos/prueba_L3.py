temperaturas = [42.1, 41.8, 41.3, 40.5, 39.8, 38.9, 38.2, 38.5, 39.1, 40.2, 41.0,      
41.5] 
TAMANO_VENTANA = 3   # variable global 

def promedio_ventana(lista, inicio, tamano):
    total = 0
    for i in range(inicio, inicio + tamano):
        total += lista[i]
    return total/tamano

# print(promedio_ventana(temperaturas, 0 ,TAMANO_VENTANA))

def calcular_promedios_moviles(lista):
    temp_promedio = []
    for i in range(len(lista)):
        if i + 1 < TAMANO_VENTANA:
            temp_promedio.append('N/A')
        else:
            temp_promedio.append(round(promedio_ventana(lista, (i+1)-TAMANO_VENTANA, TAMANO_VENTANA),2))
    return temp_promedio

def detectar_tendencia(promedios):
    for i in range(len(promedios)):
        if promedios[i] != 'N/A' and i > 0 and promedios[i-1] != 'N/A' :
            if promedios[i-1] < promedios[i]:
                print("ENFRIANDO")
            elif promedios[i-1] > promedios[i]:
                print("CALENTANDO")
            else:
                print("ESTABLE")

print(f"Promedio moviles: {calcular_promedios_moviles(temperaturas)}")
detectar_tendencia(calcular_promedios_moviles(temperaturas))