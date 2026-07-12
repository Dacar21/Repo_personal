LIMITE_TEMP  = 45.0   # variable global — temperatura máxima permitida 
LIMITE_VOLT  = 7.60   # variable global — voltaje mínimo permitido 
 
sensores = [ 
    {'nombre': 'Barometro',    'unidad': 'kPa',  'lectura': 85.3,  'activo': True }, 
    {'nombre': 'Temperatura',  'unidad': 'C',    'lectura': 46.2,  'activo': True }, 
    {'nombre': 'GPS',          'unidad': 'coord','lectura': 38.37, 'activo': True }, 
    {'nombre': 'Voltaje',      'unidad': 'V',    'lectura': 7.55,  'activo': True }, 
    {'nombre': 'Giroscopio',   'unidad': 'deg/s','lectura': 2.1,   'activo': False}, 
    {'nombre': 'Acelerometro', 'unidad': 'm/s2', 'lectura': 9.85,  'activo': True }, 
]

SENSORES_CON_ALERTA = 0

def sensores_activos(lista):
    activos = []
    for i in range(len(lista)):
            if lista[i]['activo'] == True:
                activos.append(lista[i]['nombre'])
    return activos

def verificar_alertas(lista):
     global SENSORES_CON_ALERTA
     for i in range(len(lista)):
          if lista[i] == 'Temperatura':
               for j in range(len(sensores)):
                    if sensores[j]['nombre'] == 'Temperatura':
                         if sensores[j]['lectura'] > LIMITE_TEMP:
                              SENSORES_CON_ALERTA += 1
                              print(f"ALERTA: Temperatura en {sensores[j]['lectura']} C — supera el límite de {LIMITE_TEMP}C ")
          if lista[i] == 'Voltaje':
               for j in range(len(sensores)):
                    if sensores[j]['nombre'] == 'Voltaje':
                         if sensores[j]['lectura'] < LIMITE_VOLT:
                              SENSORES_CON_ALERTA += 1
                              print(f"ALERTA: Voltaje en {sensores[j]['lectura']} V — por debajo del mínimo de {LIMITE_VOLT} V")
                                
          
def calcular_estadisticas(lista):
     diccionario_estado = {}
     diccionario_estado['total'] = len(lista)
     diccionario_estado['activos'] = len(sensores_activos(sensores))
     diccionario_estado['con_alerta'] = SENSORES_CON_ALERTA
     return diccionario_estado
     
def mostrar_panel(lista):
     print("=== PANEL DE SENSORES ===")
     for i in range(len(sensores)):
          print(f"{sensores[i]['nombre']} ", end="")
          if sensores[i]['activo'] == True:
               print("[ACTIVO]", end="")
          else:
               print("[INACTIVO]", end="")
          print(" : ", end="")
          print(f"{sensores[i]['lectura']} {sensores[i]['unidad']}")
     print("")
     verificar_alertas(sensores_activos(lista))
     diccionario_estadistica = calcular_estadisticas(lista)
     print("")
     print(f"Total sensores: {diccionario_estadistica['total']}")
     print(f"Activos: {diccionario_estadistica['activos']}")
     print(f"Con alerta: {diccionario_estadistica['con_alerta']}")


mostrar_panel(sensores)