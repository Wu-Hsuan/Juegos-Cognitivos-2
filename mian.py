import module as m

modojuego=(input("Bienvenido a Batalla Naval: n\ Escoja el modo de juego: Automático (A) o Manual (M): "))
if modojuego in "Aa":
    coloca_barcos(min_nave, m, tamano)
elif modojuego in "Mm":
    coloca_barcosmanual(min_nave, m, tamano)
else:
    print("Escoga uno de los modos")
    modojuego= (input("Bienvenido a Batalla Naval: n\ Escoja el modo de juego: Automático (A) o Manual (M): ")) 


