import threading
import time

# Recurso compartido
dato = 0
# Variables de control
lectores = 0

# Primitivas de sincronización
mutex = threading.Lock()      # protege 'lectores'
escritor = threading.Lock()        # controla acceso al recurso

def lector(id):
    global lectores

    # Sección de entrada
    mutex.acquire()
    lectores += 1
    if lectores == 1:
        escritor.acquire()  # primer lector bloquea escritores
    mutex.release()

    # Sección crítica (lectura)
    print(f"Lector {id} lee {dato}")
    time.sleep(0.5)

    # Sección de salida
    mutex.acquire()
    lectores -= 1
    if lectores == 0:
        escritor.release()  # último lector libera escritores
    mutex.release()


def escritor(id):
    global dato

    # Sección de entrada
    escritor.acquire()

    # Sección crítica (escritura)
    dato += 1
    print(f"Escritor {id} escribe {dato}")
    time.sleep(0.5)

    # Sección de salida
    escritor.release()


# Creación de hilos (ejecución finita)
hilos = []

for i in range(3):
    t = threading.Thread(target=lector, args=(i,))
    hilos.append(t)

for i in range(2):
    t = threading.Thread(target=escritor, args=(i,))
    hilos.append(t)

# Ejecutar
for t in hilos:
    t.start()

for t in hilos:
    t.join()

print("Fin")