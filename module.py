import random as rd


tamano = 8
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

#funcion que coloca barcos manuales:
def coloca_barcosmanual(min_nave,m,tamano):
  barco_puesto = 0
  while barco_puesto < min_nave:
    fila = int(input("Inserte la fila del barco: "))
    col = int(input("Inserte la columna del barco: "))
    if m[fila][col] == 0:
      m[fila][col] = "X"
      barco_puesto += 1
  return m

#Muestra la matriz como tablero
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

# Selecciona de los diferentes disparos con condiciones adicionales
def disparos(tablero):
  d = (input("Introduce el tipo de disparo: (o, *, -, +, \, /, X)"))
  fila = int(input("Introduce la coordanada de la fila: "))-1
  col = int(input("Introduce la coordanada de la columna: "))-1

  # Disparo simple (‘-’)
  if d=="-":
    tablero[fila][col]= "0"
    return tablero
  # Disparo en asterisco (‘*’)
  elif d=="*":
    if fila in range(1,7) and col in range(1,7):
      tablero[fila][col]= "0"
      tablero[fila-1][col-1]= "0"
      tablero[fila][col-1]= "0"
      tablero[fila+1][col-1]= "0"
      tablero[fila][col+1]= "0"
      tablero[fila-1][col]= "0"
      tablero[fila-1][col+1]= "0"
      tablero[fila][col+1]= "0"
      tablero[fila+1][col+1]= "0"
      return tablero
    else:
      print("¡No se puede usar este tipo de disparo en los bordes!")
      return tablero
  # Disparo en cruz (‘+’)
  elif d=="+":
    if fila in range(1,7) and col in range(1,7):
      tablero[fila][col]= "0"
      tablero[fila-1][col]= "0"
      tablero[fila+1][col]= "0"
      tablero[fila][col-1]= "0"
      tablero[fila][col+1]= "0"
      return tablero
    else:
      print("¡No se puede usar este tipo de disparo en los bordes!")
      return tablero
  # Disparo en equis (‘X’)
  elif d=="X":
    if fila in range(1,7) and col in range(1,7):
      tablero[fila][col]= "0"
      tablero[fila-1][col-1]= "0"
      tablero[fila+1][col+1]= "0"
      tablero[fila-1][col-10]= "0"
      tablero[fila-1][col+1]= "0"
      return tablero
    else:
      print("¡No se puede usar este tipo de disparo en los bordes!")
      return tablero
  # Disparo en diagonal (‘/’)
  elif d=="/":
    if fila in range(1,7) and col in range(1,7):
      tablero[fila][col]= "0"
      tablero[fila-1][col+1]= "0"
      tablero[fila+1][col-1]= "0"
      return tablero
    else:
      print("¡No se puede usar este tipo de disparo en los bordes!")
      return tablero
  # Disparo en diagonal inversa (‘\’)
  elif d=="\\":
    if fila in range(1,7) and col in range(1,7):
      tablero[fila][col] = "0"
      tablero[fila-1][col-1]= "0"
      tablero[fila+1][col+1] = "0"
      return tablero
    else:
      print("¡No se puede usar este tipo de disparo en los bordes!")
      return tablero
  # Disparo de dona (‘o’)
  elif d=="o":
    if fila in range(1,7) and col in range(1,7):
      tablero[fila-1][col-1] = "0"
      tablero[fila][col-1] = "0"
      tablero[fila+1][col-1] = "0"
      tablero[fila-1][col] = "0"
      tablero[fila+1][col] = "0"
      tablero[fila-1][col+1] = "0"
      tablero[fila][col+1] = "0"
      tablero[fila+1][col+1] = "0"
      return tablero
    else:
      print("¡No se puede usar este tipo de disparo en los bordes!")
      return tablero
  else:
    print("Disparo no existente")
    return tablero

