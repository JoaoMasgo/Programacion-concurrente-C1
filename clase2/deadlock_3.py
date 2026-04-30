import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def tarea_1():
    with lock_a:        
        print("Tarea 1 tiene Lock A, esperando Lock B...")
        time.sleep(0.1) 
        if lock_b.acquire(timeout=1):
            try:                
                print("Tarea 1 logró obtener ambos")
            finally:
                lock_b.release()    
    
def tarea_2():
    with lock_b:        
        print("Tarea 2 tiene Lock B, esperando Lock A...")
        time.sleep(0.1)
        if lock_a.acquire(1):
            try:                
                print("Tarea 2 logró obtener ambos")
            finally:
                lock_a.release()    
     

h1 = threading.Thread(target=tarea_1)
h2 = threading.Thread(target=tarea_2)

h1.start()
h2.start()