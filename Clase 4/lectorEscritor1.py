import threading
import time
import random

dato = 0
lectores = 0

mutex = threading.Lock() #protege el dato
escritor = threading.Lock() 

def lector(id, repeticiones):
    global lectores

    for _ in range(repeticiones):
        time.sleep(random.uniform(0.5, 1.5))

        # Entrada
        with mutex:
            lectores += 1
            if lectores == 1:
                escritor.acquire()

        # Sección crítica
        print(f"Lector {id} lee dato = {dato}")
        time.sleep(0.5)

        # Salida
        with mutex:
            lectores -= 1
            if lectores == 0:
                escritor.release()


def escritor_func(id, repeticiones):
    global dato

    for _ in range(repeticiones):
        time.sleep(random.uniform(1, 2))

        with escritor:
            dato += 1
            print(f"Escritor {id} escribe dato = {dato}")
            time.sleep(1)


# Crear hilos
hilos = []

for i in range(3):
    t = threading.Thread(target=lector, args=(i, 3))
    hilos.append(t)
    t.start()

for i in range(2):
    t = threading.Thread(target=escritor_func, args=(i, 2))
    hilos.append(t)
    t.start()

# Esperar a que todos terminen
for t in hilos:
    t.join()

print("Fin del programa")