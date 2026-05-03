import threading
lock1 = threading.Lock()
lock2 = threading.Lock()

def t1():
    with lock1:          # toma lock1
        with lock2:      # pide otro
            pass

"""Hold and wait significa que un hilo 
mantiene un recurso mientras solicita otro.
 Es una condición necesaria para el deadlock, 
 pero por sí sola no lo provoca; se requiere además espera circular."""