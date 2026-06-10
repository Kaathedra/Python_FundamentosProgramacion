# --- SECCIÓN DE IMPORTACIÓN ---
# Traemos herramientas que no vienen activadas por defecto
import os     # Para interactuar con el sistema operativo (limpiar la pantalla)
import time   # Para manejar pausas de tiempo
import keyboard  # Para detectar teclas al instante (requiere: pip install keyboard)

# --- DEFINICIÓN DE FUNCIONES ---
# Creamos nuestra propia instrucción para "dibujar" el mapa en la consola
def dibujar_mapa(pos_jugador, mensaje="Explorando la montaña..."):
    # Limpiamos la consola para dar efecto de animación (borra lo anterior)
    # 'cls' es para Windows, 'clear' para Mac o Linux
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=== AVENTURA INTERACTIVA ===")
    print("Controles: [W][A][S][D] para mover | [ESC] para salir")
    print("============================\n")
    
    # El mapa es una cuadrícula de 5x5 (Filas x Columnas)
    for fila in range(5):          # Recorremos cada piso (fila)
        linea_mapa = ""            # Empezamos la fila vacía
        for columna in range(5):   # Recorremos cada puerta (columna) de esa fila
            # Si las coordenadas actuales coinciden con la posición del jugador...
            if pos_jugador == [fila, columna]:
                linea_mapa += " [P] " # Dibujamos al Personaje
            else:
                linea_mapa += " [ ] " # Dibujamos suelo vacío
        print(linea_mapa)          # Al terminar la fila, la mostramos en pantalla
    
    print("\n============================")
    # Mostramos el mensaje dinámico que cambia según lo que pase
    print(f"EVENTO: {mensaje}")

# --- CONFIGURACIÓN INICIAL ---
# Guardamos la ubicación del jugador en una lista [Fila, Columna]
# Empezamos en la fila 4 (abajo) y columna 2 (centro)
posicion = [4, 2]
mensaje_evento = "Estás en la base. Muévete para comenzar."

# Dibujamos el estado inicial antes de entrar al ciclo
dibujar_mapa(posicion, mensaje_evento)

# --- CICLO PRINCIPAL (Game Loop) ---
# Un ciclo infinito para que el juego esté siempre "escuchando" al jugador
while True:
    
    # Detectamos si se presiona la tecla 'W' (Hacia Arriba)
    if keyboard.is_pressed('w'):
        # Validamos que no se salga del mapa (la fila mínima es 0)
        if posicion[0] > 0: 
            posicion[0] -= 1  # Restamos 1 a la fila para subir
            mensaje_evento = "Avanzas hacia el norte..."
        # Redibujamos con la nueva información
        dibujar_mapa(posicion, mensaje_evento)
        # Pausa de 0.2 seg para que un toque no mueva al jugador 10 veces
        time.sleep(0.2) 

    # Detectamos tecla 'S' (Hacia Abajo)
    elif keyboard.is_pressed('s'):
        # Validamos límite inferior (máximo fila 4)
        if posicion[0] < 4: 
            posicion[0] += 1  # Sumamos 1 a la fila para bajar
            mensaje_evento = "Retrocedes con cuidado..."
        dibujar_mapa(posicion, mensaje_evento)
        time.sleep(0.2)

    # Detectamos tecla 'A' (Hacia la Izquierda)
    elif keyboard.is_pressed('a'):
        # Validamos límite izquierdo (mínimo columna 0)
        if posicion[1] > 0: 
            posicion[1] -= 1  # Restamos 1 a la columna
            mensaje_evento = "Te mueves a la izquierda..."
        dibujar_mapa(posicion, mensaje_evento)
        time.sleep(0.2)

    # Detectamos tecla 'D' (Hacia la Derecha)
    elif keyboard.is_pressed('d'):
        # Validamos límite derecho (máximo columna 4)
        if posicion[1] < 4: 
            posicion[1] += 1  # Sumamos 1 a la columna
            mensaje_evento = "Te mueves a la derecha..."
        dibujar_mapa(posicion, mensaje_evento)
        time.sleep(0.2)

    # Opción para cerrar el programa manualmente
    elif keyboard.is_pressed('esc'):
        print("\nSaliendo del juego...")
        break # Rompe el ciclo 'while' y termina el código

    # --- LÓGICA DE EVENTOS ESPECIALES ---
    # Revisamos si el jugador llegó a una coordenada específica
    if posicion == [0, 0]: # Esquina superior izquierda
        mensaje_evento = "¡HAS LLEGADO A LA CIMA! Victoria."
        dibujar_mapa(posicion, mensaje_evento)
        time.sleep(2) # Pausa dramática antes de cerrar
        break # Terminamos el juego por victoria