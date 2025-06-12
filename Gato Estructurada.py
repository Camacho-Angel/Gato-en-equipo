import os

def imprimir_tablero(tablero):
    print("\n      ||     ||     ")
    print(f"   {tablero[0][0]}  ||  {tablero[0][1]}  ||  {tablero[0][2]}")
    print("     1||    2||    3")
    print(" =====++=====++======")
    print("      ||     ||     ")
    print(f"   {tablero[1][0]}  ||  {tablero[1][1]}  ||  {tablero[1][2]}")
    print("     4||    5||    6")
    print(" =====++=====++======")
    print("      ||     ||     ")
    print(f"   {tablero[2][0]}  ||  {tablero[2][1]}  ||  {tablero[2][2]}")
    print("     7||    8||    9\n")

def verificar_ganador(tab1, valor):
    for i in range(3):
        if all(tab1[i][j] == valor for j in range(3)) or all(tab1[j][i] == valor for j in range(3)):
            return True
    if tab1[0][0] == valor and tab1[1][1] == valor and tab1[2][2] == valor:
        return True
    if tab1[0][2] == valor and tab1[1][1] == valor and tab1[2][0] == valor:
        return True
    return False

def gato(contador):
    tab1 = [[0 for _ in range(3)] for _ in range(3)]
    tab2 = [[" " for _ in range(3)] for _ in range(3)]

    turno_jugador1 = True
    terminado = False
    ganador = False
    cant_turnos = 0

    while not terminado:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=== Partida número {contador} ===\n")
        imprimir_tablero(tab2)

        if not ganador and cant_turnos < 9:
            if turno_jugador1:
                ficha = 'X'
                valor = 1
                print("Turno del jugador 1 (X)")
            else:
                ficha = 'O'
                valor = 2
                print("Turno del jugador 2 (O)")

            while True:
                try:
                    pos = int(input("Ingrese la posición (1-9): "))
                    if pos < 1 or pos > 9:
                        print("Posición fuera de rango, intente nuevamente.")
                        continue
                    i = (pos - 1) // 3
                    j = (pos - 1) % 3
                    if tab1[i][j] != 0:
                        print("Esa posición ya está ocupada, intente otra.")
                        continue
                    break
                except ValueError:
                    print("Debe ingresar un número válido del 1 al 9.")

            cant_turnos += 1
            tab1[i][j] = valor
            tab2[i][j] = ficha

            ganador = verificar_ganador(tab1, valor)

            if not ganador:
                turno_jugador1 = not turno_jugador1

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            imprimir_tablero(tab2)
            if ganador:
                if turno_jugador1:
                    print("Ganador: Jugador 1!")
                    return 1
                else:
                    print("Ganador: Jugador 2!")
                    return 2
            else:
                print("¡Empate!")
                return 0

# Bucle principal con contadores de victoria
contador_partidas = 1
victorias_j1 = 0
victorias_j2 = 0
empates = 0

while True:
    resultado = gato(contador_partidas)

    if resultado == 1:
        victorias_j1 += 1
    elif resultado == 2:
        victorias_j2 += 1
    else:
        empates += 1

    print(f"\nMarcador actual:")
    print(f"Jugador 1: {victorias_j1} victoria(s)")
    print(f"Jugador 2: {victorias_j2} victoria(s)")
    print(f"Empates: {empates}")

    contador_partidas += 1
    jugar_otra = input("\n¿Deseas jugar otra partida? (s/n): ").strip().lower()
    if jugar_otra != 's':
        print("Gracias por jugar. ¡Hasta la próxima!")
        break

