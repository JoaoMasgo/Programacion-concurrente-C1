import threading
import time
import random

# Definimos un semáforo que permite máximo 3 hilos a la vez
semaforo = threading.Semaphore(3)
hilos = []
def conectar_a_base_de_datos(id_hilo):
    print(f"--- Hilo {id_hilo} esperando para conectar...")
    
    with semaforo:
        # SECCIÓN CRÍTICA
        print(f" [OK] Hilo {id_hilo} ha entrado a la base de datos.")
        time.sleep(random.uniform(1, 3)) # Simula trabajo
        print(f" [!] Hilo {id_hilo} saliendo y liberando conexión.")

# Creamos 5 hilos que quieren entrar al mismo tiempo
for i in range(5):
    t = threading.Thread(target=conectar_a_base_de_datos, args=(i,))
    hilos.append(t)
    t.start()

for i in range(5):
    t.join()    

