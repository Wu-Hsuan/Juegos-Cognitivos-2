import module as m

#menu
def menu():
    modojuego=(input("Bienvenido a Batalla Naval: n\ Escoja el modo de juego: Automático (A) o Manual (M): "))
    if modojuego in "Aa":
        coloca_barcos(min_nave, m, tamano)
    elif modojuego in "Mm":
        coloca_barcosmanual(min_nave, m, tamano)
    else:
        print("Escoga uno de los modos")
        modojuego= (input("Bienvenido a Batalla Naval: n\ Escoja el modo de juego: Automático (A) o Manual (M): ")) 

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
