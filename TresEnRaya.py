
#Creamos las constantes para luego utilizarlas
JUGADOR1 = " X "
JUGADOR2 = " O "
CLS = 35
CASILLA_VACIA = "   "
GANA_X = "\n\n\tGana el jugador X!!!"
GANA_Y = "\n\n\tGana el jugador Y!!!"
DESPEDIDA = "\tHasta la proxima!!!"
nJugadas = 9

#           00   10    20 
#           01   11    21 
#           02   12    22 
tablero=[["   ","   ","   "],
         ["   ","   ","   "],
         ["   ","   ","   "]]

#Este metodo recorre la lista del tablero y lo muestra en pantalla
def dibujaTablero():
    for i in tablero:
        print("\n-------------")

        for j in i:
            print("|"+j,end="")

        print("|",end="")

    print("\n-------------")

#Este metodo se encarga de poner la ficha del jugador en la posicion que ha seleccionado y comprueba que no este cogida
def jugadaN(caracter):
    posicionH = None 
    posicionV = None
    
    while True:
        dibujaTablero()
        while posicionH is None:
            posicionH = int(input(f"Introduce la posicion horizontal del 0-2( Jugador{caracter}):\t"))
            if(posicionH == 9):
                return False
            if not (posicionH>=3 or len(format(posicionH, '#'))<=1):
                print("El valor introducido no es valido")
                posicionH = None

        while posicionV is None:
            posicionV = int(input(f"Introduce la posicion vertical del 0-2( Jugador{caracter}):\t"))
            if(posicionV == 9):
                return False
            if not (posicionV>=3 or len(format(posicionV, '#'))<=1):
                print("El valor introducido no es valido")
                posicionV = None

        if (tablero[posicionV][posicionH]==CASILLA_VACIA):
            tablero[posicionV][posicionH] = caracter
            break 
        else:
            limpiaPantalla() 
            print("Esa posicion no esta disponible \nEnter para continuar...")
            valor = input()
            posicionH = None
            posicionV = None
    return True



#Este metodo se encarga de limpiar la pantalla
def limpiaPantalla():
    for i in range(CLS):
        print("")

#Este metodo se encarga de revisar si gano alguien la partida o no
def compruebaJugada(caracter):
    bandera = False
    for i in range(3):
        if (tablero[i][0] == caracter and tablero[i][1] == caracter and tablero[i][2] == caracter):
            bandera = True
        if (tablero[0][i] == caracter and tablero[1][i] == caracter and tablero[2][i] == caracter):
            bandera = True
        if (tablero[0][0] == caracter and tablero[1][1] == caracter and tablero[2][2] == caracter):
            bandera = True
        if (tablero[0][2] == caracter and tablero[1][1] == caracter and tablero[2][0] == caracter):
            bandera = True
    return bandera


print("Tres en raya")
print("Para salir pulse del juego introduzca '9' en cualquier solicitud de posicion")
print("\nPosiciones del tablero")
print("00   10    20")
print("01   11    21")
print("02   12    22")

contador=0
while True:
    
    if(contador < nJugadas):
        if not (jugadaN(JUGADOR1)):
            print(DESPEDIDA)
            break
        contador += 1
    if(contador < nJugadas):    
        if not (jugadaN(JUGADOR2)):
            print(DESPEDIDA)
            break
        contador += 1
        
        if contador <= 3:
            if (compruebaJugada(JUGADOR1)):
                print(GANA_X+"\n"+DESPEDIDA)
                break
            if (compruebaJugada(JUGADOR2)):
                print(GANA_Y+"\n"+DESPEDIDA)
                break 
    else:
        dibujaTablero()
        print("Empate")
        break

    