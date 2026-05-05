import time
"""
def enviar_mensaje(usuario, mensaje):
    time.sleep(1)
    print(usuario, "recibio:", mensaje)

usuarios = ["Juan", "Rosa", "Mati"]

for usuario in usuarios:
    enviar_mensaje(usuario, "hola")

"""

import threading

def enviar_mensaje(usuario, mensaje):
    time.sleep(1)
    print(usuario, "recibio:", mensaje)

usuarios = ["Juan", "Rosa", "Mati"]
threads = []

for usuario in usuarios:
    h = threading.Thread(target=enviar_mensaje, args=(usuario, "hola"))
    threads.append(h)
    h.start()

for thread in threads:
    thread.join()