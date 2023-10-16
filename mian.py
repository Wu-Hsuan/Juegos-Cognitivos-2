import module as m

# datos basicos para funcionar las funciones
tamano = 8
min_nave = int(tamano*tamano*0.55/1)
m = creaMatriz(tamano)

modojuego=(input("Bienvenido a Batalla Naval: n\ Escoja el modo de juego: Automático (A) o Manual (M): "))


if modojuego in "Aa":
    print("Tendrás 35 oportunidades de ataque para eliminar todas las naves en la pantalla.")
    print("El número restante de ataques se multiplica por diez y se convierte en tu puntuación final")
    print("Por lo tanto, cuanto más ataques te queden, más alta será tu puntuación. ¡Aprovecha la oportunidad para eliminar las naves!")
    Tablero = m.coloca_barcos(min_nave, m, tamano)
    m.muestra_tablero(Tablero,tamano)
    borra = 0
    while True:
      if "X" in Tablero[0] or "X" in Tablero[1] or "X" in Tablero[2] or "X" in Tablero[3] or "X" in Tablero[4] or "X" in Tablero[5] or "X" in Tablero[6] or "X" in Tablero[7]:
        Tablero = m.disparos(Tablero)
        m.muestra_tablero(Tablero,tamano)
        borra+=1
      else: 
        print("El juego ha terminado. Es hora de calcular la puntuación")
        break
elif modojuego in "Mm":
    tablero = m.coloca_barcosmanual(min_nave, m, tamano)
    m.muestra_tablero(tablero,tamano)
else:
    print("Escoga uno de los modos")
    modojuego= (input("Bienvenido a Batalla Naval: n\ Escoja el modo de juego: Automático (A) o Manual (M): "))



#print(tablero)
