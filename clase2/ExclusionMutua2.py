import threading
import time

contador = 0
# Creamos la primitiva Lock
lock_contador = threading.Lock()
def incrementar(hilo):
    global contador
    time.sleep(1)
    for _ in range(100):        
        print(hilo)      
        with lock_contador:  # El bloque 'with' adquiere y libera el lock automáticamente
            temp = contador   
            time.sleep(0.00001)
            temp += 1          
            contador = temp

        # al finalizar el bloque se sibera el lock    

h1 = threading.Thread(target=incrementar, args=("h1",))
h2 = threading.Thread(target=incrementar, args=("h2",))

h1.start()
h2.start()

h1.join()
h2.join()

print(contador)


