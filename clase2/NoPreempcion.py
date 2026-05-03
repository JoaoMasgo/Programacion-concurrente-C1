import threading
import time

lock = threading.Lock()

def t1():
    lock.acquire()
    time.sleep(10)   # se lo queda TODO este tiempo
    lock.release()

def t2():
    lock.acquire()   # espera sí o sí

#el sistema NO puede sacarle el lock a t1