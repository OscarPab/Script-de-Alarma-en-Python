# Script de Alarma en Python

Este proyecto contiene un script de Python que permite establecer una alarma a una hora específica. El script realiza las siguientes funciones:

1. **Obtener la hora actual:** Utiliza la biblioteca `datetime` para obtener la hora actual y formatearla en `HH:MM`.
2. **Comparar la hora actual con la hora de la alarma:** Verifica si la hora actual coincide con la hora de la alarma establecida.
3. **Reproducir un sonido de alarma:** Utiliza la biblioteca `os` para reproducir un archivo de sonido (`alarma.mp3`) cuando la hora de la alarma se alcanza.
4. **Esperar un minuto antes de verificar nuevamente:** Utiliza la biblioteca `time` para esperar un minuto antes de hacer una nueva verificación.

## Requisitos

- Python 3.x

## Uso

Ejecuta el script y proporciona la hora de la alarma en formato `HH:MM`:

```sh
python establecer_alarma.py
