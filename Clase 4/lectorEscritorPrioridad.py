import threading
import time

dato = 0

lectores_activos = 0
escritores_esperando = 0
escribiendo = False

cond = threading.Condition()

def lector(id):
    global lectores_activos, escribiendo, escritores_esperando

    with cond:
        # Si hay un escritor escribiendo o esperando → NO entra
        while escribiendo or escritores_esperando > 0:
            cond.wait()
        lectores_activos += 1

    # Sección crítica (lectura)
    print(f"[Lector {id}] lee {dato}")
    time.sleep(0.5)

    with cond:
        lectores_activos -= 1
        if lectores_activos == 0:
            cond.notify_all()  # puede despertar escritores


def escritor(id):
    global dato, lectores_activos, escribiendo, escritores_esperando

    with cond:
        escritores_esperando += 1

        while lectores_activos > 0 or escribiendo:
            cond.wait()

        escritores_esperando -= 1
        escribiendo = True

    # Sección crítica (escritura)
    print(f">>> Escritor {id} escribe <<<")
    dato += 1
    time.sleep(1)

    with cond:
        escribiendo = False
        cond.notify_all()  # despierta lectores o escritores


# Crear hilos
hilos = []

for i in range(5):
    hilos.append(threading.Thread(target=lector, args=(i,)))

for i in range(2):
    hilos.append(threading.Thread(target=escritor, args=(i,)))

# Ejecutar
for t in hilos:
    t.start()

for t in hilos:
    t.join()

print("Fin")