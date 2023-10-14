import random as rd

#Calcula  la cantidad de barcos para llena mas de 50% del tablero
min_nave = int(tamano*tamano*0.55/1)
tamano = 8
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
def diparos(matriz, tamaño):
    d= (input("Introduce el tipo de disparo: (o, *, -, +, \, /, X)"))
    f= int(input("Introduce la coordanada de la fila: "))
    c= int(input("Introduce la coordanada de la columna: "))
  
    # Disparo simple (‘-’)
    if d=="-":
        tablero[fila][col]== "0"
    # Disparo en asterisco (‘*’)
    elif d=="*":
        tablero[fila][col]== "0"
        tablero[fila-1][col-1]== "0"
        tablero[fila][col-1]== "0"
        tablero[fila+1][col-1]== "0"
        tablero[fila][col+1]== "0"
        tablero[fila-1][col]== "0"
        tablero[fila-1][col+1]== "0"
        tablero[fila][col+1]== "0"
        tablero[fila+1][col+1]== "0"
    # Disparo en cruz (‘+’)
    elif d=="+":
        tablero[fila][col]== "0"
        tablero[fila-1][col]== "0"
        tablero[fila+1][col]== "0"
        tablero[fila][col-1]== "0"
        tablero[fila][col+1]== "0"
    # Disparo en equis (‘X’)
    elif d=="X":
        tablero[fila][col]== "0"
        tablero[fila-1][col-1]== "0"
        tablero[fila+1][col+1]== "0"
        tablero[fila-1][col-10]== "0"
        tablero[fila-1][col+1]== "0"
    # Disparo en diagonal (‘/’)
    elif d=="/":
        tablero[fila][col]== "0"
        tablero[fila-1][col+1]== "0"
        tablero[fila+1][col-1]== "0"
    # Disparo en diagonal inversa (‘\’)
    elif d=="\\":
        tablero[fila][col] == "0"
        tablero[fila-1][col-1] == "0"
        tablero[fila+1][col+1] == "0"
    # Disparo de dona (‘o’)
    elif d=="o":
      tablero[fila-1][col-1] == "0"
      tablero[fila][col-1] == "0"
      tablero[fila+1][col-1] == "0"
      tablero[fila-1][col] == "0"
      tablero[fila+1][col] == "0"
      tablero[fila-1][col+1] == "0"
      tablero[fila][col+1] == "0"
      tablero[fila+1][col+1] == "0"
    else:
      print("Disparo no existente")

    

m=Matriz(tamaño)
tablero=coloca_barco(minimo_nave,m,tamaño)
mostrar_tablero(tablero, tamaño) 
diparos(m, tamaño)
