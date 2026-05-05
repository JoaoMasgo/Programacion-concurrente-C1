import threading
import time

dato = 0
lectores = 0

mutex = threading.Lock()
wrt = threading.Lock()

def lector(id):
    global lectores

    for _ in range(5):
        # Entrada
        with mutex:
            lectores += 1
            if lectores == 1:
                wrt.acquire()

        print(f"[Lector {id}] leyendo dato = {dato}")
        time.sleep(0.2)

        # Salida
        with mutex:
            lectores -= 1
            if lectores == 0:
                wrt.release()

        #  Muy poca pausa → llegan lectores constantemente
        time.sleep(0.1)


def escritor(id):
    global dato

    print(f"--- Escritor {id} quiere escribir ---")

    wrt.acquire()  # puede quedar bloqueado mucho tiempo

    print(f">>> Escritor {id} ENTRA a escribir <<<")
    dato += 1
    time.sleep(1)

    print(f">>> Escritor {id} SALE <<<")
    wrt.release()


# Crear muchos lectores
hilos = []

for i in range(8):
    t = threading.Thread(target=lector, args=(i,))
    hilos.append(t)

# Un solo escritor
t_escritor = threading.Thread(target=escritor, args=(1,))
hilos.append(t_escritor)

# Arrancar primero lectores
for t in hilos[:-1]:
    t.start()

time.sleep(0.3)  # damos ventaja a lectores

# Arrancar escritor
t_escritor.start()

# Esperar
for t in hilos:
    t.join()

print("Fin")