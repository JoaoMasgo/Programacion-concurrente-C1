import threading

saldo = 1000
lock = threading.Lock()

def retirar():
    global saldo
    for _ in range(100):
        with lock:
            if saldo > 0:
                saldo -= 1