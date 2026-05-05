import time

""" def verificar_servidor(nombre, demora):
    print("Verificando", nombre)
    time.sleep(demora)
    print(nombre, "respondio")

servidores = [
    ("Servidor A", 3),
    ("Servidor B", 1),
    ("Servidor C", 2)

]

for nombre, demora in servidores:
    verificar_servidor(nombre, demora) """


import threading

def verificar_servidor(nombre, demora):
    print("Verificando", nombre)
    time.sleep(demora)
    print(nombre, "respondio")

servidores = [
    ("Servidor A", 3),
    ("Servidor b", 1),
    ("Servidor C", 2)
]

threads = []

for nombre, demora in servidores:
    thread = threading.Thread(target=verificar_servidor, args=(nombre, demora))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()