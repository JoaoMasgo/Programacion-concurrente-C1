import time
import threading
"""
def saludar(nombre):
    time.sleep(1)
    print("Hola", nombre)

nombres = ["Ana", "Juan", "miguel", "luis"]

for nombre in nombres:
    saludar(nombre)
"""

def saludar(nombre):
    time.sleep(1)
    print("Hola", nombre)

nombres = ["Ana", "Juan", "Miguel", "LUIS"]
hilos = []

for nombre in nombres:
    h = threading.Thread(target=saludar, args=(nombre,))
    hilos.append(h) 
    h.start()

for h in hilos:
    h.join()