import threading
import time

sem = threading.Semaphore(2)

def tarea(n):
    with sem:
        print("Entra", n)
        time.sleep(2)
        print("Sale", n)


threads = []

for i in range(5):
    h = threading.Thread(target=tarea, args=(i,))
    threads.append(h)
    h.start()

for thread in threads:
    thread.join()

#El semaphore se utiliza principalmente para controlar 
# el acceso a recursos limitados, mientras que el lock se utiliza para proteger secciones críticas.