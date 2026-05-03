import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def t1():
    with lock1:
        with lock2:
            pass

def t2():
    with lock1:
        with lock2:
            pass

#ambos igual → sin deadlock

#TIMEOUT

if lock1.acquire(timeout=1):
    print("lo consiguió")
else:
    print("no pudo")

# evita quedarse esperando para siempre

#EVITAR que demore mucho un lock y que haya muchos