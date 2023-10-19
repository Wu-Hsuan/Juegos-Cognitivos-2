import random as rd
#Define el tamaño del tablero(matriz)
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
    if m[fila-1][col-1] == 0:
        m[fila-1][col-1] = "X"
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
def disparos(tablero, d, fila, col):       
    
  #Verificar si está el disparo es una esquina
  esquina=(fila == 0 and col == 0) or \
          (fila == 0 and col == tamano - 1) or \
          (fila == tamano - 1 and col == 0) or \
          (fila == tamano - 1 and col == tamano - 1)
          
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
      tablero[fila+1][col]= "0"
      tablero[fila+1][col+1]= "0"
      return tablero
    elif fila == 0 and col == 0:
      tablero[fila][col]= "0"
      tablero[fila][col+1]= "0"
      tablero[fila+1][col]= "0"
      tablero[fila+1][col+1]= "0"
      return tablero
    elif fila == 7 and col == 0:
      tablero[fila][col]= "0"
      tablero[fila][col+1]= "0"
      tablero[fila-1][col+1]= "0"
      tablero[fila-1][col]= "0"
      return tablero
    elif fila == 0 and col == 7:
      tablero[fila][col]= "0"
      tablero[fila+1][col-1]= "0"
      tablero[fila+1][col]= "0"
      tablero[fila][col-1]= "0"
      return tablero
    elif fila == 7 and col == 7:
      tablero[fila][col]= "0"
      tablero[fila][col-1]= "0"
      tablero[fila-1][col]= "0"
      tablero[fila-1][col-1]= "0"
      return tablero
    elif fila == 0 and col in range(1,7):
      tablero[fila][col]= "0"
      tablero[fila][col-1]= "0"
      tablero[fila+1][col-1]= "0"
      tablero[fila][col+1]= "0"
      tablero[fila+1][col]= "0"
      tablero[fila+1][col+1]= "0"
      return tablero
    elif fila in 7 and col == range(1,7):
      tablero[fila][col]= "0"
      tablero[fila-1][col-1]= "0"
      tablero[fila][col-1]= "0"
      tablero[fila][col+1]= "0"
      tablero[fila-1][col]= "0"
      tablero[fila-1][col+1]= "0"
      return tablero
    elif fila in range(1,7) and col == 0:
      tablero[fila][col]= "0"
      tablero[fila][col+1]= "0"
      tablero[fila-1][col]= "0"
      tablero[fila-1][col+1]= "0"
      tablero[fila+1][col]= "0"
      tablero[fila+1][col+1]= "0"
      return tablero
    elif fila in range(1,7) and col == 7:
      tablero[fila][col]= "0"
      tablero[fila-1][col-1]= "0"
      tablero[fila][col-1]= "0"
      tablero[fila+1][col-1]= "0"
      tablero[fila-1][col]= "0"
      tablero[fila+1][col]= "0"
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
    elif fila == 0 and col == 0:
      tablero[fila][col]= "0"
      tablero[fila+1][col]= "0"
      tablero[fila][col+1]= "0"
      return tablero
    elif fila == 7 and col == 0:
      tablero[fila][col]= "0"
      tablero[fila-1][col]= "0"
      tablero[fila][col+1]= "0"
      return tablero
    elif fila == 0 and col == 7:
      tablero[fila][col]= "0"
      tablero[fila+1][col]= "0"
      tablero[fila][col-1]= "0"
      return tablero
    elif fila == 7 and col == 7:
      tablero[fila][col]= "0"
      tablero[fila-1][col]= "0"
      tablero[fila][col-1]= "0"
      return tablero
    elif fila == 0 and col in range(1,7):
      tablero[fila][col]= "0"
      tablero[fila+1][col]= "0"
      tablero[fila][col-1]= "0"
      tablero[fila][col+1]= "0"
      return tablero
    elif fila in 7 and col == range(1,7):
      tablero[fila][col]= "0"
      tablero[fila-1][col]= "0"
      tablero[fila][col-1]= "0"
      tablero[fila][col+1]= "0"
      return tablero
    elif fila in range(1,7) and col == 0:
      tablero[fila][col]= "0"
      tablero[fila-1][col]= "0"
      tablero[fila+1][col]= "0"
      tablero[fila][col+1]= "0"
      return tablero
    elif fila in range(1,7) and col == 7:
      tablero[fila][col]= "0"
      tablero[fila-1][col]= "0"
      tablero[fila+1][col]= "0"
      tablero[fila][col-1]= "0"
      return tablero
  # Disparo en equis (‘X’)
  elif d=="X":
    if fila in range(1,7) and col in range(1,7):
      tablero[fila][col]= "0"
      tablero[fila-1][col-1]= "0"
      tablero[fila+1][col+1]= "0"
      tablero[fila+1][col-1]= "0"
      tablero[fila-1][col+1]= "0"
      return tablero
    elif fila == 0 and col == 0:
      tablero[fila][col]= "0"
      tablero[fila+1][col+1]= "0"
      return tablero
    elif fila == 7 and col == 0:
      tablero[fila][col]= "0"
      tablero[fila-1][col+1]= "0"
      return tablero
    elif fila == 0 and col == 7:
      tablero[fila][col]= "0"
      tablero[fila+1][col-1]= "0"
      return tablero
    elif fila == 7 and col == 7:
      tablero[fila][col]= "0"
      tablero[fila-1][col-1]= "0"
      return tablero
    elif fila == 0 and col in range(1,7):
      tablero[fila][col]= "0"
      tablero[fila+1][col+1]= "0"
      tablero[fila+1][col-1]= "0"
      return tablero
    elif fila == 7 and col == range(1,7):
      tablero[fila][col]= "0"
      tablero[fila-1][col+1]= "0"
      tablero[fila-1][col-1]= "0"
      return tablero
    elif fila in range(1,7) and col == 0:
      tablero[fila][col]= "0"
      tablero[fila-1][col+1]= "0"
      tablero[fila+1][col+1]= "0"
      return tablero
    elif fila in range(1,7) and col == 7:
      tablero[fila][col]= "0"
      tablero[fila-1][col-1]= "0"
      tablero[fila+1][col-1]= "0"
      return tablero
  # Disparo en diagonal (‘/’)
  elif d=="/":
    if fila in range(1,7) and col in range(1,7):
      tablero[fila][col]= "0"
      tablero[fila-1][col+1]= "0"
      tablero[fila+1][col-1]= "0"
      return tablero
    elif fila == 0 and col == 0:
      tablero[fila][col]= "0"
      return tablero
    elif fila == 7 and col == 0:
      tablero[fila][col]= "0"
      tablero[fila-1][col+1]= "0"
      return tablero
    elif fila == 0 and col == 7:
      tablero[fila][col]= "0"
      tablero[fila+1][col-1]= "0"
      return tablero
    elif fila == 7 and col == 7:
      tablero[fila][col]= "0"
      return tablero
    elif fila == 0 and col in range(1,7):
      tablero[fila][col]= "0"
      tablero[fila+1][col-1]= "0"
      return tablero
    elif fila == 7 and col == range(1,7):
      tablero[fila][col]= "0"
      tablero[fila-1][col+1]= "0"
      return tablero
    elif fila in range(1,7) and col == 0:
      tablero[fila][col]= "0"
      tablero[fila-1][col+1]= "0"
      return tablero
    elif fila in range(1,7) and col == 7:
      tablero[fila][col]= "0"
      tablero[fila+1][col-1]= "0"
      return tablero
  # Disparo en diagonal inversa (‘\’)
  elif d=="\\":
    if fila in range(1,7) and col in range(1,7):
      tablero[fila][col] = "0"
      tablero[fila-1][col-1]= "0"
      tablero[fila+1][col+1] = "0"
      return tablero
    elif fila == 0 and col == 0:
      tablero[fila][col]= "0"
      tablero[fila+1][col+1] = "0"
      return tablero
    elif fila == 7 and col == 0:
      tablero[fila][col]= "0"
      return tablero
    elif fila == 0 and col == 7:
      tablero[fila][col]= "0"
      return tablero
    elif fila == 7 and col == 7:
      tablero[fila][col]= "0"
      tablero[fila-1][col-1]= "0"
      return tablero
    elif fila == 0 and col in range(1,7):
      tablero[fila][col]= "0"
      tablero[fila+1][col+1] = "0"
      return tablero
    elif fila == 7 and col == range(1,7):
      tablero[fila][col]= "0"
      tablero[fila-1][col-1]= "0"
      return tablero
    elif fila in range(1,7) and col == 0:
      tablero[fila][col]= "0"
      tablero[fila+1][col+1]= "0"
      return tablero
    elif fila in range(1,7) and col == 7:
      tablero[fila][col]= "0"
      tablero[fila-1][col-1]= "0"
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
    elif fila == 0 and col == 0:
      tablero[fila+1][col] = "0""
      tablero[fila][col+1] = "0"
      tablero[fila+1][col+1] = "0"
      return tablero
    elif fila == 7 and col == 0:
      tablero[fila-1][col] = "0"
      tablero[fila-1][col+1] = "0"
      tablero[fila][col+1] = "0"
      return tablero
    elif fila == 0 and col == 7:
      tablero[fila][col-1] = "0"
      tablero[fila+1][col-1] = "0"
      tablero[fila+1][col] = "0"
      return tablero
    elif fila == 7 and col == 7:
      tablero[fila-1][col-1] = "0"
      tablero[fila][col-1] = "0"
      tablero[fila-1][col] = "0"
      return tablero
    elif fila == 0 and col in range(1,7):
      tablero[fila][col-1] = "0"
      tablero[fila+1][col-1] = "0"
      tablero[fila+1][col] = "0"
      tablero[fila][col+1] = "0"
      tablero[fila+1][col+1] = "0"
      return tablero
    elif fila == 7 and col == range(1,7):
      tablero[fila-1][col-1] = "0"
      tablero[fila][col-1] = "0"
      tablero[fila-1][col] = "0"
      tablero[fila-1][col+1] = "0"
      tablero[fila][col+1] = "0"
      return tablero
    elif fila in range(1,7) and col == 0:
      tablero[fila-1][col] = "0"
      tablero[fila+1][col] = "0"
      tablero[fila-1][col+1] = "0"
      tablero[fila][col+1] = "0"
      tablero[fila+1][col+1] = "0"
      return tablero
    elif fila in range(1,7) and col == 7:
      tablero[fila-1][col-1] = "0"
      tablero[fila][col-1] = "0"
      tablero[fila+1][col-1] = "0"
      tablero[fila-1][col] = "0"
      tablero[fila+1][col] = "0"
      return tablero
  else:
    print("Disparo no existente")
    return tablero

