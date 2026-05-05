import threading
import time

dato = 0

lectores_activos = 0
escribiendo = False
turno_escritor = False  # alternancia para evitar starvation

cond = threading.Condition()

def lector(id):
    global lectores_activos, escribiendo, turno_escritor

    with cond:
        # Espera si hay escritor activo o si es turno de escritor
        while escribiendo or turno_escritor:
            cond.wait()
        lectores_activos += 1

    # Sección crítica
    print(f"[Lector {id}] lee {dato}")
    time.sleep(0.5)

    with cond:
        lectores_activos -= 1
        if lectores_activos == 0:
            turno_escritor = True  # damos turno a escritores
            cond.notify_all()


def escritor(id):
    global dato, lectores_activos, escribiendo, turno_escritor

    with cond:
        # Espera si hay lectores o escritor activo
        while lectores_activos > 0 or escribiendo:
            cond.wait()
        escribiendo = True

    # Sección crítica
    print(f">>> Escritor {id} escribe {dato} <<<")
    dato += 1
    time.sleep(1)

    with cond:
        escribiendo = False
        turno_escritor = False  # devolvemos turno a lectores
        cond.notify_all()


# Crear hilos
hilos = []

for i in range(5):
    hilos.append(threading.Thread(target=lector, args=(i,)))

for i in range(3):
    hilos.append(threading.Thread(target=escritor, args=(i,)))

# Ejecutar
for t in hilos:
    t.start()

for t in hilos:
    t.join()

print("Fin")