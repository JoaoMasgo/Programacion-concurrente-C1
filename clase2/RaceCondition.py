"""
x = 0

def tarea():
    global x
    x += 1
    print(x)
explicar:
x = 0

hilo1 lee x = 0
hilo2 lee x = 0

hilo1 suma y guarda x = 1
hilo1 imprime 1

hilo2 suma y guarda x = 1
hilo2 imprime 1
"""
import threading
import time

contador = 0
def incrementar(hilo):
    global contador
    time.sleep(1)
    for _ in range(100):        
        print(hilo)        
        temp = contador   
        time.sleep(0.00001)
        temp += 1          
        contador = temp

h1 = threading.Thread(target=incrementar, args=("h1",))
h2 = threading.Thread(target=incrementar, args=("h2",))

h1.start()
h2.start()

h1.join()
h2.join()

print(contador)


