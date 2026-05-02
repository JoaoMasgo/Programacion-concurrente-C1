import time
""""
def descargar_archivo(numero):
    print("Descargar archivo", numero)
    time.sleep(2)
    print("aRCHIVO", numero, "descargado")

for i in range(5):
    descargar_archivo(i)
"""

import threading

def descargar_archivo(numero):
    print("Descargar archivo", numero)
    time.sleep(2)
    print("Archivo", numero, "descargado")

hilos = []

for i in range(5):
    h = threading.Thread(target=descargar_archivo, args=(i,))
    hilos.append(h)
    h.start()

for hilo in hilos:
    hilo.join()