import random
#Define el tamaño del tablero(matriz)
tamaño=8

#Calcula la cantidad de mínima de barcos para llenar más del 50% del tablero
minimo_nave=int(tamaño*tamaño*0.55/1)

#Funcion para hacer
def Matriz(tamaño):
    renglones=tamaño
    columnas=tamaño
    matriz = [ ]
    for ren in range (renglones):
        lista=[ ]
        for col in range(columnas):
            dato=0
            lista.append(dato)
            #hasta aqui se crea el renglon   
        matriz.append(lista)
    return matriz

#Función que coloca barcos aleatorios de tamaño 1 que crea en el tablero
def coloca_barco(minimo_nave,m,tamaño):
    barco_puesto=0
    while barco_puesto<minimo_nave:
        fila=random.randint(0, tamaño-1)
        col=random.randint(0, tamaño-1)
        if m[fila][col]==0:
            m[fila][col]="X"
            barco_puesto+=1
    return m

#Muestra la matriz como tablero
def mostrar_tablero(tablero, tamaño):
    print("  ", end="")
    for i in range(tamaño):
        print(i+1, end=" ")
    print("")
    for fila in range(tamaño):
        print(fila+1, end=" " )
        for col in range(tamaño):
            print(tablero[fila][col], end=" ")
        print(" ")

# Selecciona de los diferentes disparos con condiciones adicionales
def disparos(m, tamaño,):
    d= (input("Introduce el tipo de disparo: (o, *, -, +, \\, /, X)"))
    fila= int(input("Introduce la coordanada de la fila: "))
    col= int(input("Introduce la coordanada de la columna: "))
    
    # Disparo simple (‘-’)
    if d=="-":
        tablero[fila][col]== "0"
        return tablero
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
        return tablero
    # Disparo en cruz (‘+’)
    elif d=="+":
        tablero[fila][col]== "0"
        tablero[fila-1][col]== "0"
        tablero[fila+1][col]== "0"
        tablero[fila][col-1]== "0"
        tablero[fila][col+1]== "0"
        return tablero
    # Disparo en equis (‘X’)
    elif d=="X":
        tablero[fila][col]== "0"
        tablero[fila-1][col-1]== "0"
        tablero[fila+1][col+1]== "0"
        tablero[fila-1][col-1]== "0"
        tablero[fila-1][col+1]== "0"
        return tablero
    # Disparo en diagonal (‘/’)
    elif d=="/":
        tablero[fila][col]== "0"
        tablero[fila-1][col+1]== "0"
        tablero[fila+1][col-1]== "0"
        return tablero
    # Disparo en diagonal inversa (‘\’)
    elif d=="\\":
        tablero[fila][col] == "0"
        tablero[fila-1][col-1] == "0"
        tablero[fila+1][col+1] == "0"
        return tablero
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
      return tablero
    else:
        print("Disparo no existente")
    
    
        
    
#Función para escoger aleatoriamente el disparo en modo automático
def tiro_random(minimo_nave,m,tamaño, disparos):
    disp_rand=0
    while disp_rand<minimo_nave:
        lista_disparos = ["o","*","-","+","\\","/","X"]
        disp_aleatorio = random.choice(lista_disparos)
        print("Disparo actual: ", disp_aleatorio)
        disp_rand+=1
        disparos
    return m



#-------------------------Inicio del juego (menu)------------------------------
def menu(m, tablero, mostrar_tablero, disparos, minimo_nave,tiro_random):
    modojuego=(input("Bienvenido a Batalla Naval: \n Escoja el modo de juego: Automático (A) o Manual (M): "))
    if modojuego in "Aa":
        print("Se jugará solo en juego")
        mostrar_tablero(tablero,tamaño)
        disparos(tablero, tamaño)
        tiro_random(minimo_nave, m, tamaño)
        # Para acumular disparos
        borra = 0
        while True:
            if "X" in tablero[0] or "X" in tablero[1] or "X" in tablero[2] or "X" in tablero[3] or "X" in tablero[4] or "X" in tablero[5] or "X" in tablero[6] or "X" in tablero[7]:
                borra+=1
            else: 
                print("El juego ha terminado. Es hora de calcular la puntuación")
                break
    elif modojuego in "Mm":
        print("Tendrás 35 oportunidades de ataque para eliminar todas las naves en la pantalla.")
        print("El número restante de ataques se multiplica por diez y se convierte en tu puntuación final")
        print("Por lo tanto, cuanto más ataques te queden, más alta será tu puntuación. ¡Aprovecha la oportunidad para eliminar las naves!")
        mostrar_tablero(tablero,tamaño)
        disparos(tablero, tamaño)
        borra = 0
        while True:
            if "X" in tablero[0] or "X" in tablero[1] or "X" in tablero[2] or "X" in tablero[3] or "X" in tablero[4] or "X" in tablero[5] or "X" in tablero[6] or "X" in tablero[7]:
                
                borra+=1
            else: 
                print("El juego ha terminado. Es hora de calcular la puntuación")
                break
        else:
            print("Escoga uno de los modos")
            modojuego= (input("Bienvenido a Batalla Naval: n\ Escoja el modo de juego: Automático (A) o Manual (M): "))
            
    final = (35-borra)*10
    print("Your final grade is {}!".format(final))

#Inicializar el tablero
m=Matriz(tamaño)
tablero=coloca_barco(minimo_nave,m,tamaño)
menu(m,tablero,mostrar_tablero,disparos, minimo_nave, tiro_random)

