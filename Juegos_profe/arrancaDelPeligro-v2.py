import os
import time
import keyboard

def dibujar_mapa(pos_jugador, obstaculos, mensaje="Explorando..."):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== AVENTURA INTERACTIVA V2: OBSTÁCULOS ===")
    print("Controles: [W][A][S][D] | [ESC] Salir")
    print("Leyenda: [P] Jugador | [#] Obstáculo | [ ] Vacío")
    print("===========================================\n")
    
    for fila in range(5):
        linea_mapa = ""
        for columna in range(5):
            # 1. ¿Está el jugador aquí?
            if pos_jugador == [fila, columna]:
                linea_mapa += " [P] "
            # 2. ¿Hay un obstáculo en esta coordenada?
            elif [fila, columna] in obstaculos:
                linea_mapa += " [#] "
            # 3. Si no hay nada, suelo vacío
            else:
                linea_mapa += " [ ] "
        print(linea_mapa)
    
    print("\n===========================================")
    print(f"EVENTO: {mensaje}")

# --- CONFIGURACIÓN ---
posicion = [4, 2]
# Definimos una lista de listas con las coordenadas de las "paredes"
paredes = [[1, 1], [1, 2], [1, 3], [3, 0], [3, 1], [3, 3], [3, 4]]
mensaje_evento = "¡Cuidado con los muros [#]!"

dibujar_mapa(posicion, paredes, mensaje_evento)

while True:
    # Guardamos la posición actual por si chocamos y debemos "rebotar"
    nueva_fila = posicion[0]
    nueva_col = posicion[1]
    movio = False

    if keyboard.is_pressed('w'):
        if nueva_fila > 0: nueva_fila -= 1
        movio = True
    elif keyboard.is_pressed('s'):
        if nueva_fila < 4: nueva_fila += 1
        movio = True
    elif keyboard.is_pressed('a'):
        if nueva_col > 0: nueva_col -= 1
        movio = True
    elif keyboard.is_pressed('d'):
        if nueva_col < 4: nueva_col += 1
        movio = True
    elif keyboard.is_pressed('esc'):
        break

    if movio:
        # --- LÓGICA DE COLISIÓN ---
        # Verificamos si la nueva posición tentativa está en nuestra lista de paredes
        if [nueva_fila, nueva_col] in paredes:
            mensaje_evento = "¡PUM! Chocaste con una roca."
        else:
            # Si no hay pared, actualizamos la posición real
            posicion = [nueva_fila, nueva_col]
            mensaje_evento = "Caminando con cuidado..."
        
        dibujar_mapa(posicion, paredes, mensaje_evento)
        time.sleep(0.2)

    # Condición de victoria
    if posicion == [0, 4]:
        mensaje_evento = "¡LLEGASTE A LA META!"
        dibujar_mapa(posicion, paredes, mensaje_evento)
        time.sleep(2)
        break