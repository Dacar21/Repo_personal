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
    contador = 0
    for i in range(historial[-1] + 1):
       fase_equipo[fases[i]] = 0
    for k in range(historial[-1] + 1):
       for j in range(len(historial)):
           if historial[j] == k:
            fase_equipo[fases[k]] += 1 

    return fase_equipo

print(contar_por_fase(historial,FASES))