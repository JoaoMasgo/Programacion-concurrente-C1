import threading
import time

dato = 0

lectores_activos = 0
escribiendo = False
flagAvisarQueQuieroEscribir = False
cond = threading.Condition()

# Problema actual: el hilo del escritor puede morir de inanción !!!!
# Solución: darle prioridad al hilo escritor !!!!
def lector(id):
    global lectores_activos, escribiendo, flagAvisarQueQuieroEscribir

    with cond:
        while escribiendo or flagAvisarQueQuieroEscribir:
            cond.wait()  # espera si hay un escritor activo
        lectores_activos += 1

    # Sección crítica
    print(f"Lector {id} lee {dato}")
    time.sleep(0.5)

    with cond:
        lectores_activos -= 1
        if lectores_activos == 0:
            cond.notify_all()  # despierta escritores


def escritor(id):
    global dato, escribiendo, flagAvisarQueQuieroEscribir

    with cond:
        flagAvisarQueQuieroEscribir = True
        while lectores_activos > 0 or escribiendo:
            cond.wait()  # espera si hay lectores o escritor
        escribiendo = True 
        flagAvisarQueQuieroEscribir = False

    # Sección crítica
    dato += 1
    print(f"Escritor {id} escribe {dato}")
    time.sleep(0.5)

    with cond:
        escribiendo = False
        cond.notify_all()  # despierta a todos


# Hilos
hilos = []

for i in range(3):
    hilos.append(threading.Thread(target=lector, args=(i,)))

for i in range(2):
    hilos.append(threading.Thread(target=escritor, args=(i,)))

for t in hilos:
    t.start()

for t in hilos:
    t.join()

print("Fin")
