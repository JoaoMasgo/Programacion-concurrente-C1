import time

def tarea():
    time.sleep(2)
    print("Tarea terminada")

inicio = time.time()

for i in range(3):
    tarea()

fin = time.time()

print("Tiempo:", fin - inicio)

