import threading
import time

def tarea(n):
    time.sleep(2)
    print("Termine", n)

threads = []

for i in range(3):
    thread = threading.Thread(target=tarea, args=(i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()