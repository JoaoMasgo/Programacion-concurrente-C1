import threading
import time

semaforo = threading.Semaphore(2)

def tarea(id):
    print(f"Hilo {id} esperando...")
    
    semaforo.acquire()
    print(f"Hilo {id} entrando")
    
    time.sleep(2)  # simula trabajo
    
    print(f"Hilo {id} saliendo")
    semaforo.release()
    semaforo.release()
    print(semaforo._value)

hilos = []

for i in range(5):
    t = threading.Thread(target=tarea, args=(i,))
    hilos.append(t)
    t.start()
    
for t in hilos:
    t.join()