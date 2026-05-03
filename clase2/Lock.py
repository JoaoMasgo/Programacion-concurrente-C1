import threading
import time

contador = 0
lock = threading.Lock()
def sumar():
    global contador
    for _ in range(1000):
        with lock:
            temp = contador
            time.sleep(0.00001)
            temp += 1
            contador = temp

hilos = []

for i in range(2):
    h = threading.Thread(target=sumar)
    hilos.append(h)
    h.start()

for h in hilos:
    h.join()

print("Resultado:", contador)