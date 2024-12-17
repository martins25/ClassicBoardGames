
#Importamos las bibliotecas necesarias
import random

#Creamos las constantes para luego utilizarlas
ACORAZADO = " A " # 4 Posiciones x 1
CRUCERO   = " C " # 3 Posiciones x 2
SUBMARINO = " S " # 2 Posiciones x 3
BARCO     = " B " # 1 Posicion   x 4
CASILLA_VACIA = "   "

barcos = {ACORAZADO:1, CRUCERO:2, SUBMARINO:3, BARCO:4}

posOcupadas = set()

TOTAL = 99 # Casillas disponible 
CLS = 35
DESPEDIDA = "\tHasta la proxima!!!"


#           00   10    20    30    40     50    60    70    80    90
#           01   11    21    31    41     51    61    71    81    91
#           02   12    22    32    42     52    62    72    82    92
#           03   13    23    33    43     53    63    73    83    93
#           04   14    24    34    44     54    64    74    84    94
#           05   15    25    35    45     55    65    75    85    95
#           06   16    26    36    46     56    66    76    86    96
#           06   17    27    37    47     57    67    77    87    97
#           08   18    28    38    48     58    68    78    88    98
#           09   19    29    39    49     59    69    79    89    99
tablero=[["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
         ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
         ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
         ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
         ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
         ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
         ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
         ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
         ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]]

tablero2=[["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
          ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
          ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
          ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
          ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
          ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
          ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
          ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
          ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]]

def dibujaTablero(tab):
    print("\n    A   B   C   D   E   F   G   H   I   J",end="")
    
    cont=0
    for i in tab:
        
        print("\n  -----------------------------------------")
        print(f"{cont} ", end="")
        cont +=1

        for j in i:
            print("|"+j,end="")

        print("|",end="")

    print("\n  -----------------------------------------")


#0 horizontal 1 vertical
#Nos genera las fichas en el tablero
def generaAleatorios(tab, orientacion, numP, ficha):
   while True:
        fila = random.randint(0, len(tab) - 1)
        columna = random.randint(0, len(tab[0]) - 1)

        ocupado = False
        if orientacion == 0:
            if columna + numP > len(tab[0]):
                continue
            for i in range(numP):
                if tab[fila][columna + i] != CASILLA_VACIA:
                    ocupado = True
                    break
                
        else:
            if fila + numP > len(tab):
                continue
            for i in range(numP):
                if tab[fila + i][columna] != CASILLA_VACIA:
                    ocupado = True
                    break

        if ocupado:
            continue

        for i in range(numP):
            if orientacion == 0: 
                tab[fila][columna + i] = ficha
            else:  
                tab[fila + i][columna] = ficha

        return True
        

#Colocamos las fichas en los tableros
def flota(tab):
    for ficha, numP in barcos.items():
        for i in range(numP):
            while True:
                if(ficha == ACORAZADO):
                    tamaño = 4
                elif(ficha == CRUCERO):
                    tamaño = 3
                elif(ficha == SUBMARINO):
                    tamaño = 2
                elif(ficha == BARCO):
                    tamaño = 1

                if(generaAleatorios(tab, random.randint(0,2),tamaño, ficha)==True):
                    break

               

flota(tablero)
flota(tablero2)
dibujaTablero(tablero)
dibujaTablero(tablero2)