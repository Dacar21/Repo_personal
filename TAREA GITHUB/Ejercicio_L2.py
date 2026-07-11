historial = [0,0,0,1,1,1,1,2,3,3,3,3,3,4,5,6,6,6] 
 
FASES = { 
    0: 'LAUNCH PAD', 
    1: 'ASCENT', 
    2: 'APOGEE', 
    3: 'DESCENT', 
    4: 'PAYLOAD RELEASE', 
    5: 'PROBE RELEASE', 
    6: 'LANDING' 
} 


def contar_por_fase(historial, fases):
    fase_equipo = {}
    for i in range(historial[-1] + 1):
       fase_equipo[fases[i]] = 0
    for k in range(historial[-1] + 1):
       for j in range(len(historial)):
           if historial[j] == k:
            fase_equipo[fases[k]] += 1 

    return fase_equipo

#print(contar_por_fase(historial,FASES))

def fase_mas_larga(conteo):
   mayor = conteo[FASES[0]]
   for i in range(historial[-1] + 1):
      if mayor < conteo[FASES[i]]:
          mayor = conteo[FASES[i]]
          nombre_fase_mayor = FASES[i]
   return nombre_fase_mayor, mayor

diccionario_fase_contada = contar_por_fase(historial,FASES)
#print(diccionario_fase_contada)
#print(fase_mas_larga(diccionario_fase_contada))

def mostrar_resumen(historial, fases):
   for i in range(historial[-1] + 1):
      print(FASES[i],":",diccionario_fase_contada[FASES[i]], "Paquetes")
   print()
   print("Fase mas larga:", fase_mas_larga(diccionario_fase_contada)[0], fase_mas_larga(diccionario_fase_contada)[1], "Paquetes")

mostrar_resumen(historial,FASES)