EQUIPO = '1073'   # variable global 
 
historial = [ 
    {'comando': 'CX,ON',        'resultado': 'OK',   'tiempo': '00:00:05'}, 
    {'comando': 'CAL',          'resultado': 'OK',   'tiempo': '00:00:12'}, 
    {'comando': 'SIM,ENABLE',   'resultado': 'OK',   'tiempo': '00:01:00'}, 
    {'comando': 'SIM,ACTIVATE', 'resultado': 'OK',   'tiempo': '00:01:05'}, 
    {'comando': 'SIM,DISABLE',  'resultado': 'ERROR','tiempo': '00:03:00'}, 
    {'comando': 'CX,OFF',       'resultado': 'OK',   'tiempo': '00:05:00'}, 
    {'comando': 'CAL',          'resultado': 'ERROR','tiempo': '00:05:30'}, 
    {'comando': 'CX,ON',        'resultado': 'OK',   'tiempo': '00:06:00'}, 
] 

nombre_buscar = ''

def contar_resultados(historial):
    diccionario_contador = {}
    cont_ok = 0
    cont_error = 0
    for i in range(len(historial)):
        if historial[i]['resultado'] == 'OK':
            cont_ok += 1
        if historial[i]['resultado'] == 'ERROR':
            cont_error += 1
    diccionario_contador['OK'] = cont_ok
    diccionario_contador['ERROR'] = cont_error
    return diccionario_contador


def buscar_comando(historial, nombre):
    lista = []
    for i in range(len(historial)):
        if historial[i]['comando'] == nombre:
            lista.append((historial[i]['comando'],historial[i]['resultado'],historial[i]['tiempo']))
    return lista

'''
def comando_mas_usado(historial):
    comando = {}
    for i in range(len(historial)):
        comando = historial[i]['comando']
        if comando in historial
'''



print(buscar_comando(historial,nombre_buscar))
print(contar_resultados(historial))
print(len(historial))