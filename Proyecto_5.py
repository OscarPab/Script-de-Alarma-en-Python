import datetime
import time
import os

def establecer_alarma(hora_alarma):
    while True:
        # Obtener la hora actual
        hora_actual = datetime.datetime.now().strftime("%H:%M")
        print(f"Hora actual: {hora_actual}", end="\r")
        
        # Comparar la hora actual con la hora de la alarma
        if hora_actual == hora_alarma:
            print("\n¡Es hora de despertar!")
            # Reproducir un sonido de alarma
            os.system("start alarma.mp3")  # En Windows
            # os.system("afplay alarma.mp3")  # En macOS
            # os.system("mpg123 alarma.mp3")  # En Linux
            break
        
        # Esperar un minuto antes de verificar nuevamente
        time.sleep(60)

# Solicitar al usuario que ingrese la hora de la alarma
hora_alarma = input("Introduce la hora de la alarma (HH:MM): ")
establecer_alarma(hora_alarma)
