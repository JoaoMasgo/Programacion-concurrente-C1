import threading
import time

def tarea():
    time.sleep(2)
    print("Tarea terminada")

inicio = time.time()

hilos = []

for i in range(3):
    h = threading.Thread(target=tarea)
    hilos.append(h)
    h.start()

for h in hilos:
    h.join()

fin = time.time()

print("Tiempo:", fin - inicio)