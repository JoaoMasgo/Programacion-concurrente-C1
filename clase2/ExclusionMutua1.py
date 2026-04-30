import threading
import time

contador = 0
lock_contador = threading.Lock()
def incrementar(hilo):
    global contador
    time.sleep(1)
    for _ in range(100):        
        print(hilo)      
        lock_contador.acquire() # Adquirimos el lock (cierra el candado)
        try: 
            temp = contador   
            time.sleep(0.00001)
            temp += 1          
            contador = temp
        finally:               # Se ejecuta SIEMPRE, incluso si ocurre un error  
            lock_contador.release()   # Libera el lock (abre el candado)    
                                    

h1 = threading.Thread(target=incrementar, args=("h1",))
h2 = threading.Thread(target=incrementar, args=("h2",))

h1.start()
h2.start()

h1.join()
h2.join()

print(contador)


