import random as rd

#Calcula  la cantidad de barcos para llena mas de 50% del tablero
min_nave = int(tamano*tamano*0.55/1)

#Funcion que crea el tablero
def creaMatriz(tamano):
  renglones = tamano
  columnas = tamano
  matriz = []
  for ren in range(renglones):
    lista = []
    for col in range(columnas):
      dato = 0
      lista.append(dato)
    matriz.append(lista)
  return matriz

#funcion que coloca barcos aleatorios de tamano de 1 en el tablero
def coloca_barcos(min_nave,m,tamano):
  barco_puesto = 0
  while barco_puesto < min_nave:
    fila = rd.randint(0, tamano-1)
    col = rd.randint(0,tamano-1)
    if m[fila][col] == 0:
      m[fila][col] = "X"
      barco_puesto += 1
  return m

def muestra_tablero(tablero,tamano):
  print(" ",end = " ")
  for i in range(tamano):
    print(i+1, end=" ")
  print("")
  for fila in range(tamano):
    print(fila+1,end = " ")
    for col in range(tamano):
      print(tablero[fila][col],end = " ")
    print("")

# Disparo diagonal inversa (‘\’)
def DDI(fila,col):
  tablero[fila][col] == "0"
  tablero[fila-1][col-1] == "0"
  tablero[fila+1][col+1] == "0"

# Disparo dona (‘o’)
def DD(fila,col):
  tablero[fila-1][col-1] == "0"
  tablero[fila][col-1] == "0"
  tablero[fila+1][col-1] == "0"
  tablero[fila-1][col] == "0"
  tablero[fila+1][col] == "0"
  tablero[fila-1][col+1] == "0"
  tablero[fila][col+1] == "0"
  tablero[fila+1][col+1] == "0"

# Disparo simple (‘-’)
def DS(fila,col):
  tablero[fila][col] == "0"
