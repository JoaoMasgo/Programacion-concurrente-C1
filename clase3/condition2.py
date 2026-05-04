import threading

cond = threading.Condition()
listo = False

def esperar():
    global listo
    with cond:
        while not listo:
            cond.wait()
        print("continuo")

def avisar():
    global listo
    with cond:
        listo = True
        cond.notify()