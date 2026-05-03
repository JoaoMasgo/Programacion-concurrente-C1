import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def t1():
    with lock1:
        time.sleep(1)
        with lock2:
            print("h1 listo")

def t2():
    with lock2:
        time.sleep(1)
        with lock1:
            print("h2 listo")


h1 = threading.Thread(target=t1)
h2 = threading.Thread(target=t2)

h1.start()
h2.start()
