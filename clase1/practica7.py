import threading
import time

def tarea(n):
    time.sleep(1)
    print("Tarea", n)

threads = []

for i in range(3):
    h = threading.Thread(target=tarea, args=(i,))
    h.start()

for thread in threads:
    thread.join()