import time
"""
def tarea(n):
    print("Inicio tarea", n)
    time.sleep(2)
    print("Fin tarea", n)

for i in range(4):
    tarea(i)

"""
import threading

def tarea(n):
    print("Inicio tarea", n)
    time.sleep(2)
    print("Fin tarea", n)

threads = []

for i in range(4):
    h = threading.Thread(target=tarea, args=(i,))

    threads.append(h)
    h.start()

for thread in threads:
    thread.join()