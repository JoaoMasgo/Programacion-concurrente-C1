import time
import threading

""" def tarea():
    time.sleep(2)
    print("ok")

for i in range(3):
    tarea()

 """

def tarea():
    time.sleep(2)
    print("ok")

hilos = []

for i in range(3):
    h = threading.Thread(target=tarea)
    hilos.append(h)
    h.start()

for h in hilos:
    h.join()