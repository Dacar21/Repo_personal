EQUIPO = '1073'   # variable global 
 
comandos_recibidos = [ 
    'CMD,1073,CX,ON', 
    'CMD,1073,CAL', 
    'CMD,9999,CX,ON', 
    'CMD,1073,SIM,ENABLE', 
    'cmd,1073,CAL', 
    'CMD,1073,SIM,ACTIVATE', 
    'CMD,1073,SIM,DISABLE', 
    'DATOS,1073,OK', 
] 
 
COMANDOS_VALIDOS = ['CX,ON', 'CX,OFF', 'CAL', 'SIM,ENABLE', 
                    'SIM,ACTIVATE', 'SIM,DISABLE'] 

def validar_formato(cmd):
        separacion = comandos_recibidos[cmd].split(",",2)
        for j in range(len(separacion)):
            if separacion[j] == "CMD" and separacion[j+1] == EQUIPO and len(separacion)>=3:
                return True
            else: return False

#for i in range(len(comandos_recibidos)):
#     print(validar_formato(i))

def extraer_instruccion(posicion, cmd):
     separacion = comandos_recibidos[posicion].split(",",2)
     if cmd == True:
         for i in range(len(separacion)):
              if separacion[i] in COMANDOS_VALIDOS:
                   return separacion[i]
     return 'INVALIDO'
          
def procesar_todos(lista):
     for i in range(len(lista)):
          if validar_formato(i) == True:
               estado = 'VALIDO'
               estado_secundario = 'CONOCIDA'
          elif validar_formato(i) == False:
               estado = 'INVALIDO'
               estado_secundario = '-'

          print(f"{lista[i]}  --> {estado}  |  Instruccion: {extraer_instruccion(i,validar_formato(i))}  |  {estado_secundario}")

#for i in range(len(comandos_recibidos)):
#     print(extraer_instruccion(i,validar_formato(i)))
                   

procesar_todos(comandos_recibidos)
             
               