import threading
import time

saldo = 1000

def retirar():
    global saldo
    for _ in range(100):
        temp = saldo
        time.sleep(0.00001)
        temp -= 1
        saldo = temp

hilos = []

for i in range(2):
    h = threading.Thread(target=retirar)
    hilos.append(h)
    h.start()

for h in hilos:
    h.join()

print("Saldo final:", saldo)