#-------------------------Inicio del juego (menu)------------------------------
def menu(min_nave, coloca_barcos, muestra_tablero, disparos, m):
    modojuego=(input("Bienvenido a Batalla Naval: n\ Escoja el modo de juego: Automático (A) o Manual (M): "))
    tamano = 8
    if modojuego in "Aa":
        print("Tendrás 35 oportunidades de ataque para eliminar todas las naves en la pantalla.")
        print("El número restante de ataques se multiplica por diez y se convierte en tu puntuación final")
        print("Por lo tanto, cuanto más ataques te queden, más alta será tu puntuación. ¡Aprovecha la oportunidad para eliminar las naves!")
        Tablero = coloca_barcos(min_nave, m, tamano)
        muestra_tablero(Tablero,tamano)
        
        # Para acumular disparos
        borra = 0
        while True:
            if "X" in Tablero[0] or "X" in Tablero[1] or \
                "X" in Tablero[2] or "X" in Tablero[3] or \
                    "X" in Tablero[4] or "X" in Tablero[5] or \
                        "X" in Tablero[6] or "X" in Tablero[7]:
                disp_rand=0
                while disp_rand<min_nave:
                    lista_disparos = ["o","*","-","+","\\","/","X"]
                    d = rd.choice(lista_disparos)
                    print("Disparo actual: ", d) 
                    disp_rand+=1
                    fila = rd.randint(0, tamano-1)
                    col = rd.randint(0,tamano-1) 
                    Tablero = disparos(Tablero, d, fila, col)
                    muestra_tablero(Tablero,tamano)
                    borra+=1
            else: 
                print("El juego ha terminado. Es hora de calcular la \
                      puntuación")
                break
        
    elif modojuego in "Mm":
        min_nave = int(input("¿Cuántos barcos desea colocar?: "))
        Tablero = coloca_barcosmanual(min_nave, m, tamano)
        muestra_tablero(Tablero,tamano)

        borra = 0
        while True:
            if "X" in Tablero[0] or "X" in Tablero[1] or "X" in Tablero[2] or\
                "X" in Tablero[3] or "X" in Tablero[4] or "X" in Tablero[5] or\
                    "X" in Tablero[6] or "X" in Tablero[7]:
                d = (input("Introduce el tipo de disparo:\
                           (o, *, -, +, \, /, X)"))
                fila = int(input("Introduce la coordanada de la fila: "))-1
                col = int(input("Introduce la coordanada de la columna: "))-1
                Tablero = disparos(Tablero, d, fila, col)
                muestra_tablero(Tablero,tamano)
                borra+=1
            else: 
                print("El juego ha terminado. Es hora de calcular la \
                      puntuación")
                break
        else:
            print("Escoga uno de los modos")
            modojuego= (input("Bienvenido a \Batalla Naval: \n Escoja el \
                              modo de juego: Automático (A) o Manual (M): "))
    
    final = (35-borra)*10
    print("Your final grade is {}!".format(final))

# Inicializar el juego  
m = creaMatriz(tamano)
menu(min_nave, coloca_barcos, muestra_tablero, disparos, m)
