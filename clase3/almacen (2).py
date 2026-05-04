import threading
import time

condicion = threading.Condition()
productos = []

def comprador():
    with condicion:
        # Mientras el almacén esté vacío, esperamos
        while len(productos) == 0:
            print("Comprador: Almacén vacío, esperando...")
            condicion.wait() # Suelta el lock y espera notificación
        
        # Al despertar, ya tiene el lock de nuevo
        item = productos.pop()
        print(f"Comprador: Procesé el item {item}")

def vendedor():
    time.sleep(2) # Simula que tarda en producir
    with condicion:
        productos.append("Producto A")
        print("Vendedor: Agregué un producto y aviso.")
        condicion.notify() # Despierta al consumidor

h_comp = threading.Thread(target=comprador)
h_vend = threading.Thread(target=vendedor)

h_comp.start()
h_vend.start()
h_comp.join()
h_vend.join()