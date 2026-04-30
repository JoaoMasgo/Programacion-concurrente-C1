import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def tarea_1():
    with lock_a:
        with lock_b:
            print("Tarea 1 tiene Lock A, esperando Lock B...")
            time.sleep(0.1)             
            print("Tarea 1 logró obtener ambos")

def tarea_2():
    with lock_a:
        with lock_b:
            print("Tarea 2 tiene Lock B, esperando Lock A...")
            time.sleep(0.1)          
            print("Tarea 2 logró obtener ambos")

h1 = threading.Thread(target=tarea_1)
h2 = threading.Thread(target=tarea_2)

h1.start()
h2.start()