import threading

x = 0
lock = threading.Lock()

def tarea():
    global x
    for _ in range(1000):
        with lock:
            x += 1
            print(x)

hilos = []

for i in range(2):
    h = threading.Thread(target=tarea)
    hilos.append(h)
    h.start()

for h in hilos:
    h.join()