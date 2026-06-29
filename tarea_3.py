STATE_MAP = {
    0 : 'LAUNCH PAD',
    1 : 'ASCENT',
    2 : 'APOGEE',
    3 : 'DESCENT',
    4 : 'PAYLOAD RELEASE',
    5 : 'PROBE RELEASE',
    6 : 'LANDIG'
}

ACTIVE_FLIGHT = [1, 2, 3]

numero = int(input("Enter a state number (0-6):"))

def obtener_estado(diccionario, numero):
    if numero in diccionario:
        return diccionario[numero]
    else:
        return 'Estado Invalido'

estado = obtener_estado(STATE_MAP, numero)


def mostrar_mensaje(estado, numero):
    if estado == 'Estado Invalido':
        print("Numero fuera del rango")
    elif numero in ACTIVE_FLIGHT:
        print("Active flight:", estado)
    else:
        print("On ground:", estado)

mostrar_mensaje(estado,numero)