
#Creamos las constantes para luego utilizarlas
JUGADOR1 = " X "
JUGADOR2 = " O "
CLS = 35
CASILLA_VACIA = "   "
GANA_X = "\n\n\tGana el jugador X!!!"
GANA_Y = "\n\n\tGana el jugador O!!!"
DESPEDIDA = "\tHasta la proxima!!!"
TAMANO = 21

#           00   10    20    30    40     50    60
#           01   11    21    31    41     51    61
#           02   12    22    32    42     52    62
#           03   13    23    33    43     53    63 
#           04   14    24    34    44     54    64
#           05   15    25    35    45     55    65 
tablero=[["   ","   ","   ","   ","   ","   ","   "],
         ["   ","   ","   ","   ","   ","   ","   "],
         ["   ","   ","   ","   ","   ","   ","   "],
         ["   ","   ","   ","   ","   ","   ","   "],
         ["   ","   ","   ","   ","   ","   ","   "],
         ["   ","   ","   ","   ","   ","   ","   "]]

#Este metodo se encarga de pintar el tablero en la pantall
def dibujaTablero():
    print("\n  A   B   C   D   E   F   G  ",end="")
    for i in tablero:
        print("\n-----------------------------")

        for j in i:
            print("|"+j,end="")

        print("|",end="")

    print("\n-----------------------------")


def jugada(jugador):
    posicion = None
    posH = None
    posV= None

    while posicion is None:
        limpiaPantalla() 
        dibujaTablero()
        posicion = input(f"Introduce un caracter entre A-G ( Jugador:{jugador}): \t")
        
        if not (posicion!=None)and(type(posicion)==str)and(len(posicion)==1):
            posicion = None
        elif not ('A' <= posicion <= 'G' or 'a' <= posicion <= 'g'):
            posicion = None
        else:
            if(posicion == 'A' or posicion=='a'):
                posH = 0
                posV = 5
            elif(posicion == 'B' or posicion=='b'):
                posH = 1
                posV = 5
            elif(posicion == 'C' or posicion=='c'):
                posH = 2
                posV = 5
            elif(posicion == 'D' or posicion=='d'):
                posH = 3
                posV = 5
            elif(posicion == 'E' or posicion=='e'):
                posH = 4
                posV = 5
            elif(posicion == 'F' or posicion=='f'):
                posH = 5
                posV = 5
            elif(posicion == 'G' or posicion=='g'):
                posH = 6
                posV = 5

        
            while True:
                if (tablero[posV][posH]==CASILLA_VACIA):
                    tablero[posV][posH] = jugador
                    break                      
                elif (posV==0):
                    limpiaPantalla() 
                    print("Esa posicion no esta disponible \nEnter para continuar...")
                    valor = input()
                    break
                posV-=1

#Este metodo se encarga de limpiar la pantalla
def limpiaPantalla():
    for i in range(CLS):
        print("")


#Este metodo se encarga de comprobar las jugadas
def compruebaJugada(caracter):
    bandera = False

    for fila in tablero:
        if fila.count(caracter) == 4:
            return True

    for columna in range(len(tablero[0])):
        columna_fichas = [fila[columna] for fila in tablero]
        if columna_fichas.count(caracter) == 4:
            return True

    for i in range(len(tablero)-4):
        if tablero[i][i] == caracter and tablero[i+1][i+1] == caracter and tablero[i+2][i+2] == caracter and tablero[i+3][i+3] == caracter:
            return True

    for i in range(len(tablero)-3):
        if tablero[i][i] == caracter and tablero[i+1][i+2] == caracter and tablero[i+2][i+4] == caracter and tablero[i+3][i+6] == caracter:
            return True

    return bandera


while True:
    TAMANO-=1
    
    jugada(JUGADOR1)
    if(compruebaJugada(JUGADOR1)):
        dibujaTablero()
        print(GANA_X+"\n"+DESPEDIDA)
        break
    
    jugada(JUGADOR2)
    if(compruebaJugada(JUGADOR2)):
        dibujaTablero()
        print(GANA_Y+"\n"+DESPEDIDA)
        break

    if(TAMANO < 0):
        break    

dibujaTablero()