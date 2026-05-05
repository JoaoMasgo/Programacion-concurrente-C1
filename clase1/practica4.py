import time
"""
def procesar_imagen(nombre):
    print("Procensando", nombre)
    time.sleep(3)
    print(nombre, "lista")

imagenes = ["img1.png", "img2.png", "img3.png"]

for img in imagenes:
    procesar_imagen(img)

"""
import threading
def procesar_imagen(nombre):
    print("Procesando", nombre)
    time.sleep(3)
    print(nombre, "lista")


imagenes = ["img1.png", "img2.png", "img3.png"]
hilos = []
for img in imagenes:
    h = threading.Thread(target=procesar_imagen, args=(img,))
    hilos.append(h)
    h.start()

for h in hilos:
    h.join()